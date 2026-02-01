from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)
model = ChatHuggingFace(llm=llm)
def word_count(text):
    return text.split()
# 2️⃣ Wrap as chat model


prompt1 = PromptTemplate(template = 'Write a joke about {topic}',
                        input_variables=['topic'])

parser = StrOutputParser()

prompt2 = PromptTemplate(template = "Write an explanation of the joke {joke}",
                        input_variables=['joke'])
joke_gen = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough() ,
    'word_count' : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen,parallel_chain)

result = (final_chain.invoke({'topic' : 'AI'}))

print(result)