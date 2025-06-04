import os
from datetime import datetime, timedelta
import streamlit as st
import numpy as np
import io
import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_openai import ChatOpenAI
from langchain_google_community import GoogleSearchAPIWrapper
from langchain.prompts import PromptTemplate

# --- Sayfa Konfig (ilk komut olmalı) ---
st.set_page_config(page_title="Leadership Coach Chatbot", layout="wide")

# --- Koyu Tema Stil ---
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(145deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    textarea, input, .stTextInput>div>div>input {
        background-color: #1f1f1f !important;
        color: white !important;
        border-radius: 8px;
    }
    .stButton button {
        background-color: #4c8bf5 !important;
        color: white !important;
        border: none !important;
        padding: 0.4rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #376fc2 !important;
    }
    div[data-testid="stMarkdownContainer"] > div {
        background: rgba(255,255,255,0.05);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    div[data-testid="stMarkdownContainer"] > div:hover {
        border-color: #4c8bf5;
        box-shadow: 0 0 12px #4c8bf555;
    }
    .custom-card {
        background-color: #2c2f38;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        text-align: center;
        font-weight: 600;
        color: white;
        box-shadow: 0 0 5px rgba(255,255,255,0.05);
    }
    .sidebar-bottom {
        text-align: center;
        font-weight: 500;
        color: white;
        background-color: #2c2f38;
        padding: 10px;
        border-radius: 12px;
        margin-top: 2rem;
    }
    .stTextArea textarea {
        height: 100px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Ortam Ayarları ---
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# --- Embedding Model ve Veri Yükleme (Cache ile) ---
@st.cache_resource
def load_embedder():
    return SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

@st.cache_resource
def load_chunks_and_embeddings():
    with open("turkish_chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)
    embedder = load_embedder()
    if "embedding" in chunks[0]:
        embeddings = np.array([c["embedding"] for c in chunks])
    else:
        texts = [c["chunk"] for c in chunks]
        embeddings = embedder.encode(texts)
    return chunks, embeddings

# --- Memory tabanlı context retrieval ---
def get_memory_context(question):
    chunks, embeddings = load_chunks_and_embeddings()
    embedder = load_embedder()
    q_emb = embedder.encode([question])
    sims = cosine_similarity(q_emb, embeddings)[0]
    best_idx = np.argsort(sims)[::-1][:3]
    docs = [chunks[i] for i in best_idx]
    context = "\n".join([doc["chunk"] for doc in docs])
    return context, docs

# --- Relevancy ve cevabı GPT-4 ile üret ---
def ask_if_relevant_enough(question, context):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = PromptTemplate(
        template=(
            "Konu: Liderlik Koçluğu\n"
            "Soru: {question}\n"
            "Bilgi: {context}\n\n"
            "Konu liderlik veya Liderlik koçluğu değilse veya bilgiyle en azından makul bir bağ kurulamıyorsa sadece 'HAYIR' yaz.\n"
            "Eğer liderlik koçluğu ile ilgiliyse veya bilgi soruya biraz bile bir şekilde yardımcı oluyorsa sadece 'EVET' yaz.\n"
            "Başka hiçbir şey yazma."
        ),
        input_variables=["question", "context"]
    )
    result = (prompt | llm).invoke({"question": question, "context": context})
    return result.content.strip().lower() == "evet"

def generate_answer(question, context):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = PromptTemplate(
        template="Soru: {question}\nVerilen bilgi: {context}\nCevabı Türkçe ve profesyonel şekilde ver.",
        input_variables=["question", "context"]
    )
    result = (prompt | llm).invoke({"question": question, "context": context})
    return result.content

def do_google_fallback(question):
    search = GoogleSearchAPIWrapper(k=3)
    current_year = datetime.now().year
    search_query = f"{question} after:{current_year - 1}"
    web_results = search.results(search_query, num_results=3)

    links = [r["link"] for r in web_results if "link" in r]
    web_results_text = "\n".join([f"{r['title']}: {r['snippet']}" for r in web_results])

    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = PromptTemplate(
        template="Soru: {question}\nWeb Sonuçları:\n{web_results}\n"
                 "Cevabı Türkçe ve profesyonel bir şekilde ver. Son web aramaları günceldir ve yıl {current_year}, buna dikkat et.",
        input_variables=["question", "web_results", "current_year"]
    )
    result = (prompt | llm).invoke({
        "question": question,
        "web_results": web_results_text,
        "current_year": current_year
    })
    return result.content, links

# --- Pipeline ---
def answer_pipeline(question):
    context, docs = get_memory_context(question)

    if len(context.strip()) < 100:
        st.warning("Konu hakkında yeterince bilgim yok. Google'dan sizin için bunları buldum.")
        return do_google_fallback(question) + ("Google",)

    if not ask_if_relevant_enough(question, context):
        st.warning("Konu hakkında yeterince bilgim yok. Google'dan sizin için bunları buldum.")
        return do_google_fallback(question) + ("Google",)

    answer = generate_answer(question, context)
    unique_titles = list(set(doc.get("video_title", "Bilinmeyen kaynak") for doc in docs))
    return answer, unique_titles, "Chunks"

# --- Uygulama Arayüzü ---
st.title("👨‍💼 Leadership Coach Chatbot")
st.caption("Sorularınızı girin, AI destekli koçluk cevabınızı alın.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form("soru_form"):
    user_question = st.text_area("", placeholder="İyi bir liderin özellikleri nelerdir?", label_visibility="collapsed")
    submitted = st.form_submit_button("Cevapla")

if submitted and user_question.strip():
    with st.spinner("Yanıt hazırlanıyor..."):
        answer, sources, source_type = answer_pipeline(user_question)

    st.session_state.chat_history.append((user_question, answer))

    st.markdown("### 💬 Cevap")
    st.markdown(f"<div style='padding:1rem;border-radius:12px;background:#1f1f1f'>{answer}</div>", unsafe_allow_html=True)

    st.markdown("### 📄 Kaynaklar")
    if source_type == "Chunks":
        for i, s in enumerate(sources, 1):
            st.markdown(f"{i}. {s}")
    else:
        for i, link in enumerate(sources, 1):
            st.markdown(f"{i}. [Link]({link})")

# --- Sidebar: Saat Kartı ---
turkiye_saati = datetime.utcnow() + timedelta(hours=3)
st.sidebar.markdown(
    f"""
    <div class="custom-card">
        🕒 <strong>Saat (GMT+3):</strong> {turkiye_saati.strftime('%H:%M:%S')}
    </div>
    """,
    unsafe_allow_html=True
)

# --- Sidebar: Geçmiş ---
with st.sidebar.expander("🕘 Geçmiş", expanded=True):
    for q, a in reversed(st.session_state.chat_history):
        st.markdown(f"**Soru:** {q}")
        st.markdown(f"<div style='background:#1a1a1a;padding:0.5rem;border-radius:8px'>{a}</div>", unsafe_allow_html=True)
        st.markdown("---")

    if st.session_state.chat_history:
        export_text = "\n\n".join(f"Soru: {q}\nCevap: {a}" for q, a in st.session_state.chat_history)
        buffer = io.StringIO(export_text)

        col1, col2 = st.columns(2)
        with col1:
            st.download_button("⬇️ Geçmişi İndir", data=buffer.getvalue(), file_name="chat_gecmisi.txt")
        with col2:
            if st.button("🗑️ Geçmişi  Temizle"):
                st.session_state.chat_history = []

# --- Footer ---
st.sidebar.markdown("""
    <div class="sidebar-bottom">
        Mert KAYA - 2025
    </div>
""", unsafe_allow_html=True)
