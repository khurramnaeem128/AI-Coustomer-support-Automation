# AI Customer Support Automation

## Project Overview

AI Customer Support Automation is a real-world AI-powered customer support system designed to automatically receive, validate, process, classify, and respond to customer inquiries. The system combines a customer-facing frontend, FastAPI backend, n8n workflow automation, an AI Agent with an OpenRouter LLM, Google Sheets logging, and human-support escalation through email.

The project demonstrates how AI, backend APIs, workflow automation, validation, error handling, data logging, and human-in-the-loop support can work together as one complete automation system.

---

## Key Features

* Customer inquiry web form
* FastAPI backend API
* Pydantic request and response validation
* API key validation
* Required-field validation
* Email format validation
* Customer message validation
* AI-powered inquiry classification
* Inquiry priority detection
* Human-support requirement detection
* AI-generated customer responses
* OpenRouter LLM integration
* Google Sheets inquiry logging
* Automatic human-support escalation
* Email notification for human escalation
* Backend error handling
* CORS configuration
* End-to-end frontend-to-AI workflow

---

## System Architecture

```text
Customer
   │
   ▼
Frontend Web Form
   │
   ▼
FastAPI Backend
   │
   ▼
n8n Webhook
   │
   ├── API Key Validation
   ├── Required Fields Validation
   ├── Email Validation
   └── Message Validation
          │
          ▼
   AI Customer Support Agent
          │
          ▼
      OpenRouter LLM
          │
          ▼
    Structured AI Response
          │
          ├──────────────► Google Sheets
          │
          ▼
   Human Escalation Check
       │           │
      TRUE        FALSE
       │           │
       ▼           ▼
 Human Support   AI Response
 Email            │
       │           │
       ▼           ▼
 Human Escalation Response
              │
              ▼
            Customer
```

---

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Pydantic
* Requests
* python-dotenv

### AI & Automation

* n8n
* AI Agent
* OpenRouter
* Large Language Model (LLM)

### Data & Communication

* Google Sheets
* Email notification

---

## Workflow Explanation

### 1. Customer Inquiry

The customer submits their name, email address, and message through the web form.

### 2. FastAPI Backend

The frontend sends the inquiry to the FastAPI backend. FastAPI validates the incoming data using Pydantic.

### 3. API Security

The backend sends the request to the n8n webhook with an API key for request authentication.

### 4. Request Validation

The n8n workflow validates:

* API key
* Required fields
* Email format
* Message quality

Invalid requests receive appropriate error responses.

### 5. AI Processing

The AI Customer Support Agent processes the valid inquiry and determines:

* Inquiry category
* Priority
* Whether human support is required
* Appropriate customer response

The AI is instructed not to invent company information or pricing.

### 6. Data Logging

Customer inquiry information and the AI-generated result are stored in Google Sheets for record keeping and support tracking.

### 7. Human Escalation

If the AI determines that human assistance is required, n8n sends an email notification to human support.

### 8. Customer Response

The customer receives either an AI-generated response or a human-escalation confirmation.

---

## Inquiry Categories

The AI system can classify inquiries into:

* `service_inquiry`
* `pricing_inquiry`
* `technical_support`
* `general_inquiry`
* `human_escalation`

The system also assigns:

* `low`
* `medium`
* `high`

priority levels.

---

## Project Structure

```text
AI Coustomer support Automation/
│
├── frontend/
│   └── index.html
│
├── n8n/
│   └── AI_Customer_Support_Automation.json
│
├── backened/
│   ├── main.py
│   └── .env
│
├── .gitignore
└── README.md
```

---

## Backend API

### Endpoint

```text
POST /customer-inquiry
```

### Example Request

```json
{
  "name": "Ahmed",
  "email": "ahmed@example.com",
  "message": "I need help with your service."
}
```

### Example Successful Response

```json
{
  "success": true,
  "response": "Sure! Could you please provide more details about what you need help with regarding our service?"
}
```

---

## Validation

The backend validates:

* Name length
* Valid email format
* Message length
* Required fields

Invalid input is rejected with an appropriate HTTP validation response.

The n8n workflow also performs additional validation before sending data to the AI system.

---

## Error Handling

The backend handles important integration failures, including:

* Invalid customer input
* Invalid email
* Missing required fields
* n8n connection failure
* n8n timeout
* Invalid response from the automation system

For example:

```text
502 Bad Gateway
Unable to connect to the support automation.
```

when the n8n automation is unavailable.

---

## Environment Variables

Sensitive configuration is stored in the `.env` file instead of being placed directly in the Python source code.

Example:

```env
N8N_API_KEY=your_api_key
N8N_WEBHOOK_URL=your_webhook_url
```

The `.env` file should never be committed to a public repository.

---

## Testing

The system has been tested across multiple scenarios:

### Successful Cases

* Valid customer inquiry
* General inquiry
* Pricing inquiry
* Technical support inquiry
* Human escalation
* Frontend-to-backend communication
* Backend-to-n8n communication
* AI response generation

### Validation Cases

* Missing required fields
* Invalid email
* Short/invalid message
* Invalid API key
* Invalid request data

### Error Handling

* n8n unavailable
* Backend integration failure
* Timeout handling
* Invalid automation response

---

## Security

The project includes several security and reliability measures:

* API key validation
* Environment variables for sensitive configuration
* Input validation with Pydantic
* n8n request validation
* Error handling
* CORS configuration

Production deployment should use restricted CORS origins, HTTPS, secure secret management, and production-grade authentication.

---

## Future Improvements

Possible future improvements include:

* Authentication and authorization
* Database-based customer history
* Admin dashboard
* Conversation history
* Advanced analytics
* Rate limiting
* Production monitoring
* Better human-support management
* Deployment with production infrastructure
* More advanced AI/RAG capabilities

---

## Project Goal

The goal of this project is to demonstrate a practical AI automation system that can reduce manual customer-support workload while maintaining validation, logging, AI-based decision making, and human escalation when required.

This project combines **AI Engineering, Backend Development, API Integration, and Workflow Automation** into one real-world application.
