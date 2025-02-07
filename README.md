# 📝 Speech-to-Text Note App

## 📌 Project Description  
The **Speech-to-Text Note App** is a Python-based notepad application that allows users to create, edit, and manage notes with an integrated speech-to-text feature. Users can dictate their notes, which are automatically converted into text. The app includes additional features such as note history management, text formatting, a search function, exporting notes to PDF, and a professional UI theme. The goal is to provide a seamless and efficient note-taking experience with voice input capabilities.

## ✨ Features  
- 🎤 **Speech-to-Text Conversion** – Users can dictate notes instead of typing.  
- 💾 **Save and Manage Notes** – Users can save, edit, and delete notes.  
- 📜 **Note History** – A list of saved notes that users can select and modify.  
- 🔄 **Update Existing Notes** – Edits overwrite the original note instead of creating a new entry.  
- 🔍 **Search Functionality** – Users can search for specific notes.  
- ✍ **Text Formatting** – Supports **bold**, *italic*, and _underline_ formatting.  
- 🎧 **Visual Listening Indicator** – A visual cue shows when the app is actively listening for speech input.  
- 📄 **Export to PDF** – Users can save notes as PDF files.  
- 🎨 **Professional UI Theme** – A modern and improved color scheme and layout for a better user experience.  

---

## 🛠 Tools Required  

### **1. Programming Language**  
- 🐍 **Python 3.x** – The core language for development.  

### **2. Development Environment & Libraries**  
- 🖥 **VS Code / PyCharm** – Recommended IDEs for coding.  
- 🏗 **venv (Virtual Environment)** – To manage dependencies and avoid conflicts.  
- 🎨 **tkinter** – Used for building the graphical user interface (GUI).  
- 🗣 **speech_recognition** – Converts spoken words to text.  
- 🎙 **pyaudio** – Captures audio input for speech recognition.  
- 📑 **pdfkit** – Converts notes to PDF format.  
- 🖨 **wkhtmltopdf** – Required by `pdfkit` for generating PDF files.  
- 🔊 **pyttsx3 (Optional)** – For text-to-speech functionality.  

### **3. External Dependencies & Setup**  
- **Install `wkhtmltopdf`** (for PDF export)  
  - **macOS:** `brew install wkhtmltopdf`  
  - **Linux:** `sudo apt-get install wkhtmltopdf`  
  - **Windows:** Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)  

---

## ⚙ Installation Steps  

1️⃣ **Set up a virtual environment** (recommended):  
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

2️⃣ Install required dependencies:

```bash
pip install tk speechrecognition pyaudio pdfkit pyttsx3
```

3️⃣ Ensure wkhtmltopdf is installed and configured correctly.

4️⃣ Run the application:
```bash
python main.py
```

📜 License
This project is open-source and available under the MIT License.

🚀 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

📬 Contact
For any questions or feedback, please reach out via email or open an issue on GitHub.
