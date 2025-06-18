# 🧠 Leadership Coach Chatbot

A Turkish-language leadership coach chatbot that blends **GPT-4**, **local embeddings**, **Weaviate**, and **Google Search API** into a Streamlit-based interface. Designed to assist users with leadership principles, self-growth, and strategic coaching conversations.


---

## 🚀 Features

- ✅ GPT-4 responses with fallback to Google Search when context is insufficient
- ✅ Local JSON chunks with HuggingFace embeddings
- ✅ Weaviate vector database integration
- ✅ Google Search API for supplementing weak responses
- ✅ Streamlit frontend with dark mode UI
- ✅ File-based document chunking and upload
- ✅ Whisper-based transcript preprocessing
- ✅ Turkish language support 🇹🇷

---

## 📁 Project Structure

```bash
.
├── .streamlit/                  # Streamlit theme and settings
├── .devcontainer/               # Optional devcontainer support
├── screenshots/                 # UI screenshots
├── audio_downloader.py          # Audio utility for preprocessing
├── jsontocsv.py                 # Convert transcripts to CSV
├── prepare_transcripts.py       # Format for embedding
├── transcript_maker_whisper.py  # Whisper transcription
├── upload_to_weaviate.py        # Upload local JSON chunks
├── upoad_weaviate_cloud.py      # Upload to Weaviate Cloud
├── turkish_chunks.json          # Turkish content chunks
├── requirements.txt             # Python dependencies
├── README.md                    # You're here
└── steamlit_leadership_chatbot.py # Main Streamlit app
