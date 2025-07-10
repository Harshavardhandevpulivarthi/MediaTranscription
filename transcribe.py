import os
import whisper
import json
from tqdm import tqdm

# Define input and output directories
INPUT_DIR = "input_transcriptions"
OUTPUT_DIR = "output_transcriptions"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the smallest Whisper model

model = whisper.load_model("tiny.en")  # English-only, uses less memory


def transcribe_media(file_path):
    """Transcribes a given media file using Whisper."""
    try:
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def process_directory(directory):
    """Scans the directory for media files and transcribes them."""
    media_extensions = {".mp3", ".wav", ".mp4", ".mkv", ".mov", ".avi"}
    for root, _, files in os.walk(directory):
        for file in tqdm(files, desc="Processing Files"):
            if any(file.lower().endswith(ext) for ext in media_extensions):
                file_path = os.path.join(root, file)
                print(f"Transcribing: {file_path}")

                transcription = transcribe_media(file_path)
                if transcription:
                    save_transcription(file, transcription)

def save_transcription(file_name, text):
    """Saves the transcription to a text and JSON file."""
    base_name = os.path.splitext(file_name)[0]
    txt_path = os.path.join(OUTPUT_DIR, f"{base_name}.txt")
    json_path = os.path.join(OUTPUT_DIR, f"{base_name}.json")

    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)
    
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump({"file": file_name, "transcription": text}, json_file, indent=4)

if __name__ == "__main__":
    process_directory(INPUT_DIR)
    print("Transcription process completed!")