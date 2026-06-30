# 🎙️ AI Meeting Summarizer

An AI-powered Meeting Summarizer that converts meeting recordings into text and automatically generates concise summaries and key discussion points using Large Language Models (LLMs).

---

## 📌 Overview

Meetings often contain lengthy discussions, making it difficult to remember important decisions and action items.

This project solves that problem by automatically:

- 🎤 Converting speech into text using OpenAI Whisper
- 📝 Generating a concise meeting summary
- 📋 Extracting key discussion points using Llama 3.3 via the Groq API
- 🌐 Providing an easy-to-use web interface with Gradio

---

## 🚀 Features

- Upload meeting recordings
- Automatic Speech-to-Text transcription
- AI-generated meeting summary
- Key point extraction
- User-friendly Gradio interface
- Secure API key management using `.env`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenAI Whisper | Speech-to-Text |
| Groq API | Fast LLM Inference |
| Llama 3.3 | Text Summarization |
| Gradio | Web Interface |
| python-dotenv | Environment Variables |
| FFmpeg | Audio Processing |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
Meeting-Summarizer-AI/
│
├── app.py                 # Gradio user interface
├── transcriber.py         # Speech-to-Text using Whisper
├── summarizer.py          # Summary generation using Llama
├── requirements.txt
├── README.md
├── .gitignore
├── .env                   # API key (not uploaded)
│
├── audio/
│   └── sample.mp3
│
├── outputs/
│   ├── transcript.txt
│   └── summary.txt
│
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/VanshikaMalhotra-22/Meeting-Summarizer-AI-project.git
```

### 2. Navigate to the project

```bash
cd Meeting-Summarizer-AI-project
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install FFmpeg

Download and install FFmpeg, then ensure it is added to your system PATH.

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:7860
```

---

## 🧠 How It Works

```
Meeting Audio
      │
      ▼
OpenAI Whisper
(Speech → Text)
      │
      ▼
Transcript
      │
      ▼
Groq API
      │
      ▼
Llama 3.3
(Summary + Key Points)
      │
      ▼
Gradio Interface
      │
      ▼
Display Results
```

---

## 📷 Screenshots

### Home Screen

![Home](C:\C++ Programs\AI ML\Meeting-Summarizer-AI\screenshots\homepage.png)

### Transcript

![Transcript](screenshotsC:\C++ Programs\AI ML\Meeting-Summarizer-AI\screenshots\transcript.png)

### Meeting Summary

![Summary](C:\C++ Programs\AI ML\Meeting-Summarizer-AI\screenshots\summary.png)
![KeyPoints](C:\C++ Programs\AI ML\Meeting-Summarizer-AI\screenshots\keypoints.png)

## 🔮 Future Improvements

- Speaker identification
- Action item extraction
- Support for multiple languages
- PDF meeting report generation
- Cloud deployment
- Docker support

---

## 👩‍💻 Author

**Vanshika Malhotra**

GitHub: https://github.com/VanshikaMalhotra-22

---

## ⭐ If you found this project helpful, consider giving it a star!
