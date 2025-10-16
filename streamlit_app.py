import streamlit as st
import streamlit.components.v1 as components
import base64

# Load video
video_path = "real_k2.mp4"
with open(video_path, "rb") as f:
    video_bytes = f.read()
    video_base64 = base64.b64encode(video_bytes).decode()

# Load Happy Diwali GIF
gif_path = "happy-diwali-happy-diwali-2023.gif"
with open(gif_path, "rb") as f:
    gif_bytes = f.read()
    gif_base64 = base64.b64encode(gif_bytes).decode()

# --- HTML & JS ---
components.html(
    f"""
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            background-color: black;
        }}
        #video-container, #gif-container {{
            height: 100vh;
            width: 100vw;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        video {{
            height: 100vh;
            width: 100vw;
            object-fit: cover;
        }}
        #gif-container {{
            display: none;
        }}
        img {{
            height: 100vh;
            width: 100vw;
            object-fit: cover;
        }}
    </style>

    <div id="video-container">
        <video id="mainVideo" autoplay controls playsinline>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

    <div id="gif-container">
        <img src="data:image/gif;base64,{gif_base64}" alt="Happy Diwali">
    </div>

    <script>
        const video = document.getElementById("mainVideo");
        const videoContainer = document.getElementById("video-container");
        const gifContainer = document.getElementById("gif-container");

        // Ensure sound is enabled
        video.muted = false;
        video.volume = 1.0;

        // When video ends: swap to GIF and trigger Streamlit balloons
        video.addEventListener("ended", function() {{
            videoContainer.style.display = "none";
            gifContainer.style.display = "flex";
            window.parent.postMessage({{ type: "SHOW_BALLOONS" }}, "*");
        }});
    </script>
    """,
    height=700,
)

# --- JS listener for Streamlit side ---
st.markdown(
    """
    <script>
        window.addEventListener("message", (event) => {
            if (event.data.type === "SHOW_BALLOONS") {
                const params = new URLSearchParams(window.location.search);
                params.set("show", "balloons");
                window.location.search = params.toString();
            }
        });
    </script>
    """,
    unsafe_allow_html=True
)

# --- Trigger balloons when query param is set ---
if st.query_params.get("show") == "balloons":
    st.balloons()
