# SEMINAR 2 - (MORE) PYTHON & VIDEO - LAURA RUIZ (NIA: 240445)

import subprocess
import json

class Seminar_two:

    # EXERCISE 1 METHODS
    # Method that cuts the desired video fragment and saves it in the chosen path
    def cut_vid(self, in_path, out_path, init_t, end_t):
        cut_command = f"ffmpeg -i {in_path} -ss {init_t} -to {end_t} -c:v copy -c:a copy {out_path}"
        subprocess.run(cut_command, shell=True, check=True)
        print("Video cut generated.")

    # Method to generate a video that contains motion vectors.
    def video_vectors(self, in_path, out_path):
        motion_vec_comm = f"ffmpeg -flags2 +export_mvs -i {in_path} -vf codecview=mv=pf+bf+bb {out_path}"
        subprocess.run(motion_vec_comm, shell=True, check=True)
        print("Motion vector video generated.")

    # EXERCISE 2 METHOD
    def exercise_two(self, in_path, out_path):
        # cut 50 sec video
        out1 = 'S2_generated_files/E2_BBB_50s.mp4'
        self.cut_vid(in_path, out1, '00:03:10', '00:04:00')

        # extract mono audio from 50-sec video
        out2 = 'S2_generated_files/E2_BBB_mono.mp3'
        mono_track_comm = f"ffmpeg -i {out1} -f mp3 -ab 192000 -ac 1 -vn {out2}"
        subprocess.run(mono_track_comm, shell=True, check=True)

        # extract stereo audio at lower bitrate (b:a 32k)
        out3 = 'S2_generated_files/E2_BBB_stereo.mp3'
        stereo_track_comm = f"ffmpeg -i {out1} -f mp3 -vn -b:a 32k {out3}"
        subprocess.run(stereo_track_comm, shell=True, check=True)

        # audio in AAC codec
        out4 = 'S2_generated_files/E2_BBB_aac.aac'
        aac_comm = f"ffmpeg -i {out1} -vn -c:a aac {out4}"
        subprocess.run(aac_comm, shell=True, check=True)

        # Now package everything in a .mp4 with FFMPEG
        cc = f'ffmpeg -i {out1} -i {out2} -i {out3} -i {out4} -c copy -map 0:v -map 1:a -map 2:a -map 3:a -movflags +faststart {out_path}'

        # run process
        subprocess.run(cc, shell=True, check=True)

    # EXERCISE 3 METHOD
    def analyze_container(self, in_path):
        analyze_container_comm = ['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-of', 'json', in_path]
        output = subprocess.run(analyze_container_comm, capture_output=True, text=True)
        if output.returncode == 0:
            json_data = json.loads(output.stdout)
            audio_tracks = sum(1 for stream in json_data['streams'] if stream['codec_type'] == 'audio')
            video_tracks = sum(1 for stream in json_data['streams'] if stream['codec_type'] == 'video')
            subtitle_tracks = sum(1 for stream in json_data['streams'] if stream['codec_type'] == 'subtitle')
            total_tracks = {
                'Audio tracks': audio_tracks,
                'Video tracks': video_tracks,
                'Subtitle tracks': subtitle_tracks
            }
            return total_tracks
        else:
            return None


# EXERCISE 1
# Cut 9 seconds from BBB. Start a Python script that, with the help from FFMpeg, it will have a
# method inside a Class, which will output a video that will show the macroblocks and the motion vectors

# We declare the variables and paths our methods require.
BBB_path = "../bunny.mp4" # path of our original video
cut_vid_path = "S2_generated_files/E1_BBB_9sec.mp4"
vectors_vid_path = "S2_generated_files/E1_BBB_motion_vec.mp4"
init_time = '00:02:00'
end_time = '00:02:09'

BBB = Seminar_two() # We create a Seminar_two object
BBB.cut_vid(BBB_path, cut_vid_path, init_time, end_time) #cut original video into a 9-second fragment
BBB.video_vectors(cut_vid_path, vectors_vid_path) #generates a video that contains motion vectors from the above 9-sec video.
print("\nEXERCISE 1 DONE\n")


# EXERCISE 2
# You’re going to create another method in order to create a new BBB container. It will fulfill this requirements:
# · Cut BBB into 50 seconds only video.
# · Export BBB(50s) audio as MP3 mono track.
# · Export BBB(50s) audio in MP3 stereo w/ lower bitrate
# · Export BBB(50s) audio in AAC codec
# Now package everything in a .mp4 with FFMPEG!!

container_path = 'S2_generated_files/E2_container.mp4'
BBB.exercise_two(BBB_path, container_path)
print("\nEXERCISE 2 DONE\n")


# EXERCISE 3
# Create another method which reads the tracks from an MP4 container, and it’s able to say how
# many tracks does the container contains

mp4_file_path = 'S2_generated_files/E2_container.mp4'  # Replace with your MP4 file path
tracks_info = BBB.analyze_container(mp4_file_path)
if tracks_info:
    for i in tracks_info:
        print(i, ": ", tracks_info[i])
else:
    print("No info to read")
print("\nEXERCISE 3 DONE\n")

# EXERCISE 4 & 5
# Create a new script which will download subtitles, integrate them and output a video with
# printed subtitles (this means, it will form part of the video track).

# Define paths
video_path = 'E6_files/friends_vid.mp4' # input video path
# We may download subtitles previously so that we have an .srt file:
subtitles_path = 'E6_files/friends_vid_subs.srt' # subtitles file path (.srt)
output_path = 'S2_generated_files/E4_video_subtitled.mp4' # output path (.mp4 container)

# import script
import E4_subtitles

# call function to add subtitles
E4_subtitles.add_subtitles(video_path, subtitles_path, output_path)
print("\nEXERCISE 4 AND 5 DONE\n")

# EXERCISE 6
# Same as last process (individual script, which method will be inheritated in the main one). This
# time, we need to use ffmpeg to extract the YUV histogram and create a new video container, which
# video track will have the histogram displayed.

# Import new script
import E6_histogram

# Define input and output paths
BBB_path = "S2_generated_files/E1_BBB_9sec.mp4"
BBB_container_hist_path = 'S2_generated_files/E6_BBB_histogram.mp4'

# Call function
E6_histogram.generate_histogram(BBB_path, BBB_container_hist_path)
print("\nEXERCISE 6 DONE\n")

