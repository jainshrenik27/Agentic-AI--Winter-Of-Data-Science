🤖 Agentic-AI — Winter of Data Science

This repository documents my learning journey and hands-on work during Winter of Data Science, focused on Agentic AI, Hugging Face models, neural networks from scratch, and LangChain.

📂 Project Structure & Contents
📁 hugging_face_models.ipynb

This notebook contains hands-on experiments using the Hugging Face Transformers library with different NLP pipelines.

1️⃣ Text Summarization

Uses pipeline("summarization") from transformers

A long paragraph (4–5 sentences) is defined as a single Python string

The summarization pipeline is applied with appropriate min_length and max_length values to control summary size

2️⃣ Text Generation

Uses pipeline("text-generation")

A prompt such as:

"In 2030, AI systems will"


is passed to the model

Demonstrates open-ended text generation using a pretrained language model

3️⃣ Sentiment Analysis

Uses pipeline("sentiment-analysis")

Performs sentiment classification on sample input text

Outputs sentiment labels and confidence scores

📁 Neural_network_from_scratch

Implemented a Neural Network from scratch without using high-level deep learning frameworks

Applied to the MNIST handwritten digit dataset

Covers:

Forward propagation

Backpropagation

Weight and bias updates

Training and evaluation logic

Complete implementation is provided in the notebook inside this folder

📁 Langchain

Hands-on learning and experimentation with the LangChain framework

Focuses on building agentic AI workflows

Explores:

LLM orchestration

Tool usage

Prompt chaining


Agent-based reasoning

Emphasis on practical understanding rather than theory

🎯 Learning Outcomes

Practical understanding of Hugging Face NLP pipelines

Strong grasp of neural network fundamentals by implementing one from scratch

Exposure to agentic AI concepts using LangChain

Experience in structuring AI workflows and experiments in notebooks
