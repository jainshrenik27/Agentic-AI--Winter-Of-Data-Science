from langchain_openai import OpenAI

llm = OpenAI(model = 'gpt')

text = llm.invoke("What is the capital of india")
print(text)