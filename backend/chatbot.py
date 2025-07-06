# backend/chatbot.py

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langdetect import detect
from chromadb import PersistentClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_video_response(video_id: str, query: str) -> str:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=['en', 'hi'])
        raw_text = " ".join(chunk['text'] for chunk in transcript_list)
    except TranscriptsDisabled:
        return "Transcript not available for this video."
    except Exception as e:
        return f"Error getting transcript: {str(e)}"

    if not raw_text:
        return "Transcript is empty."

    lang = detect(raw_text)
    if lang != "en":
        model = GoogleGenerativeAI(model='gemini-2.0-flash')
        translation_prompt = f"Translate this to English:\n{raw_text}"
        translated = model.invoke(translation_prompt)
        transcript_text = str(translated).strip()
    else:
        transcript_text = raw_text

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript_text])

    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

    try:
        client = PersistentClient(path="chroma_db2")
        client.delete_collection("transcript")
    except Exception:
        pass

    vector_store = Chroma(
        collection_name='transcript',
        embedding_function=GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
        persist_directory='chroma_db2'
    )
    vector_store.add_documents(chunks)

    retriever = RunnableLambda(lambda x: vector_store.similarity_search(x, k=5))

    def get_doc(retrieved_doc):
        return "\n\n".join(doc.page_content for doc in retrieved_doc)

    prompt = PromptTemplate(
        template="""You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the context is not sufficient, just say "I don't know".
{context}
Question: {query}""",
        input_variables=["context", "query"]
    )

    chain = (
        RunnableParallel({
            "context": retriever | RunnableLambda(get_doc),
            "query": RunnablePassthrough()
        }) | prompt | GoogleGenerativeAI(model='gemini-2.0-flash') | StrOutputParser()
    )

    try:
        return chain.invoke(query)
    except Exception as e:
        return f"Error during chain invocation: {str(e)}"
