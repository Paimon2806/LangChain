import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage , HumanMessage
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
	api_key=os.getenv("AZURE_OPENAI_API_KEY"),
	deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
	api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
	azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
	temperature=0.6
	)
print("llm initialised.")



prompt_template=ChatPromptTemplate(
	[
		("system","you are a helpfull assistant that explains complex concepts consisely"),
		("human","Explain theses {concept} properly"),
	]
	)
print("Prompt Defined")


message_blockchain = prompt_template.format_messages(concept="blockchain")
message_quantum = prompt_template.format_messages(concept="Quantum computer")
print("prompts are formatted for blockchain and quantum computer")


print("LLM invoking for blockchain")
response_blockchain = llm.invoke(message_blockchain)
print(f"{response_blockchain.content}")


print("LLM invoking for quantum computer")
response_quantum = llm.invoke(message_quantum)
print(f"{response_quantum.content}")




