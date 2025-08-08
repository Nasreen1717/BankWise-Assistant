import os
from dotenv import load_dotenv
from typing import Any
from pydantic import BaseModel, Field
from agents import (
    Agent,
    output_guardrail,
    RunContextWrapper,
    GuardrailFunctionOutput,
    Runner,
    RunConfig,
    AsyncOpenAI,
    OpenAIChatCompletionsModel
)

# Load environment variables from .env file
load_dotenv()

# Configure Gemini provider and model
gemini_api_key = os.getenv("GEMINI_API_KEY")
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Define schema for output guardrail validation
class Check_Res_Class(BaseModel):
    is_not_banking_related: bool = Field(
        description="Set to True if the LLM response is unrelated to banking topics"
    )
    reasoning: str = Field(description="Explanation of the validation decision")

# Initialize output guardrail agent
o_guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions="Ensure LLM responses are strictly related to banking. Set is_not_banking_related to True for non-banking topics, such as Hollywood or unrelated subjects.",
    model=model,
    output_type=Check_Res_Class
)

# Define output guardrail function
@output_guardrail
async def res_check(ctx: RunContextWrapper, agent: Agent, output: Any) -> GuardrailFunctionOutput:
    result = await Runner.run(o_guardrail_agent, output, context=ctx)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_banking_related
    )