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
    model="gemini-2.0-flash-lite",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)



prompt = ChatPromptTemplate.from_messages([
    ("system", "You are my helper that helps me prepare for interview. I will ask you interview questions and you answer them how I am supposed to answer them."),
    ("human", "{topic} to me.")
])

parser = StrOutputParser()

chain = prompt | llm | parser
#
# print("running invoke")
# response = chain.invoke({"topic": "What is the role of an activation function? Name a few common ones and their use cases."})
# output_filename = "text/activation_function.txt"
# with open(output_filename, "w") as f:
#     f.write(response)


# print("running stream")
# output_filename = "attention.txt"
# content = ""
# for chunk in chain.stream({"topic":"attention mechanism"}):
#     content += chunk
# with open(output_filename, "w") as f:
#     f.write(content)



print("running batch")
responses = chain.batch([
    {"topic":"You've mentioned proficiency in Python and popular ML libraries. Can you explain the typical use cases for NumPy, Pandas, and Scikit-learn in a machine learning workflow?"},
    {"topic":"Describe a scenario where you would use groupby() and pivot_table() in Pandas."},
    {"topic":"What's the difference between a list and a tuple in Python? When would you use one over the other?"},
    {"topic":"Explain what a dictionary is in Python and its common applications."}
])
output_filename = "text/libraries.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(responses[0])

output_filename = "text/pandas.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(responses[1])

output_filename = "text/list_vs_tuple.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(responses[2])

output_filename = "text/dictionary.txt"
with open(output_filename, "w" , encoding="utf-8") as f:
    f.write(responses[3])





