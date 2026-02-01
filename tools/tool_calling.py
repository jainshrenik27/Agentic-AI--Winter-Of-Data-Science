from langchain_core.tools import StructuredTool,tool
from langchain_huggingface import ChatHuggingFace,HuggingFaceEmbeddings,HuggingFaceEndpoint
from pydantic import BaseModel,Field

HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)
model = ChatHuggingFace(llm = llm)


@tool
def multiply(a : int , b: int ) -> int:
    """multiply 2 numbers a and b and return their product"""
    return a*b

print(multiply.invoke({'a' : 3,'b' : 4}))


# tool calling

llm_with_tools = model.bind_tools([multiply])

result = llm_with_tools.invoke('Can you multiply 3 with 10 ')


#tool execution

print(multiply.invoke(result.tool_calls[0]))

