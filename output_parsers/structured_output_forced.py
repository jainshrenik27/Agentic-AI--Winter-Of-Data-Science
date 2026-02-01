from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="bastienp/Gemma-2-2B-Instruct-structured-output",
    task="text-generation",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

schema = [ResponseSchema(name = 'fact_1',description = 'Fact1 about the topic'),
          ResponseSchema(name = 'fact_2',description = 'Fact 2 abput the topuc'),
          ResponseSchema(name = 'fact_3',description = 'Fact 3 abput the topuc'),
]
parser = StrOutputParser.from_response_schema(schema)

template = PromptTemplate(
    template = 'Give 3 facts about {topic} \n '
)

chain = template | model | parser
result = chain.invoke({})

 