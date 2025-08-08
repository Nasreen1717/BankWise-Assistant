import os
from dotenv import load_dotenv
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from agents import InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
import rich
from input_guardrail import check_slangs
from my_tools import generate_customer_token, identify_banking_purpose
from handoff_agents import account_agent, transfer_agent, loan_agent

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

# Initialize the main banking assistant agent
agent = Agent(
    name="BankWise Assistant",
    instructions="""
    You are a professional and friendly banking assistant.

    1. Greet customers warmly and professionally.
    2. Use identify_banking_purpose to determine the customer's needs.
    3. If confidence > 0.8, direct the customer to the appropriate specialist.
    4. Always use generate_customer_token to issue a service token.

        # Example: argument for generate_customer_token can only be (service_type = "general" or service_type = "account_service" or service_type = "transfer_service" or service_type = "loan_service")
            
    Always provide helpful and courteous service.
    """,
    model=model,
    handoffs=[account_agent, transfer_agent, loan_agent],
    tools=[generate_customer_token, identify_banking_purpose],
    input_guardrails=[check_slangs],
)

# Run interactive loop for customer queries
while True:
    try:
        user_input = input("\n💼 Welcome to BankWise Assistant. How may I assist you today? ")
        if user_input.lower() in ['quit', 'exit']:
            break

        result = Runner.run_sync(agent, user_input, run_config=config)
        rich.print(result.final_output)
       

    except InputGuardrailTripwireTriggered as e:
        print("⚠️ We apologize, but your input contains inappropriate language. Please rephrase your request.")
    except OutputGuardrailTripwireTriggered as e:
        print("⚠️ We apologize, but we cannot process this request. Please contact our support team for assistance.")