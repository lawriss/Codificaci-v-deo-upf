# P2 - PYTHON & VIDEO
import subprocess

# EXERCISE 1
# Create a python script which converts this video into a .mp2 video file, 
# and is able to parse the ‘ffmpeg –i BBB.mp2’ file and save the video info

# We first set the path of the input video and the output file.
input_video = "/Users/valentin/Desktop/P2_video/Codificaci-v-deo-upf/bunny.mp4"
E1_output_mp2 = "/Users/valentin/Desktop/P2_video/Codificaci-v-deo-upf/BBB.mp2"

# We define the ffmpeg command that converts our file from mp4 to mp2 
t1_command = f"ffmpeg -i {input_video} -c:v mpeg2video -q:v 0 {E1_output_mp2}" 

# We run the command with subprocess and obtain a mp2 file called "BBB.mp2"
subprocess.run(t1_command, shell=True, check=True)
print(f"Video conversion to MP2 completed: {E1_output_mp2}")

# Now we extract video info with the following ffmpeg command
T1_1_command = f"ffprobe {E1_output_mp2}"
info = subprocess.check_output(T1_1_command, shell=True, stderr=subprocess.STDOUT, text=True)

# And save the video information in a txt file
info_file = "video_info.txt"
with open(info_file, "w") as f:
    for line in info.split('\n'):
        f.write(line)
        f.write('\n')


# EXERCISE 2
# On this script, create a method which lets you use ffmpeg to modify the resolution.
# The original resolution was 424x240
resolution_w = 42
resolution_h = 24
E2_output = "/Users/valentin/Desktop/P2_video/Codificaci-v-deo-upf/BBB_less_resolution.mp4"
t2_command = f"ffmpeg -i {input_video} -vf scale={resolution_w}:{resolution_h} {E2_output}"
subprocess.run(t2_command, shell=True, check=True)


# EXERCISE 3
# Create another method which lets you change the chroma subsampling
def change_ch_subsampling(inp, out, subs):
    t3_command = f"ffmpeg -i {inp} -c:v libx264 -vf format={subs} {out}"
    subprocess.run(t3_command, shell=True, check=True)

E3_output = "/Users/valentin/Desktop/P2_video/Codificaci-v-deo-upf/BBB_chr_subsampling.mp4"
chroma_subsampling = ['yuv420p', 'yuv422p', 'yuv444p'] #Respectively: 8-bit [4:2:0, 4:2:2, 4:4:4]
# In this case, if we use 4:2:0:, Cb' and Cr' are each subsampled at a factor of two,
# both horizontally and vertically
change_ch_subsampling(input_video, E3_output, chroma_subsampling[0])


# EXERCISE 4
# Create another method which lets you read the video info and print at
# least 5 relevant data from the video
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

# We call the function
original_video = "/Users/valentin/Desktop/P2_video/Codificaci-v-deo-upf/bunny.mp4"
read_vid_info(original_video)

# EXERCISE 5
# Let’s try to level up your coding skills. Remember your script from P1? Learn how to
# inheritate and try to do some interaction with it from the new script

# we import our previous lab (inherit the script)
# NOTE: I did the lab1 in google collab, and lab2 in PyCharm. When importing lab1 thus, there were
# many errors of compatibility. That's why I commented the ffmpeg commands because they didn't
# work properly in PyCharm. But the other functions can be used when inheriting with no problem.
# I also added "if __name__ == "__main__":" before prints so that when we import the lab, we don't
# get all the previous prints. From now on I will use PyCharm :)

import P1_240445 as p1

# checking that we can call functions from the other script properly
y,u,v = p1.rgb_to_yuv(210,123,85)
r,g,b = p1.yuv_to_rgb(y,u,v)
print("\n \n TASK 5:")
print(r,g,b)