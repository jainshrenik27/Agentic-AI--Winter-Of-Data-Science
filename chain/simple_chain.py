from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template = 'Generate 2 interesting facts about {topic}',
    inupt_variables = ['topic']
)

parser = StrOutputParser()

chain  = prompt | model | parser

result = chain.invoke({'topic' : 'Babar Azam'})

print(result)