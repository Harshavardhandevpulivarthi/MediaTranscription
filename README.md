# MediaTranscription
This project is designed to automate the transcription of audio and video files using OpenAI’s Whisper model. It processes a directory of media files, extracts spoken content, and stores the transcriptions in structured formats for easy access.

Key Features:
Automated Media File Detection: The script scans directories for common media file formats (.mp3, .wav, .mp4, .mkv, .mov, .avi).
AI-Powered Transcription: Utilizes Whisper’s tiny.en model for efficient and accurate English-language transcription.
Structured Output: Saves transcriptions as .txt and .json files for flexibility in downstream processing.
Error Handling: Implements exception handling to manage file processing errors.
Progress Tracking: Uses tqdm to display real-time progress when processing multiple files.
Technologies Used:
Python for scripting
Whisper for transcription
JSON & Text Processing for structured output
OS & TQDM for file handling and progress tracking
Conclusion:
This project streamlines media transcription, making it useful for content creators, researchers, and professionals who need automated speech-to-text conversion.
