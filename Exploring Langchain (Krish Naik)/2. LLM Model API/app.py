from fastapi import FastAPI
from langserve import add_routes
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
import uvicorn

app = FastAPI(
    title="Ollama LangServe",
    version="1.0",
    description="Serve Ollama (Mistral) via API"
)

prompt = ChatPromptTemplate.from_template("Write a short poem about {topic} for a 5-year-old.")

llm = Ollama(model="mistral")

# Add LangServe route
add_routes(
    app,
    prompt | llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)