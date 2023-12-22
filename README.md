# Run remote LLMs from streamlit 
using the web API from OPenAI and/or Mistral.

Experiments with [Streamlit](https://streamlit.io/)

These are my first streamlit projects, so be kind when commenting :)

The `openai-spike.py` code is based on the example on the LLM section of the streamlit website.

The `mistral-api.py` and m̀ulti-mistral.py`projects are inspired by the OpenAI example.

The OpenAI app maintains a chat history.

The two mistral apps are one-shot apps at present; in other words, they don't maintain a history of the chat.
Each prompt starts a new chat session.

`mistreal-api.py` sends your prompt to the `mistral-tiny`model and displays the result.

`multi-mistral` send your prompt to `mistral-tiny`, `mistral-small` and `1mistral-medium`.
It displays your prompt and each model's response to it.

To run any of these you will need accounts with OpenAI and/or Mistral's **La PLatforme**.

A web search should tell you how to obtain them. Since you'll have to pay for usage,
make sure you have **set a limit on how much you are willing to spend**.

Once you have the relevant API key or keys, you'll need to install the relevant software.

These instructions are for Linux, including the Raspberry Pi 5, on which streamlit runs very well.)

1. Clone this repository into a directory of your choice
   ```shell
   git clone https://github.com/romilly/streamlit_spikes.git
   ```
   
3. Move into the directory containing the repository.
   ```shell
   cd cd streamlit_spikes/
   ```
2. Create a file called `.env` in the `src` directory of the project. It should contain a line for each key you need, in the following format:
    ```text
    MISTRAL_API_KEY=YOUR_MISTRAL_KEY
    OPENAI_API_KEY=YOUR_OPEN_AI_KEY
    ```
4. in the parent directory, create a virtual environment and activate it
   ```shell
   cd ..
   python -m venv venv
   source venv/bin/activate
   ```
   
5. Install the requirements using pip
   ```shell
   pip install -r requirements.txt
   ```
6. Run one of the applications
    ```shell
   cd src
   streamlit run mistral-api.py
   ```
A browser window should open containing the mistral app.
 Now you can enter a prompt in the entry field and send it to the mistral-tiny model. Wait a few seconds and the response will appear.






