from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
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

prompt1 = PromptTemplate(template = 'Write a joke about {topic}',
                        input_variables=['topic'])

parser = StrOutputParser()

prompt2 = PromptTemplate(template = "Write an explanation of the joke {joke}",
                        input_variables=['joke'])

joke_gen = RunnableSequence(prompt1,model,parser)
pareallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanantion' : RunnableSequence(prompt2,model,parser)
})

chain = RunnableSequence(joke_gen,pareallel_chain)
print(chain.invoke({'topic' : 'girls'}))

