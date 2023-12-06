import subprocess

# EXERCISE 2

#Create a script that will export 2 video comparision. For example: VP8 vs VP9 (both in same screen).
#Then choose 2 codecs of the 4 mentioned before, create the output and comment the
#differences you find there

def compare_vid(path1, path2, output_path):
    cc2 = f'ffmpeg -i {path1} -i {path2} -filter_complex "[0:v][1:v]hstack=inputs=2[v];[0:a][1:a]amerge[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k {output_path}'
    subprocess.run(cc2, shell=True, check=True)