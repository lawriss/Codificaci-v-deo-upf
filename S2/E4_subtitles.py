# EXERCISE 4
# Create a new script which will download subtitles, integrate them and output a video with
# printed subtitles (this means, it will form part of the video track)

import subprocess

def add_subtitles(video_path, subtitles_path, output_path):

    # We take the input video (video_path), add the previously downloaded subtitles (subtitles_path)
    # and output our original video with the integrated subtitles (output_path)

    command = f'ffmpeg -i {video_path} -vf subtitles={subtitles_path} {output_path}'
    subprocess.run(command, shell=True, check=True)