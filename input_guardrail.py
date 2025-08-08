import os
from dotenv import load_dotenv
from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    RunConfig,
    AsyncOpenAI,
    OpenAIChatCompletionsModel
)
from pydantic import BaseModel, Field

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

# Define schema for input guardrail validation
class Check_Slang_Class(BaseModel):
    is_abusive: bool = Field(description="Set to True if the user query contains slang or abusive language")
    reasoning: str = Field(description="Explanation of the validation decision")

# Initialize input guardrail agent
i_guardrail_agent = Agent(
    name="Input Guardrail Agent",
    instructions="Always check user queries for abusive or slang words to ensure appropriate communication.",
    model=model,
    output_type=Check_Slang_Class
)

# Define input guardrail function
@input_guardrail
async def check_slangs(ctx: RunContextWrapper, agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(i_guardrail_agent, input, context=ctx, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_abusive
    )