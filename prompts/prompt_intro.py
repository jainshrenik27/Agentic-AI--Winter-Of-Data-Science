
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint ,HuggingFaceEmbeddings
from langchain_core.messages import HumanMessage

HF_TOKEN = "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"

llm = HuggingFaceEndpoint(repo_id = "mistralai/Mistral-7B-Instruct-v0.2",task = "conversational",huggingfacehub_api_token=HF_TOKEN,
        temperature =  1.0,
    )
llm = HuggingFaceEmbeddings(repo_id = "sentence-transformers/all-MiniLM-L6-v2",task = "feature -extraction ",huggingfacehub_api_token=HF_TOKEN,
        temperature =  1.0,
    )
model = ChatHuggingFace(llm = llm)

text = "Explain me about magnus carlsen"



