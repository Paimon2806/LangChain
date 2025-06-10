import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
API_BASE = os.getenv("AZURE_OPENAI_API_ENDPOINT")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")



print("attemting to initialize AzureChatOpenAI...")

try:

	llm=AzureChatOpenAI(
		deployment_name=DEPLOYMENT_NAME,
    	api_key=API_KEY,
    	api_version=API_VERSION,
    	model="gpt-4o",
    	azure_endpoint=API_BASE,
    	
		temperature=0.7
	)
	print("AzureChatOpenAI initialized Successfully.")

	messages = [
		SystemMessage(content="You are a friendly and helpful AI Assiatant that provides concise answer."),
		HumanMessage(content="What is the capital of Canada?")
	]

	print("Messages Prepared")

	print("Invoking the LLM with the prepared message...")
	response = llm.invoke(messages)


	print("\n-- LLM Response ---")
	print(f"{response.content}")

except Exception as e:
	print("Error")


