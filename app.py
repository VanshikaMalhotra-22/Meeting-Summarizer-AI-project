import gradio as gr

from transcriber import transcribe_audio
from summarizer import summarize_text


def process_meeting(audio):

    transcript = transcribe_audio(audio)

    summary = summarize_text(transcript)

    return transcript, summary


app = gr.Interface(
    fn=process_meeting,

    inputs=gr.Audio(
        type="filepath",
        label="Upload Meeting Recording"
    ),

    outputs=[
        gr.Textbox(label="Transcript", lines=10),
        gr.Textbox(label="Meeting Summary", lines=10)
    ],

    title="🎙️ AI Meeting Summarizer",

    description="Upload a meeting recording to generate a transcript and summary."
)

app.launch()