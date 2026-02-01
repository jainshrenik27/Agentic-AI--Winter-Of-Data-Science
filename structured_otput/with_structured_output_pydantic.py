from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage ,SystemMessage
from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from langchain_core.
from pydantic import BaseModel

HF_TOKEN = "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"

# 1️⃣ Correct HF endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    huggingfaceh    ub_api_token=HF_TOKEN,
)

# 2️⃣ Wrap as chat model
model = ChatHuggingFace(llm=llm)

# custom schema

class Review(BaseModel):
    key_themes: List[str] = Field(
        description="Write down all the key themes discussed in the review in a list"
    )

    summary: str = Field(
        description="A brief summary of the review"
    )

    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either negative, positive or neutral"
    )

    pros: Optional[List[str]] = Field(
        default=None,
        description="Write down all the pros inside a list"
    )

    cons: Optional[List[str]] = Field(
        default=None,
        description="Write down all the cons inside a list"
    )

    name: Optional[str] = Field(
        default=None,
        description="Write the name of the reviewer"
    )
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
