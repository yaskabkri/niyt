from moviepy.editor import VideoClip
import numpy as np

# Define a function that returns the frame at time t
def animate(t):
    # Create a numpy array representing a colored frame
    frame = np.zeros((300, 400, 3), dtype=np.uint8)
    frame[:int(100 + 100 * t), :int(200 + 100 * t)] = [255, 255, 255]
    return frame

# Create a VideoClip with the animation function and duration
animation = VideoClip(animate, duration=2)

# Write the animation to a file
animation.write_videofile("animated_output.mp4", fps=24)
