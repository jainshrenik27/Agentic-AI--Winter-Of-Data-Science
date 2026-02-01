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

#1st prompt 
template1 = PromptTemplate(template = "Write a detailed report on {topic}",input_variables =['topic'] )

template2  =PromptTemplate(template = "write a 5 short line summary on the following {text}",input_variables = ['text'])

# prompt1 = template1.invoke({'topic' :'black-hole'})

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text' : result.content})

# result1 = model.invoke(prompt2)

# print(result.content)
# print(result1.content)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : 'black hole'})

print(result)