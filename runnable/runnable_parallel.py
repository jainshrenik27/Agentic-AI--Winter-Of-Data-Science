from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.runnables import RunnableSequence,RunnableParallel
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

promp2 = PromptTemplate("Write an explanation of the joke {joke}",
                        input_variables=['joke'])
chain = RunnableParallel({
    'joke' : RunnableSequence(prompt1,model,parser)
    'explanantion' : RunnableSequence(prompt2,)

})

print(chain.invoke({'topic' : 'cricket'}))
