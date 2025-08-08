import random
from agents import function_tool
from pydantic import BaseModel

# Define schema for banking purpose identification
class ServiceType(BaseModel):
    service: str
    confidence: float
    keywords_detected: list[str]
    reasoning: str

# Define schema for token generation
class ToolInfo(BaseModel):
    token_number: str
    wait_time: str
    message: str
    service_type: str

# Tool to identify the banking service needed
@function_tool
def identify_banking_purpose(customer_request: str):
    """Identifies the banking service required based on the customer's request."""
    request = customer_request.lower()
    if ("balance" in request) or ("account" in request) or ("statement" in request):
        return ServiceType(
            service="account_service",
            confidence=0.9,
            keywords_detected=["balance", "account", "statement"],
            reasoning="Customer wants to check their account."
        )
    elif ("transfer" in request) or ("send" in request) or ("payment" in request):
        return ServiceType(
            service="transfer_service",
            confidence=0.9,
            keywords_detected=["transfer", "send", "payment"],
            reasoning="Customer wants to send money or make payment."
        )
    elif ("loan" in request) or ("mortgage" in request) or ("borrow" in request):
        return ServiceType(
            service="loan_service",
            confidence=0.9,
            keywords_detected=["loan", "mortgage", "borrow"],
            reasoning="Customer needs help with a loan."
        )
    else:
        return ServiceType(
            service="general_banking",
            confidence=0.5,
            keywords_detected=["general"],
            reasoning="Customer needs general banking assistance."
        )

# Tool to generate a customer service token
@function_tool
def generate_customer_token(service_type: str = "general") -> ToolInfo:
    """Generates a token number for the customer queue based on the service type.
    
    Args: service_type = "general", "account_service", "transfer_service", or "loan_service"
    """
    if service_type == "account_service":
        prefix = "A"
        wait_time = "5-10 minutes"
    elif service_type == "transfer_service":
        prefix = "T"
        wait_time = "2-5 minutes"
    elif service_type == "loan_service":
        prefix = "L"
        wait_time = "15-20 minutes"
    else:
        prefix = "G"
        wait_time = "8-10 minutes"

    token_number = f"{prefix}{random.randint(100, 999)}"
    return ToolInfo(
        token_number=token_number,
        wait_time=wait_time,
        message=f"Please take token {token_number} and wait for {wait_time}. Have a seat, and we will call you shortly!",
        service_type=service_type
    )