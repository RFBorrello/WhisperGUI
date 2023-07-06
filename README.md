# WhisperGUI
A Graphical User Interface for transcribing audio files using OpenAI's Whisper Library.  It also allows the user to convert MP4 files into MP3 format as well.

# Prerequisites
To use the WhisperGUI, you need to have the following installed:
- A compatible version of Python - Whisper should be compatible with versions 3.9-3.11, the most recent stable version can be downloaded from here https://www.python.org/downloads/
- Whisper - this can be pip along with its dependencies from the command line (after Python is installed) using:
  

  **pip install git+https://github.com/openai/whisper.git**

  
- FFMPEG - the easiest to install this on Windows is using scoop/choco via the commandline.
  - For info on how to setup Scoop, please visit: https://scoop.sh/. However, you should be able to install it on Windows from Powershell using the following command:
  
    **irm get.scoop.sh | iex**
    
  - Once Scoop is setup, ffmpeg can be installed via the commandline using the following:
 
    **scoop install ffmpeg**
 
# Disclosures
WhisperGUI was made with help from ChatGPT.

This repository uses Whisper, which is licensed under the MIT License (Copyright (c) 2022 OpenAI). The original source code can be found at https://github.com/openai/whisper.
