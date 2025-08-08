from agents import Agent
from output_guardrail import res_check

# Define agent for account-related services
account_agent = Agent(
    name="Account Services Agent",
    instructions="Assist users with queries about account balances, statements, and account information. Always generate a service token.",
    model="gemini-2.0-flash",
    output_guardrails=[res_check]
)

# Define agent for transfer-related services
transfer_agent = Agent(
    name="Transfer Services Agent",
    instructions="Assist users with money transfers and payments. Always generate a service token.",
    model="gemini-2.0-flash",
    output_guardrails=[res_check]
)

# Define agent for loan-related services
loan_agent = Agent(
    name="Loan Services Agent",
    instructions="Assist users with loans and mortgages. Always generate a service token.",
    model="gemini-2.0-flash",
    output_guardrails=[res_check]
)