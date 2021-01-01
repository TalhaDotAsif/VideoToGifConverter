from moviepy.editor import videoFileClip

clip = VideoFileClip("video.mp4")
clip.write_gif("mygif.gif,fps=10")