import os
import json

def extract_problems_and_solutions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    pairs = []
    start_prompt = "{Prompt}"
    start_completion = "{Completion}"
    end_prompt = "{Completion}"

    while True:
        prompt_start_index = content.find(start_prompt)
        if prompt_start_index == -1:
            break

        prompt_end_index = content.find(end_prompt, prompt_start_index)
        if prompt_end_index == -1:
            break

        completion_start_index = content.find(start_completion, prompt_end_index)
        if completion_start_index == -1:
            break

        completion_end_index = content.find(start_prompt, completion_start_index)
        if completion_end_index == -1:
            completion_end_index = len(content)

        prompt = content[prompt_start_index + len(start_prompt):prompt_end_index].strip()
        completion = content[completion_start_index + len(start_completion):completion_end_index].strip()

        pairs.append({"prompt": prompt, "completion": completion})

        content = content[completion_end_index:]

    return pairs

def create_training_data(file_path):
    pairs = extract_problems_and_solutions(file_path)

    # Create the "training_data" directory if it doesn't exist
    output_directory = 'training_data'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create the output file path
    file_name = "training_data.jsonl"
    output_file_path = os.path.join(output_directory, file_name)

    # Write the problem and solution pairs to the output file
    with open(output_file_path, 'w') as output_file:
        for pair in pairs:
            json.dump(pair, output_file)
            output_file.write('\n')

    print(f"Training data file created: {output_file_path}")

def process_problem_sets_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            create_training_data(file_path)

# Example usage
folder_path = 'problem_sets'
process_problem_sets_folder(folder_path)
