from langchain_core.prompts import ChatMessagePromptTemplate , MessagesPlaceholder
 
 #chat history 
chat_template = ChatMessagePromptTemplate(
  [
   ('system' ,'You are a helpful assistant    ')
  ]
 )
chat_history = []
 #load chat history 
with open('chat_history.txt') as f:
    chat_history.append(f.readlines())

print(chat_history)
 #create prompt
prompt = chat_template.invoke()