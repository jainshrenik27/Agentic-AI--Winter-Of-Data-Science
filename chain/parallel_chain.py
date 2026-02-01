from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnabelParallel
HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(template= 'Generate short and simple text from the following text \n {text}',
                         input_variables=['text'])

prompt2 = PromptTemplate(template = 'Generate  5 short question and answers on the follwowing \n {text}',
                         input_variables= ['text'])

prompt3 = PromptTemplate()

parallel_chain = RunnabelParallel()

merge_chain = prompt3 | model1 | parser 

chain = parallel_chain | merge_chain

