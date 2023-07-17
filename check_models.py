import subprocess
import os

# Set the path to your API key file
api_key_file = "api_key.txt"

# Read the API key from the file
with open(api_key_file, "r") as f:
    api_key = f.read().strip()

# Create the list fine-tunes command
list_command = ["openai", "api", "fine_tunes.list"]

# Set the environment variable for the API key
env = dict(os.environ)
env["OPENAI_API_KEY"] = api_key

# Run the list fine-tunes command
result = subprocess.run(list_command, env=env, capture_output=True, text=True)

# Print the output
print(result.stdout)
