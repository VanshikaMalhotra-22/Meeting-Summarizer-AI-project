import whisper

# Load the Whisper model
model = whisper.load_model("base")


def transcribe_audio(audio_path):
    """
    Converts speech in an audio file into text.

    Parameters:
        audio_path (str): Path to the audio file.

    Returns:
        str: Transcribed text.
    """

    result = model.transcribe(audio_path)
    transcript = result["text"]

    return transcript


if __name__ == "__main__":
    print("transcriber.py is running...")

    audio_file = "audio/sample.mp3"

    transcript = transcribe_audio(audio_file)

    print("\nTranscript:\n")
    print(transcript)

    with open("outputs/transcript.txt", "w", encoding="utf-8") as file:
        file.write(transcript)

    print("\nTranscript saved successfully!")