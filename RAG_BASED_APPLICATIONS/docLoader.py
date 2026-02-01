from langchain_community.document_loaders import PyPDFLoader
df = PyPDFLoader('shrenik.pdf')

docs = df.load()

print((docs[0].metadata
       ))