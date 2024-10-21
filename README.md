# 🗣️ Voice Assistant with Groq API

This project is a Python-based voice assistant that integrates **speech recognition**, **text-to-speech (TTS)**, and the **Groq API** for generating conversational responses. The assistant listens to your voice commands, processes them, and speaks the response back to you. It also includes the ability to shut down based on voice input.

## ✨ Features

- **Speech Recognition**: Converts spoken language into text using Google's Speech Recognition API.
- **Text-to-Speech**: Converts text responses into natural-sounding speech using the `pyttsx3` module.
- **Groq API Integration**: Generates conversational responses using Groq's AI models.
- **Custom Commands**: Ability to shut down the assistant via voice command (`"shut down"`).
  
## 📚 Technologies Used

- **Python 3.9+**
- **[Groq API](https://groq.com)**: For AI-driven conversational responses.
- **[speech_recognition](https://pypi.org/project/SpeechRecognition/)**: For recognizing and converting voice commands to text.
- **[pyttsx3](https://pypi.org/project/pyttsx3/)**: A cross-platform text-to-speech library.
  
## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher.
- Pip (Python package manager).
- An internet connection for interacting with Google's Speech Recognition service and the Groq API.

### Installation

1. Clone the repository or download the project files.
   
   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
