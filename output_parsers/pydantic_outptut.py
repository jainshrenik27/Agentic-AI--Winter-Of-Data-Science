from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from langch
HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()
  

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : 'black hole'})

print(result)