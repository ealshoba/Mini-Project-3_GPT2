# GPT-2 Text Generation:

- This project uses two GPT-2 models to generate text in a conversation-like manner. Model 1 generates the first response, and Model 2 generates the following response based on Model 1's output.

- Start the Flask Server:
    1) In your terminal, navigate to the project directory and run:
    python3 app.py

    2) Access the Web Interface: Open your browser and go to:
    http://127.0.0.1:5000/

    3) Enter a prompt and specify the max length. The conversation will start, with Model 1 generating the first response and Model 2 responding to it.

- How It Works:
    1) The user enter a prompt and specify the max length.
    2) Model 1 (GPT-2) generates the first response based on the user's input.
    3) Model 2 (GPT-2) generates the next response based on Model 1's output.

- Created by:
    This project was created by Elyas Al Shobaki.
