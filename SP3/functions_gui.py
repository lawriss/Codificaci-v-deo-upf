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
    print('Histogram video generated')

def video_vectors(in_path, out_path):
    motion_vec_comm = f"ffmpeg -flags2 +export_mvs -i {in_path} -vf codecview=mv=pf+bf+bb {out_path}"
    subprocess.run(motion_vec_comm, shell=True, check=True)
    print("Motion vector video generated.")

def read_vid_info(path):
    T4_command = f"ffprobe {path}"
    info = subprocess.check_output(T4_command, shell=True, stderr=subprocess.STDOUT, text=True)
    print("TASK 4 - VIDEO INFORMATION: ")
    for line in info.split('\n'):
        if line.startswith('  Duration:'):
            output1 = line.replace(",", "\n")
            print(output1)
        if line.startswith('  Stream #0:0'):
            output1 = line.replace(",", "\n")
            print(output1)

def download_mp3(in_path, out_path):
    comm = f'ffmpeg -i {in_path} -vn -acodec libmp3lame -q:a 4 {out_path}'
    subprocess.run(comm, shell=True, check=True)

def convert_VP8(BBB_path):
    outputVP8 = 'output_VP8.webm'
    c5 = f'ffmpeg -i {BBB_path} -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis {outputVP8}'
    subprocess.run(c5, shell=True, check=True)

def convert_VP9(BBB_path):
    outputVP9 = 'output_VP9.webm'
    c6 = f'ffmpeg -i {BBB_path} -c:v libvpx-vp9 -crf 30 -b:v 0 {outputVP9}'
    subprocess.run(c6, shell=True, check=True)

def convert_h265(BBB_path):
    outputh265 = 'output_h265.mp4'
    c7 = f'ffmpeg -i {BBB_path} -c:v libx265 -crf 28 -preset medium -c:a aac -b:a 128k {outputh265}'
    subprocess.run(c7, shell=True, check=True)

def convert_720p(BBB_path):
    output720p = 'output_720p.mp4'
    c1 = f'ffmpeg -i {BBB_path} -vf "scale=1280:720" -c:a copy {output720p}'
    subprocess.run(c1, shell=True, check=True)

def convert_480p(BBB_path):
    output480p = 'output_480p.mp4'
    c2 = f'ffmpeg -i {BBB_path} -vf "scale=640:480" -c:a copy {output480p}'
    subprocess.run(c2, shell=True, check=True)

def convert_360x240(BBB_path):
    output360x240 = 'output_360x240.mp4'
    c3 = f'ffmpeg -i {BBB_path} -vf "scale=360:240" -c:a copy {output360x240}'
    subprocess.run(c3, shell=True, check=True)

def convert_160x120(BBB_path):
    output160x120 = 'output_160x120.mp4'
    c4 = f'ffmpeg -i {BBB_path} -vf "scale=160:120" -c:a copy {output160x120}'
    subprocess.run(c4, shell=True, check=True)

def compare_vid(path1, path2, output_path):
    cc2 = f'ffmpeg -i {path1} -i {path2} -filter_complex "[0:v][1:v]hstack=inputs=2[v];[0:a][1:a]amerge[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k {output_path}'
    subprocess.run(cc2, shell=True, check=True)