# SEMINAR / LAB 3 - LAURA RUIZ - NIA: 240445
import subprocess
# EXERCISE 1
# Convert BBB video into: 720p, 480p, 360x240, 160x120
# Convert them into VP8, VP9, h265 & AV1
class change_resolution:
    def convert_720p(self, BBB_path):
        output720p = 'BBB_720p.mp4'
        c1 = f'ffmpeg -i {BBB_path} -vf "scale=1280:720" -c:a copy {output720p}'
        subprocess.run(c1, shell=True, check=True)

    def convert_480p(self, BBB_path):
        output480p = 'BBB_480p.mp4'
        c2 = f'ffmpeg -i {BBB_path} -vf "scale=640:480" -c:a copy {output480p}'
        subprocess.run(c2, shell=True, check=True)

    def convert_360x240(self, BBB_path):
        output360x240 = 'BBB_360x240.mp4'
        c3 = f'ffmpeg -i {BBB_path} -vf "scale=360:240" -c:a copy {output360x240}'
        subprocess.run(c3, shell=True, check=True)

    def convert_160x120(self, BBB_path):
        output160x120 = 'BBB_160x120.mp4'
        c4 = f'ffmpeg -i {BBB_path} -vf "scale=160:120" -c:a copy {output160x120}'
        subprocess.run(c4, shell=True, check=True)

    def convert_VP8(self, BBB_path):
        outputVP8 = 'BBB_VP8.webm'
        c5 = f'ffmpeg -i {BBB_path} -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis {outputVP8}'
        subprocess.run(c5, shell=True, check=True)

    def convert_VP9(self, BBB_path):
        outputVP9 = 'BBB_VP9.webm'
        c6 = f'ffmpeg -i {BBB_path} -c:v libvpx-vp9 -crf 30 -b:v 0 {outputVP9}'
        subprocess.run(c6, shell=True, check=True)

    def convert_h265(self, BBB_path):
        outputh265 = 'BBB_h265.mp4'
        c7 = f'ffmpeg -i {BBB_path} -c:v libx265 -crf 28 -preset medium -c:a aac -b:a 128k {outputh265}'
        subprocess.run(c7, shell=True, check=True)

# AV1 (this takes too long)
#outputAV1 = 'BBB_AV1.mkv'
#c8 = f'ffmpeg -i {BBB_path} -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental {outputAV1}'
#subprocess.run(c8, shell=True, check=True)

# define paths
BBB_path_complete = '../bunny.mp4'
BBB_cut_path = 'BBB_cut.mp4'
# cut video for faster processing
cut_command = f"ffmpeg -i {BBB_path_complete} -ss 00:03:00 -to 00:03:30 -c:v copy -c:a copy {BBB_cut_path}"
subprocess.run(cut_command, shell=True, check=True)

# create object: video modificable
video_modif = change_resolution()

# modify video resolution (to 480p format)
video_modif.convert_480p(BBB_cut_path)
print('EXERCISE 1 DONE\n\n')


# EXERCISE 2

# import ex 2 script
import SP3_Exercise2

# convert video to VP8
video_modif.convert_VP8(BBB_cut_path)
# convert video to VP9
video_modif.convert_VP9(BBB_cut_path)

# define input and output paths
path_VP8 = 'BBB_VP8.webm'
path_VP9 = 'BBB_VP9.webm'
out_path = 'comparison_output.mp4'

# create comparison video
SP3_Exercise2.compare_vid(path_VP8, path_VP9, out_path)
print('EXERCISE 2 DONE\n\n')

