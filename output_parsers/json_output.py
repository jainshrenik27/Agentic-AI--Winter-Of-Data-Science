from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

#template
template = PromptTemplate(
    template="Give me 5 facts about {topic} \n{format_instruction}",
    input_variables=['topic'],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({'topic': 'competitive programming' })
print((result))
