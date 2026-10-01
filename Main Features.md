Main Features
Save Meeting

Store:

Client name
Meeting date
Participants
Meeting notes
AI Memory & Recall

Hindsight stores and retrieves relevant information from previous meetings for a specific client.

AI Meeting Preparation

The AI combines current meeting information with recalled historical information to generate a structured preparation brief.

Meeting Brief

The generated brief includes:

Client Overview
Previous Interests
Key Concerns
Important Stakeholders
Competitors
Talking Points
Questions to Ask
Suggested Next Steps
Client Memory Isolation

Information is recalled in the context of the selected client, helping prevent information from unrelated clients from appearing in a meeting brief.

Technology Stack
Frontend
Next.js
React
TypeScript
Tailwind CSS
Backend
Python
FastAPI
Uvicorn
AI & Memory
Hindsight — persistent memory
Groq — LLM inference
Deployment
Frontend: Vercel
Backend: Render
Source Control: GitHub
Project Structure
MemoryMeet-AI/
├── backend/
│   ├── agent/
│   ├── models/
│   ├── services/
│   ├── main.py
│   ├── requirements.txt
│   └── .gitignore
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── package.json
│   └── ...
│
└── README.md
Running Locally
Backend
cd backend
python -m venv venv

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a .env file:

HINDSIGHT_API_KEY=your_hindsight_api_key
HINDSIGHT_API_URL=your_hindsight_api_url
HINDSIGHT_BANK_ID=your_hindsight_bank_id
GROQ_API_KEY=your_groq_api_key

Start the backend:

python -m uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs
Frontend

Open another terminal:

cd frontend
npm install

Create .env.local:

NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000

Start:

npm run dev

Open:

http://localhost:3000
API Endpoints
Method	Endpoint	Purpose
GET	/health	Check backend health
GET	/meetings	Get saved meetings
POST	/meetings	Save a meeting
POST	/meetings/recall	Recall client memories
POST	/meetings/prepare	Generate an AI meeting brief
Example Workflow
Enter a client name.
Add meeting participants.
Enter the current meeting notes/context.
Click Save Meeting.
Click Prepare Me.
MemoryMeet AI recalls relevant historical context.
The AI generates a personalized meeting brief.
Example Use Case

A client has discussed cloud migration over several meetings.

MemoryMeet AI can recall:

Security requirements
Migration timeline
Pricing concerns
Competitor comparisons
Important stakeholders
Minimal-downtime requirements

Before the next meeting, the team receives this context in one structured brief instead of manually searching through old notes.

Security

API keys and environment variables are kept outside the Git repository.

Do not commit:

.env
.env.local
venv/
node_modules/
.next/
Team

MemoryMeet AI was developed collaboratively with responsibilities across:

AI Agent & LLM integration
Hindsight memory
Python backend
Frontend
Data & testing
Integration & documentation
Project Status

Core workflow:

Save Meeting
    ↓
Hindsight Retain
    ↓
Hindsight Recall
    ↓
AI Agent
    ↓
Meeting Brief

The application is designed as a preparation and memory layer alongside existing meeting workflows such as Zoom or Google Meet rather than replacing the video-conferencing platform.

MemoryMeet AI — Remember what matters. Prepare for what’s next.


### After saving

Run:

```cmd
git status

Paste the output here.