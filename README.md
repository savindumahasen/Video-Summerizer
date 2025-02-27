# Video-Summerizer
This is an end to end video summerizer Agentic AI project with phidata, 'google gemini-2.0-flash-exp' LLM model, and streamlit. By using this application, users can analyze and get the video summary to identify whether this videos are relevent to their task or not without watching the full videos and wasting their time. And also this agent comprises of duck duck go search tool. Consequently, users can find  relevent content  to their uploaded video in web.

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required Python dependencies:

    ```terminal
    pip install -r requirements.txt
    ```

3. Create a `.env` file and include the necessary environment variables:

    ```text
    GOOGLE_API_KEY = "your gemini token"
    ```
    Replace `your gemini token` with your actual API keys.

4. Run the script to start the agent:

    ```terminal
    streamlit run app.py
    ```
