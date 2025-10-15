import streamlit as st
import streamlit.components.v1 as components
import base64

# Load your local audio file
audio_path = "Kantara.mp3"
with open(audio_path, "rb") as f:
    audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()

# Load your local video file
video_path = "k2.mp4"
with open(video_path, "rb") as f:
    video_bytes = f.read()
    video_base64 = base64.b64encode(video_bytes).decode()

# Inject HTML to make video take full viewport size
components.html(
    f"""
    <style>
        html, body, #video-container {{
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            background-color: black;
        }}
        video {{
            height: 100vh;
            width: 100vw;
            object-fit: cover; /* maintain aspect ratio and cover whole screen */
        }}
        audio {{
            display: none;
        }}
    </style>
    <div id="video-container">
        <video autoplay muted controls playsinline>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    </div>
    """,
    height=700,
)
