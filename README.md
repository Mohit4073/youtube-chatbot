# 🎥 YouTube Chatbot with LangChain & Gemini AI

This project is an AI-powered chatbot that answers questions about any YouTube video using its transcript. It utilizes:
- 🧠 Google Gemini (Generative AI)
- 🧾 YouTube Transcript API
- 🔍 LangChain for vector search
- 🗃️ ChromaDB for persistent storage
- 🌐 FastAPI for the backend server

---

## 🚀 Features

- 🔎 Automatically fetches transcript of a given YouTube video
- 🌐 Translates non-English transcripts to English (if needed)
- 🧱 Splits and embeds the transcript using GoogleEmbeddings
- 🧠 Uses Gemini AI to answer questions based on transcript context
- 💾 Stores vector data with Chroma for retrieval
- 🧑‍💻 Simple front-end UI for interaction (ask questions!)
- 🌍 Full-stack: Backend with FastAPI and Frontend with HTML/JS

---

## 🧰 Tech Stack

| Layer         | Technology              |
|--------------|--------------------------|
| Backend       | Python, FastAPI         |
| LLM & Embeddings | Google Gemini + LangChain |
| Transcript    | YouTube Transcript API |
| Vector DB     | Chroma (Persistent)     |
| Frontend      | HTML, JavaScript        |

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Mohit4073/youtube-chatbot.git
cd youtube-chatbot
```

## 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # on Linux/Mac
venv\Scripts\activate       # on Windows
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Set Environment Variables

Create a `.env` file in the root of the project directory and add your Gemini API key:

```ini
GOOGLE_API_KEY=your_google_api_key_here
```

## 5️⃣ Run the Server

Start your FastAPI backend server:

```bash
cd backend
uvicorn main:app --reload
```

## 💬 How It Works

1. User enters a **YouTube video ID** and a **question** in the chatbot UI.
2. The **backend fetches the transcript** using `youtube_transcript_api`.
3. If the transcript is in a non-English language, it uses **Gemini** to translate it to English.
4. The transcript is **split into chunks** using LangChain's `RecursiveCharacterTextSplitter`.
5. These chunks are **embedded using Gemini embeddings**.
6. Embeddings are stored in **ChromaDB** for efficient similarity search.
7. The user's query is **matched against similar chunks** from the transcript.
8. **Gemini** is prompted with the most relevant transcript chunks and **returns an answer**.

---

## 🧪 Example Query

- **Video ID:** `k8Y6SQYfQ4s`  
- **Question:** "Is there discussion about Ajay Devgan in the video?"  
- **Answer:** "Yes, Ajay Devgan was mentioned in the context of..."

## 📂 Project Structure

youtube-chatbot/
├── backend/
│   ├── main.py            # FastAPI entry point
│   ├── chatbot.py         # LangChain logic & Gemini chain
│
├── frontend/
│   ├── index.html         # Chat UI
│   ├── script.js          # Frontend logic
│
├── chroma_db2/            # Chroma persistent storage
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
└── README.md              # Project documentation

