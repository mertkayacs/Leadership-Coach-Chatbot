<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/svg/leadership-coach-logo-on-dark.svg">
    <img src="docs/brand/svg/leadership-coach-logo-on-light.svg" alt="Leadership Coach" width="320">
  </picture>
</p>

<h1 align="center">Ask a leadership question in Turkish. Get an answer with its sources.</h1>

<p align="center">
  A Turkish-language leadership coach chatbot built with Streamlit.<br>
  <b>281 transcript chunks from 27 interviews. GPT-4o answers. Google as fallback.</b>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white">
  <img alt="281 transcript chunks" src="https://img.shields.io/badge/chunks-281-2F6B4F?style=flat-square">
  <img alt="Side project, 2025" src="https://img.shields.io/badge/project-side%20project%202025-6D597A?style=flat-square">
  <a href="https://github.com/mertkayacs/Leadership-Coach-Chatbot"><img alt="GitHub stars" src="https://img.shields.io/github/stars/mertkayacs/Leadership-Coach-Chatbot?style=flat-square&logo=github&color=8A6D3B"></a>
</p>

<p align="center">
  <a href="#quick-start"><img alt="Quick start" src="https://img.shields.io/badge/Quick%20start-6D597A?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNMTIgMTV2NXMzLjAzLS41NSA0LTJjMS4wOC0xLjYyIDAtNSAwLTUiLz48cGF0aCBkPSJNNC41IDE2LjVjLTEuNSAxLjI2LTIgNS0yIDVzMy43NC0uNSA1LTJjLjcxLS44NC43LTIuMTMtLjA5LTIuOTFhMi4xOCAyLjE4IDAgMCAwLTIuOTEtLjA5Ii8%2BPHBhdGggZD0iTTkgMTJhMjIgMjIgMCAwIDEgMi0zLjk1QTEyLjg4IDEyLjg4IDAgMCAxIDIyIDJjMCAyLjcyLS43OCA3LjUtNiAxMWEyMi40IDIyLjQgMCAwIDEtNCAyeiIvPjxwYXRoIGQ9Ik05IDEySDRzLjU1LTMuMDMgMi00YzEuNjItMS4wOCA1IC4wNSA1IC4wNSIvPjwvZz48L3N2Zz4%3D&logoColor=white"></a>
  <a href="turkish_chunks.json"><img alt="Data" src="https://img.shields.io/badge/Data-1E2A38?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48ZWxsaXBzZSBjeD0iMTIiIGN5PSI1IiByeD0iOSIgcnk9IjMiLz48cGF0aCBkPSJNMyA1VjE5QTkgMyAwIDAgMCAyMSAxOVY1Ii8%2BPHBhdGggZD0iTTMgMTJBOSAzIDAgMCAwIDIxIDEyIi8%2BPC9nPjwvc3ZnPg%3D%3D&logoColor=white"></a>
  <a href="steamlit_leadership_chatbot.py"><img alt="App" src="https://img.shields.io/badge/App-1E2A38?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48ZyBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBkPSJNNiAyMmEyIDIgMCAwIDEtMi0yVjRhMiAyIDAgMCAxIDItMmg4YTIuNCAyLjQgMCAwIDEgMS43MDQuNzA2bDMuNTg4IDMuNTg4QTIuNCAyLjQgMCAwIDEgMjAgOHYxMmEyIDIgMCAwIDEtMiAyeiIvPjxwYXRoIGQ9Ik0xNCAydjVhMSAxIDAgMCAwIDEgMWg1Ii8%2BPHBhdGggZD0iTTEwIDEyLjUgOCAxNWwyIDIuNSIvPjxwYXRoIGQ9Im0xNCAxMi41IDIgMi41LTIgMi41Ii8%2BPC9nPjwvc3ZnPg%3D%3D&logoColor=white"></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/hero-dark.webp">
    <img src="docs/assets/readme/hero-light.webp" alt="Leadership Coach Chatbot answer in Turkish with a sources list naming three interview videos, in a dark teal Streamlit interface" width="960">
  </picture>
</p>

Leadership Coach is a Streamlit chatbot that answers leadership questions in Turkish. It searches 281 transcript chunks from 27 interview videos that ship in the repository, using a local multilingual embedding model and cosine similarity. GPT-4o checks whether the best matches fit the question and writes the answer with its sources. When the local content does not fit, the app falls back to a Google search.

---

## Why Leadership Coach

The app keeps retrieval small and shows where each answer comes from.

|  |  |
|---|---|
| <img src="docs/assets/readme/icons/book-text.svg" width="18" height="18" alt=""> **Answers with sources** | Each answer lists the interview titles it was built from, as the screenshot above shows under "Kaynaklar". |
| <img src="docs/assets/readme/icons/database.svg" width="18" height="18" alt=""> **No vector database** | Chunks are embedded at start-up with sentence-transformers (paraphrase-multilingual-MiniLM-L12-v2), and the top three matches by cosine similarity go to the model. |
| <img src="docs/assets/readme/icons/search.svg" width="18" height="18" alt=""> **Google fallback** | When the relevance check says the local chunks do not cover the question, the app queries the Google Programmable Search API for three results. |
| <img src="docs/assets/readme/icons/file-json.svg" width="18" height="18" alt=""> **Data you can rebuild** | The chunks file holds video title, text and source URL. Scripts for yt-dlp, Whisper transcription and chunking rebuild it from a YouTube playlist. |

## Features

**Chat**

- Turkish question box and answer view.
- Source list under every answer.
- Session history with a download button and a clear button.

**Retrieval**

- Local embeddings with scikit-learn cosine similarity, no server.
- GPT-4o relevance check, then answer generation.
- Google search fallback through LangChain.

**Data pipeline**

- audio_downloader.py, transcript_maker_whisper.py and prepare_transcripts.py build the chunks.
- The Weaviate upload scripts remain in the repository and are not used by the app.

## Quick start

```sh
git clone https://github.com/mertkayacs/Leadership-Coach-Chatbot.git
cd Leadership-Coach-Chatbot
pip install -r requirements.txt
streamlit run steamlit_leadership_chatbot.py
```

Set `OPENAI_API_KEY` for GPT-4o, plus `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` (a Programmable Search Engine ID) for the Google fallback. On first load the app encodes the chunks with the local model.

### Requirements

- Python 3.11 (the version the dev container pins).
- An OpenAI API key and Google search credentials.
- A dev container configuration for Codespaces is in .devcontainer.

## FAQ

<details>
<summary><b>Which language does it speak?</b></summary>

Questions, answers and the interface are in Turkish.
</details>

<details>
<summary><b>Where do the answers come from?</b></summary>

From the 281 chunks of 27 interview videos in the repository. When none of them fits, the app searches Google and says so.
</details>

<details>
<summary><b>Do I need a database?</b></summary>

No database is needed. Embeddings are computed at start-up with a local model.
</details>

<details>
<summary><b>What are the Weaviate scripts for?</b></summary>

They are left from an earlier version. The [LeadershipGuide](https://github.com/mertkayacs/Weaviate-Based-LeadershipGuide-Chatbot) repository is the Weaviate variant.
</details>

If Leadership Coach is useful to you, a ⭐ helps other people find it.

Photos behind the screenshots are credited in [docs/assets/readme/CREDITS.md](docs/assets/readme/CREDITS.md).

[![views](https://hits.sh/github.com/mertkayacs/Leadership-Coach-Chatbot.svg?view=today-total&style=flat-square&label=views&color=6D597A&labelColor=1E2A38)](https://github.com/mertkayacs/Leadership-Coach-Chatbot)
