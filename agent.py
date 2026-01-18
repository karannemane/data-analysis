from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain_community.tools import Tool
from langgraph.prebuilt import create_react_agent

from tools import preview_csv, summary_csv, missing_csv

tools = [
    Tool("Preview CSV", preview_csv, "Preview CSV rows"),
    Tool("Summary CSV", summary_csv, "Statistical summary"),
    Tool("Missing Values", missing_csv, "Find missing values"),
]

_agent = None

def load_agent():
    global _agent
    if _agent is None:
        llm_pipeline = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            max_new_tokens=300
        )
        llm = HuggingFacePipeline(pipeline=llm_pipeline)
        _agent = create_react_agent(llm=llm, tools=tools)
    return _agent

def run_agent(question: str) -> str:
    agent = load_agent()
    result = agent.invoke({"messages": [("user", question)]})
    return result["messages"][-1].content
