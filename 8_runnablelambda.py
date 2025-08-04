import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful teacher that explains every topic in dept and easy to understand words."),
    ("human", "{topic}")
])

def level_formatter(inputs: dict) -> dict:
    level = inputs.get("level", "basic")
    if level == "beginner":
        inputs["topic"] = f"Explain '{inputs['topic']}'in simple terms"
    elif level == "advanced":
        inputs["topic"] = f"Explain {inputs['topic']}with technical details"
    else:
        inputs["topic"] = f"Explain {inputs['topic']}"
    return inputs

formatter = RunnableLambda(level_formatter)

parser = StrOutputParser()

chain = formatter | prompt | llm | parser

print("running invoke")

response = chain.invoke({"topic": "transformer architecture", "level": "expert"})
print(response)













