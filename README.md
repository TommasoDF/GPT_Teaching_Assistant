# Fine-tuning a GPT model

This repository contains code and instructions for fine-tuning a model using OpenAI's GPT-3.5 API. By fine-tuning the model, you can customize its behavior for specific tasks and domains.

## Prerequisites

Before proceeding with the fine-tuning process, make sure you have the following:

1. OpenAI API Key: Obtain your API key from the OpenAI platform. You can generate API keys in the OpenAI web interface. See [here](https://platform.openai.com/account/api-keys) for details.


2. Training Data: Prepare your training data in the desired format. The training data should be a collection of prompts and corresponding completions, with the following structure:
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
The file must be a .JSONL file.


## Steps to Fine-tune the Model

1. Clone the Repository:

   ```
   git clone <repository_url>
   ```
2. Set your API KEY:

    Once you have your api key, copy and paste it into the file 'api_key.txt'.

3. Prepare Training Data:

    Place your training data in the `training_data` directory. 
    In our case we had some problem sets with solutions written in LaTeX.
    The 'fine_tune.py' file expects your input files to be in the `problem_sets` folder, in .txt format.
    The .txt should have the following structure: {prompt} <Excercise> {completion} <your solution>.
    Running 
    ```
   python fine_tune.py
   ```
   will generate a file called `training_data` in the `training_data` directory.
   Check this file to make sure that the structure is the one expected.

4. Create a Fine-tuning Job:

   Run the following command to initiate the fine-tuning process:

   ```
   python fine_tune.py
   ```

   This script will create a fine-tuning job using the 'curie' base model and your training data. The job will be submitted to the OpenAI API for processing. If you want to change the model that is going to be fine-tuned you can just change the 'base_model' field.

5. Monitor Job Status:

   Use the following command to monitor the status of your fine-tuning job:

   ```
   python check_job_status.py
   ```

   This script will display the status of your fine-tuning job, such as 'pending', 'running', 'succeeded', or 'failed'. Wait until the job is complete.

6. Access Fine-tuned Model:

   Once the fine-tuning job is completed, you will receive the ID of the fine-tuned model. Use this ID to refer to your fine-tuned model in subsequent API calls.

   Update the `fine_tuned_model_id` variable in the `use_fine_tuned_model.py` script with the obtained model ID.

7. Use the Fine-tuned Model:

   Run the following command to generate completions using the fine-tuned model:

   ```
   python use_fine_tuned_model.py
   ```

   This script will use the fine-tuned model to generate completions based on the provided prompts.

That's it! You have successfully fine-tuned the 'curie' model and can now utilize it for your specific tasks.

---
