#! Python3
# WhisperGUI.py written by Richard Borrello (with help from ChatGPT) last updated on July 6, 2023
# WhisperGUI is intended to help provide a graphical interface for OpenAI's Whisper speech-to-text library.
# It also offers users the ability to use convert MP4 files into MP3 files using FFMPEG (a prerequisite for Whisper)


import tkinter as tk
from tkinter import filedialog
import subprocess
import whisper
import threading

# Function to handle the MP4 to MP3 conversion
def convert_to_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if file_path:
        output_file = file_path.replace(".mp4", ".mp3")
        status_label.config(text="Converting...")
        disable_buttons()
        # Run the conversion in a separate thread
        threading.Thread(target=convert_thread, args=(file_path, output_file)).start()

# Function to run the MP4 to MP3 conversion in a separate thread
def convert_thread(file_path, output_file):
    subprocess.call(["ffmpeg", "-i", file_path, output_file])
    status_label.config(text="Conversion complete.")
    enable_buttons()

# Function to handle the MP3 transcription
def transcribe_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if output_file:
            status_label.config(text="Transcribing...")
            disable_buttons()
            # Run the transcription in a separate thread
            threading.Thread(target=transcribe_thread, args=(file_path, output_file)).start()

# Function to run the MP3 transcription in a separate thread
def transcribe_thread(file_path, output_file):
    model = whisper.load_model("tiny.en")
    result = model.transcribe(file_path)
    with open(output_file, "w") as f:
        f.write(result["text"])
    status_label.config(text="Transcription complete.")
    enable_buttons()

# Function to disable the buttons during conversion/transcription
def disable_buttons():
    convert_button.config(state=tk.DISABLED)
    transcribe_button.config(state=tk.DISABLED)

# Function to enable the buttons after conversion/transcription
def enable_buttons():
    convert_button.config(state=tk.NORMAL)
    transcribe_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title("Media Converter")

# Create a label for program description and instructions
description_label = tk.Label(
    window,
    text="Media Converter\n\nThis program allows you to convert MP4 files to MP3 format and transcribe MP3 files to text using OpenAI's Whisper library.\n\nInstructions:\n1. Click 'Convert MP4 to MP3' to convert an MP4 file.\n2. Click 'Transcribe MP3' to transcribe an MP3 file.\n3. Select the file and follow the prompts.\n4. The status will be displayed below.",
    justify=tk.LEFT,
    padx=10,
    pady=10
)
description_label.pack()

# Create the buttons for conversion and transcription
convert_button = tk.Button(window, text="Convert MP4 to MP3", command=convert_to_mp3)
convert_button.pack()

transcribe_button = tk.Button(window, text="Transcribe MP3", command=transcribe_mp3)
transcribe_button.pack()

# Create the status label
status_label = tk.Label(window, text="Ready")
status_label.pack()

# Run the GUI main loop
window.mainloop()
