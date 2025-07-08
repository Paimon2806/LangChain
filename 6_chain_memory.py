import os 
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory


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

memory = ConversationSummaryMemory(
    llm=llm,
    memory_key="history",
    return_messages=True
)

prompt = ChatPromptTemplate.from_messages(
	[
	("system","You are a chatbot that is a teacher and explain topics like a teacher to a user. The user will provide input in the format 'explain <topic> to me in <level> level.'. You should extract the topic and level from this input."),
    ("placeholder","{history}"),
	("human","{text}")
	])
print("Prompt template defined")



parser = StrOutputParser()
print("parser defined")


# chain = LLMChain(prompt = prompt , memory = memory , llm = llm , output_parser = parser)
chain = prompt | memory | llm | parser

print("chain defined")


response1 = chain.invoke({"text" : "explain langchain to me in basic level."})
print(response1["text"])


response2 = chain.invoke({"text" : "explain langcchain futher please in basic level."})
print(response2["text"])

