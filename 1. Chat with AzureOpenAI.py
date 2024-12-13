import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


# Load environment variables from .env
load_dotenv()

# Initiate an LLM model based on Azure OpenAI Deployment
llm_model = AzureChatOpenAI(
    azure_deployment="gpt-35-turbo-kumar",  # your deployment
    api_version="2023-03-15-preview",  #your api version
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# Simple Chat
# messages = "List top 5 greatest achievements by Sachin Tendulkar!"
# result = llm_model.invoke(messages)


### Using Messages
## Coding Assistant
# messages = [
#     ("system", "You are a helpful assistant that helps with writing Python code. Create sample code with user sentence."),
#     ("human", "Sort Customers by their Last Name"),
# ]

## General Knowledge Assistant
# messages = [
#     (
#         "system",
#         "You are a helpful AI assistant that helps with Facts. Provide answer to User input.",
#     ),
#     # ("human", "What is most common surname for men in India other than 'Patel'")
#     ("human", "What are the most common surnames in India"),
# ]

## Math Assistant
# messages = [
#     ("system", "You are a helpful assistant that helps with solving Math Problems. Explain user input to middle school kid."),
#     ("human", "Why 1/0 is not 0, and 1/0 is infinity?"),
# ]

## AI Messages
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="Why 81 divided by 9 is 9?"),
]

result = llm_model.invoke(messages)

print("Full result:\n-----------")
print(result)

print("\nContent only:\n------------")
print(result.content)
print("\n\n")
