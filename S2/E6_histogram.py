# EXERCISE 6
# Use ffmpeg to extract the YUV histogram and create a new video container, which
# video track will have the histogram displayed.

import subprocess

def generate_histogram(input_path, output_path):
    # define intermediate file paths
    scaled_path = 'scaled_input.mp4'
    histogram_path = 'histogram_input.mp4'

    # command to scale our video to a bigger size so that the histogram plot can be entirely seen
    # the previous resolution (original video size) was too small: 424x240
    c1 = f'ffmpeg -i {input_path} -vf "scale=1280:720" {scaled_path}'
    subprocess.run(c1, shell=True, check=True)

    # We generate a new video containing the original video (scaled to bigger size) and an overlay of yuv histogram
    c2 = f'ffmpeg -i {scaled_path} -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" {histogram_path}'
    subprocess.run(c2, shell=True, check=True)

    # Finally we package it in a new video container and remove previous files
    c3 = f'ffmpeg -i {histogram_path} -c copy -map 0:v -map 0:a -movflags +faststart {output_path}'
    subprocess.run(c3, shell=True, check=True)

    # Remove intermediate files
    c4 = f'rm {scaled_path} {histogram_path}'
    subprocess.run(c4, shell=True, check=True)