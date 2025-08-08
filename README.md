
# **BankWise Assistant**

*A Secure AI-Powered Banking Application with Handoff and Guardrails*

## **Overview**

BankWise Assistant is a secure, AI-driven banking assistant built using the **OpenAI Agent SDK** with **Gemini API** integration.
It uses **handoff agents**, **function tools**, and **input/output guardrails** to ensure professional, safe, and accurate customer service interactions.

The system can:

* Detect a customer’s banking needs (Account, Transfer, Loan, General)
* Redirect queries to the right specialist (handoff mechanism)
* Generate customer service tokens with wait times
* Prevent inappropriate language (input guardrails)
* Block irrelevant or unsafe responses (output guardrails)

This makes it ideal for building **secure conversational banking experiences**.

---

## **Features**

* 🔹 **AI-powered intent detection** – identifies customer requests with high confidence
* 🔹 **Secure communication** – filters abusive input & unrelated outputs
* 🔹 **Handoff mechanism** – routes customers to specialized banking agents
* 🔹 **Token generation** – assigns unique tokens with estimated wait times
* 🔹 **Environment-based API configuration** – secure handling of API keys

---

## **Project Structure**

```
bankwise-assistant/
│
├── mai.py                     # Main application entry point
├── my_tools.py                # Tools: Identify purpose & Generate tokens
├── handoff_agents.py          # Specialized banking agents
├── input_guardrail.py         # Input safety checks
├── output_guardrail.py        # Output topic relevance checks
├── .env                       # Environment variables (GEMINI_API_KEY)
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
```

---

## **Tech Stack**

* **Python 3.10+**
* **OpenAI Agent SDK**
* **Google Gemini API**
* **Pydantic** for schema validation
* **dotenv** for environment variables
* **Rich** for colored console output
* **uv** for running the project

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/bankwise-assistant.git
cd bankwise-assistant
```

### **2. Create a Virtual Environment**

Using `uv` (recommended):

```bash
uv venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

Or using `venv`:

```bash
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
```

### **3. Install Dependencies**

```bash
uv pip install -r requirements.txt
```

Or without uv:

```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> **Note:** Get your Gemini API key from the [Google AI Studio](https://makersuite.google.com/).

---

## **Running the Application**

### **With uv (Recommended)**

```bash
uv run mai.py
```

### **With Python**

```bash
python mai.py
```

You should see:

```
💼 Welcome to BankWise Assistant. How may I assist you today?
```

Type your banking query, for example:

```
I want to check my account balance.
```

---

## **How It Works**

### **1. Input Guardrails** (`input_guardrail.py`)

* Checks for slang or abusive words before processing.
* If triggered → politely asks the customer to rephrase.

### **2. Intent Detection** (`my_tools.py`)

* Uses `identify_banking_purpose()` to determine the service type:

  * Account Service
  * Transfer Service
  * Loan Service
  * General Banking

### **3. Handoff to Specialized Agents** (`handoff_agents.py`)

* Directs customers to the correct agent based on intent.

### **4. Token Generation**

* `generate_customer_token()` issues a unique token & wait time.
* Example: `"Please take token A472 and wait for 5-10 minutes."`

### **5. Output Guardrails** (`output_guardrail.py`)

* Ensures AI responses stay banking-related.
* If irrelevant → blocks and asks for clarification.

---

## **Example Interaction**

```
💼 Welcome to BankWise Assistant. How may I assist you today?
> I want to apply for a loan.

🔹 Detected Service: Loan Service
🔹 Token: L283
🔹 Wait Time: 15-20 minutes
💬 Please take token L283 and wait for 15-20 minutes. Have a seat, and we will call you shortly!
```

---

## **Security Considerations**

* **No sensitive data is stored** – all processing is session-based.
* **Guardrails prevent harmful or unrelated content** from entering or leaving the system.
* **Environment variables** protect API keys.

---

## **Future Improvements**

* 🖥 Web-based UI with Streamlit or FastAPI
* 📊 Admin dashboard for token tracking
* 🔔 Real-time notifications when token is called
* 🌎 Multilingual support

---

## **License**

This project is licensed under the **MIT License** – free to use, modify, and distribute.




