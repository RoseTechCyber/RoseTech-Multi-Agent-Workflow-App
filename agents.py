from transformers import pipeline

# Load a small local model (CPU-friendly)
generator = pipeline("text-generation", model="gpt2")

def planner_agent(task: str) -> str:
    return generator(f"Break down the task: {task}", max_length=100)[0]["generated_text"]

def coder_agent(task: str) -> str:
    return generator(f"Write Python code to solve: {task}", max_length=150)[0]["generated_text"]

def critic_agent(code: str) -> str:
    return generator(f"Review the following code:\n{code}", max_length=100)[0]["generated_text"]
