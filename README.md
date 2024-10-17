# AudioSyncAI

**AudioSyncAI** is a web application designed to seamlessly replace audio tracks in video files using advanced AI technologies. With this tool, users can extract audio from videos, transcribe it, correct inaccuracies, and generate a new audio track using text-to-speech capabilities.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Audio Extraction:** Extract audio from various video formats (MP4, MOV, AVI) with ease.
- **AI-Powered Transcription:** Utilize AssemblyAI for accurate transcription of audio content.
- **Transcription Correction:** Improve transcriptions using Azure OpenAI, enhancing clarity by removing filler words and correcting mistakes.
- **Text-to-Speech Conversion:** Convert corrected text into high-quality audio using Google Text-to-Speech (gTTS).
- **Seamless Integration:** Replace the original audio in the video with the newly generated audio track, ensuring synchronization between video and audio.

## Technologies Used

- **Streamlit:** For creating the web application interface.
- **MoviePy:** For video and audio processing.
- **AssemblyAI:** For transcribing audio files.
- **Azure OpenAI:** For correcting transcription and enhancing clarity.
- **gTTS (Google Text-to-Speech):** For converting text to speech.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `streamlit`
  - `moviepy`
  - `assemblyai`
  - `requests`
  - `gtts`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AudioSyncAI.git
   cd AudioSyncAI
