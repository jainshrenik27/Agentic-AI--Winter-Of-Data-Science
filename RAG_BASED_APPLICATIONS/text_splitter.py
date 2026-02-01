from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

df = PyPDFLoader('shrenik.pdf')

df = df.load()

# print(df)
# print((df[1].metadata))
splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
    )
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
)
 
result = splitter.split_documents(df)

print(result)