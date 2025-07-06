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
