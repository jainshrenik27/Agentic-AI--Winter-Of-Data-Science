from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage ,SystemMessage
from typing import TypedDict,Annotated

HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfacehub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

# 3️⃣ Define schema
class Review(TypedDict):
    summary: Annotated[str,"Give me a breif ssummary of the review"]
    sentiment: str 

# 4️⃣ Create structured-output model
structured_model = model.with_structured_output(Review)

# 5️⃣ Invoke with chat messages
result = structured_model.invoke([
    SystemMessage(content=(
        "Return ONLY valid JSON. "
        "Do NOT include explanations, markdown, or text outside JSON. "
        "The response MUST exactly match the schema."
    )),
    HumanMessage(content="summary = The hardware is great but the battery overheats. sentiment = postitive")
])


print((result))
