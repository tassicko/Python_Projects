import streamlit as st
import numpy as np
import plotly.express as px
import os
import subprocess

# 1. Set up the web page title
st.title("🤖 My First ML Visualizer")
st.write("This is running locally on my machine!")

# 2. Add interactive sidebar controls
st.sidebar.header("Visualizer Settings")
learning_rate = st.sidebar.slider("Learning Rate", min_value=0.01, max_value=1.0, value=0.1)
epochs = st.sidebar.slider("Number of Iterations", min_value=10, max_value=500, value=100)

# 3. Generate some fake ML-like data based on user input
x = np.linspace(-10, 10, epochs)
# Simulate a loss curve flattening out faster if learning rate is high
y = np.exp(-learning_rate * x) if learning_rate > 0 else x ** 2

# 4. Create an interactive plot
fig = px.line(x=x, y=y, labels={'x': 'Iterations', 'y': 'Loss/Error'}, title="Training Loss Curve Simulation")

# 5. Display the plot in the web app
st.plotly_chart(fig)

# ==========================================
# NEW: MANIM INTEGRATION SECTION
# ==========================================
st.header("🎬 Dynamic Manim Animation")
st.write("Click the button below to render a cinematic explanation of your settings.")

if st.button("Generate Manim Video"):
    with st.spinner("Manim is rendering your animation... Please wait."):
        # Create a temporary script file containing the Manim code
        manim_code = f"""
from manim import *

class LossAnimation(Scene):
    def construct(self):
        # Create axes configured dynamically to match iterations
        axes = Axes(
            x_range=[-10, 10, 2],
            y_range=[0, {max(y):.2f}, {max(y) / 5:.2f}],
            axis_config={{"color": BLUE}},
        )
        labels = axes.get_axis_labels(x_label="Iterations", y_label="Loss")

        # Plot the exact same mathematical function
        graph = axes.plot(
            lambda x: np.exp(-{learning_rate} * x), 
            color=MAROON,
            x_range=[-10, 10]
        )

        # Add labels describing the settings
        title = Text(f"LR: {learning_rate} | Iterations: {epochs}", font_size=24).to_edge(UP)

        # Animate everything on screen
        self.play(Write(axes), Write(labels))
        self.play(FadeIn(title))
        self.play(Create(graph), run_time=2)
        self.wait(1)
"""
        # Save the code to a temporary python file
        with open("temp_manim_scene.py", "w") as f:
            f.write(manim_code)

        # Call Manim via terminal.
        # '-ql' flag renders at Low Quality (480p) to keep Streamlit fast.
        # '--media_dir .' saves media folders in your current directory.
        command = "manim -ql --media_dir . temp_manim_scene.py LossAnimation"
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Manim's standard low-quality output path structure
        video_path = os.path.join("videos", "temp_manim_scene", "480p15", "LossAnimation.mp4")

        # Display the video if it rendered successfully
        if os.path.exists(video_path):
            st.success("Animation rendered successfully!")
            st.video(video_path)

            # Optional: Clean up the generated files to keep your directory tidy
            # os.remove("temp_manim_scene.py")
        else:
            st.error("Something went wrong with the Manim render. Ensure Manim is installed via pip.")
