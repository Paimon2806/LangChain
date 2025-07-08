import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# llm = AzureChatOpenAI(
#     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#     api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
#     azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
#     deployment_name=os.getenv("AZURE_OEPNAI_DEPLOYMENT_NAME"),
#     model_name="gpt-4o",
#     temperature=0.6
# )


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)



prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful teacher that explains every topic in dept and easy to understand words."),
    ("human", "Explain {topic} to me.")
])

parser = StrOutputParser()

chain = prompt | llm | parser

print("running invoke")
response = chain.invoke({"topic": "Runnable chain in langchain"})
output_filename = "runnable_chain.txt"
with open(output_filename, "w") as f:
    f.write(response)


print("running stream")
output_filename = "attention.txt"
for chunk in chain.stream({"topic":"attention mechanism"}):
    with open(output_filename, "r") as r:
        file_content = r.read()
        chuck = chunk + file_content
    with open(output_filename, "w") as f:
        f.write(chuck)



print("running batch")
responses = chain.batch([
    {"topic":"transformers"},
    {"topic":"prompt engineering"}
])
output_filename = "transformers.txt"
with open(output_filename, "w") as f:
    f.write(responses[0])

output_filename = "prompt engineering.txt"
with open(output_filename, "w") as f:
    f.write(responses[1])






