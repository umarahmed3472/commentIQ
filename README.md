CommentIQ is a lightweight web app that summarizes user comments using AI. Users click a Summarize button, the comments are sent to a local Python backend, and an AI-generated summary is returned and displayed in the UI. Built for a hackathon — simple, fast, and local-only.

Tech Stack:
Frontend: HTML, CSS, JavaScript  
Backend: Python (Flask)  
AI: OpenAI API  

## Setup Instructions

1. Clone the repo
git clone https://github.com/umarahmed3472/commentIQ.git
cd commentIQ

2. Create a .env file
Create a file named .env in the project root and add:
OPENAI_API_KEY=your_openai_api_key_here

Important: .env is intentionally git-ignored. Do not commit it.

3. Install Python dependencies
Make sure you have Python 3.9+ installed.
pip install flask openai python-dotenv

4. Run the backend server
python app.py
The server will start on http://127.0.0.1:5000

5. Open the frontend
Open index.html in your browser (double-click or run `open index.html`)

## How It Works
1. User enters comments in the comment section
2. User clicks Summarize
3. Frontend sends comments to the Python backend
4. Backend builds a prompt and sends it to the OpenAI API
5. The summary is returned and displayed in a popup/modal

## Project Structure
commentIQ/

├── index.html

├── script.js

├── app.py

├── .gitignore

├── .env (local only, not committed)

└── README.md


## Future Improvements
- Add likes to comments and have AI summarize consider that data as well
- Consider replies to comment section threads

## License
MIT
