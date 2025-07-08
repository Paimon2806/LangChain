import os 
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

load_dotenv()

llm = AzureChatOpenAI (
	api_key = os.getenv("AZURE_OPENAI_API_KEY"),
	api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
	azure_endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT"),
	deployment_name = os.getenv("AZURE_OEPNAI_DEPLOYMENT_NAME"),
	temperature = 0.6,
	model_name = "gpt-4o"
	)
print("llm defined")

template = ChatPromptTemplate.from_messages(
	[
	("system","You are a chatbot that is a teacher and explain topics like a teacher to a user."),
	("human","explain {topic} to me in {level} level.")
	])
print("Template defined")



parser = StrOutputParser()
print("parser defined")


chain = LLMChain(prompt = template , llm = llm , output_parser = parser)
# chain = LLMChain(llm=llm, prompt=template, output_parser=parser)

print("chain defined")


response = chain.invoke({"topic" : "langchain" , "level" : "basic"})

print(response["text"])


