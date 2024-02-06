# Jarvis Virtual Assistant

## Overview

Jarvis Virtual Assistant is a Python script designed to serve as a personalized virtual assistant, integrating various functionalities for a seamless user experience. The code incorporates voice recognition, web browsing, Wikipedia searches, email sending, file exploration, and OpenAI GPT-3.5 integration. This comprehensive virtual assistant aims to enhance productivity and streamline user interactions through voice commands.

## Features

### 1. Voice Interaction

Utilizing the **speech_recognition** library and **pyttsx3** for speech synthesis, Jarvis enables hands-free control and engagement.

### 2. Web Browsing

Open specific websites, such as YouTube, Google, Drive, and WhatsApp, using the **webbrowser** module. Easily expand the list to include more websites.

### 3. Wikipedia Search

Retrieve information from Wikipedia by voice commands, providing concise summaries based on user queries.

### 4. Email Sending

Send emails effortlessly with the **smtplib** library. Users can dictate the content, and Jarvis takes care of the email delivery.

### 5. File Search

Efficiently search for files within specified root directories. The script prompts users for the file name and provides the path if found.

### 6. Time Display

Ask Jarvis for the current time, and it responds with the current time in a user-friendly format.

### 7. Code Editor Opening

Open a specified code editor with ease. Users can customize the **codePath** variable to match their preferred code editor.

### 8. GPT Integration

Interact with the OpenAI GPT-3.5 model for generating intelligent responses. While the code for calling GPT is provided, users need to uncomment and supply the OpenAI API key for this feature.

## Usage

1. Install required dependencies: `pip install pyttsx3 wikipedia webbrowser SpeechRecognition pywhatkit openai dotenv`
2. Set up environment variables in a **.env** file for email and OpenAI credentials.
3. Run the script: `python jarvis.py`

## Contribution

Contributions to enhance features, improve error handling, and optimize the codebase are welcome. Please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
