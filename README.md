Here's the markdown text for your project:

# FSTT-LLM-Chat-Bot

A chat bot for the FSTT-LLM project. Fine-tuned Llama3 8B instruct.

> [!WARNING]  
> If you want to run the project on docker, know that the containers will take up to 50GB of disk space in total.

## Setup Instructions

1. **Go to the source directory**: Make sure you have the necessary storage requirements.

2. **Install and open MongoDB**: Create a database named `chat-ui` and a collection with the same name.

3. **Download the model**: 
   - Download the model from this [link](https://huggingface.co/aL0NEW0LF/unsloth-llama-3-q4_k_m).
   - Place the downloaded model in the base folder.

4. **Start the project**:
   - Open a terminal in the base directory.
   - Run the following command to start the project:
     ```bash
     docker-compose -f docker-compose.yml up -d
     ```

5. **Access the project**:
   - Open your web browser and go to `localhost:3000`.

Your project should now be up and running!
