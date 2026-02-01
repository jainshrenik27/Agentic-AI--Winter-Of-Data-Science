from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from langchain_core.runnables import RunnableBranch,RunnableLambda
HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field('give the sentiment of the feedback as one of the literals')

parser2 = PydanticOutputParser(pydantic_object= Feedback)

parser1 = StrOutputParser()

prompt1 = PromptTemplate(template = 'Classifiy the feedback of the following feedback text \n {text} \n {format_instructions}',
                         input_variables= ['text'],
                         partial_variables={'format_instructions' : parser2.get_format_instructions()})

classifier_chain = prompt1 | model | parser2


branch_chain = RunnableBranch(
    (),
    ()
)

chain = classifier_chain | branch_chain

result  =chain.invoke({'text' : 'The samartphone is very wonderful to use'} 
)

print(result)

