import openai
import os

# Set the path to your API key file
api_key_file = "api_key.txt"

# Read the API key from the file
with open(api_key_file, "r") as f:
    api_key = f.read().strip()

# Set the API key
openai.api_key = api_key

# Define the fine-tuned model ID
fine_tuned_model_id = "curie:ft-personal:my-finetuned-model-2023-07-17-12-45-18"

# Define your prompt
prompt = "Say if the following function, is a norm on $\mathbb{R}^3$. \[\max\left\{\sqrt{x_1^2+x_2^2},|x_3|\right\}\]"

# Define the temperature
temperature = 0.8

# Define the max tokens
max_tokens = 100

# Generate a completion using the fine-tuned model
response = openai.Completion.create(
    model=fine_tuned_model_id,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Get the generated completion text
completion_text = response.choices[0].text.strip()

# Print the generated completion
print(completion_text)
