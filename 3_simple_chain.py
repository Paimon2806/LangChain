import os 	
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = AzureChatOpenAI(
	api_key = os.getenv("AZURE_OPENAI_API_KEY"),
	api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
	azure_endpoint = os.getenv("AZURE_OPENAI_API_ENDPOINT"),
	deployment_name = os.getenv("AZURE_OEPNAI_DEPLOYMENT_NAME"),
	model_name = "gpt-4o",
	temperature = 0.6
	)

prompt_template = ChatPromptTemplate.from_messages([
	("system","You are a helpful assistant that helps with coding and teach like a teacher."),
	("human","Explain this {topic} to me , in {level} level.")
	])

print("Prompt Defined")

output_parsers = StrOutputParser()
print("Output prasers defined")

# message = prompt_template.format_messages(topic="langchain framework")



chain = prompt_template | llm | output_parsers

response = chain.invoke({"topic":"langchain framework", "level" : "advance"})

print(f"{response}")