import os
import speech_recognition as sr
import pyttsx3
from groq import Groq

# Initialize the Groq API client
client = Groq(
    api_key="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",  # Use your API key securely
)

# Initialize the speech recognition engine
r = sr.Recognizer()

# Text-to-speech engine initialization
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  # Set the voice to female or any preferred voice

    engine.say(text)
    engine.runAndWait()

# Voice recognition and listening
def listen():
    with sr.Microphone() as source:
        print("💡 Listening... 💡")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("📢 Recognizing... 📢")
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Error❌")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Interact with the Groq API to generate responses
def get_groq_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,  # Pass the user's speech input
                }
            ],
            model="llama3-8b-8192",  # You can choose a different model based on your requirements
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        print(f"Error in Groq API: {e}")
        return "I'm sorry, I couldn't process your request."

# Main loop for the virtual assistant
def main():
    speak("Initializing One")
    while True:
        command = listen()  # Listen to voice input

        if "shut down" in command:  # Example shutdown command
            speak("🟢 Shutting down 🟢")
            quit()

        elif command != "":  # If there is a valid command, query Groq API
            groq_response = get_groq_response(command)
            print(f"Groq API Response: {groq_response}")
            speak(groq_response)  # Convert Groq's response to speech

        else:
            speak("🛑 Please input a valid command 🛑")

if __name__ == "__main__":
    main()
