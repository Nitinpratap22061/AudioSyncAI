import streamlit as st
from moviepy.editor import VideoFileClip, AudioFileClip
import tempfile
import assemblyai as aai
import requests
import json
from gtts import gTTS
import os


aai.settings.api_key = "8289507116a9488ea30f54a45e6b3172"  

# Set up Azure OpenAI API credentials
azure_api_key = "22ec84421ec24230a3638d1b51e3a7dc"  
endpoint_url = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

st.title("Audio Replacement in Video using AI")

video_file = st.file_uploader("Upload your video file", type=["mp4", "mov", "avi"])

if video_file is not None:
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        temp_video_path = temp_video.name

    # Load the video file using VideoFileClip
    video_clip = VideoFileClip(temp_video_path)

    # Check if the video has an audio track
    if video_clip.audio is not None:
        # Define the audio file path
        audio_file = "extracted_audio.wav"
        
        # Extract and save the audio
        video_clip.audio.write_audiofile(audio_file)

        # Inform the user
        st.success("Audio extracted and saved as extracted_audio.wav")

        # Optionally, you can also display the audio player
        st.audio(audio_file, format='audio/wav')

        # Transcribe the extracted audio
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_file)

        # Display the transcribed text
        st.success("Transcription complete!")
        st.write(transcript.text)  # Display the transcribed text

        # Correct the transcription using Azure OpenAI
        prompt = f"Correct this transcription and remove filler words: '{transcript.text}'"

        headers = {
            "Content-Type": "application/json",
            "api-key": azure_api_key
        }

        # Prepare the data for the API request
        data = {
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }

        # Make the API request
        response = requests.post(endpoint_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            # Process the response
            response_data = response.json()
            corrected_text = response_data['choices'][0]['message']['content'].strip()
            st.text("Corrected Text:")
            st.text(corrected_text)

            # Convert corrected text to speech
            tts = gTTS(text=corrected_text, lang='en')  # Change 'en' to desired language code if needed
            tts_file_path = "corrected_audio.mp3"
            tts.save(tts_file_path)

            # Inform the user about the TTS completion
            st.success("Text-to-Speech conversion complete!")

            # Provide an audio player for the generated TTS audio
            st.audio(tts_file_path)

            # Optional: Clean up the temporary files
            os.remove(audio_file)

            # Replace the original audio in the video with the new audio track
            new_audio_clip = AudioFileClip(tts_file_path)
            final_video = video_clip.set_audio(new_audio_clip)

            # Define the output video file path
            output_video_path = "final_video.mp4"
            final_video.write_videofile(output_video_path, codec="libx264")

            # Inform the user that the video has been processed
            st.success("The original audio has been replaced with the new audio!")

            # Provide a download link for the final video
            with open(output_video_path, "rb") as file:
                st.download_button(label="Download Final Video", data=file, file_name=output_video_path)

        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    else:
        st.error("The uploaded video file does not contain an audio track.")
