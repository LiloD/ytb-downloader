from pytube import YouTube 
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--link', type=str)
args = parser.parse_args()

if args.link == "":
    print("link must be specified")
    exit(1)

print("Try downlaod youtube link: ", args.link)

SAVE_PATH = "./outputs" 

try: 
    # object creation using YouTube 
    yt = YouTube(args.link) 
except: 
    print("Connection Error") 
    exit(2)

# Get all streams and filter for mp4 files
video_streams = yt.streams.filter(file_extension='mp4', only_video=True)
max_res = 0
max_res_vstream = None
for vstream in video_streams:
    res = int(vstream.resolution[:-1])
    if res > max_res:
        max_res = res
        max_res_vstream = vstream

print("use Video Stream: {}".format(max_res_vstream))


audio_stream = yt.streams.filter(file_extension='mp4', only_audio=True)
max_abr = 0
max_abr_stream = None
for astream in audio_stream:
    abr = int(astream.abr[:-4])
    if abr > max_abr:
        max_abr = abr
        max_abr_stream = astream

print("use Audio Stream: {}".format(max_abr_stream))

try: 
    max_res_vstream.download(output_path=SAVE_PATH, filename="input_video.mp4")
    max_abr_stream.download(output_path=SAVE_PATH, filename="input_audio.mp4")
    print('Video downloaded successfully!')
except : 
    print("Some Error!")

#ffmpeg -i input_video_file.vcodec -i input_audio_file.acodec -c:v libx264 -crf 18 -c:a aac -b:a 128k -ar 48k output.mp4 
subprocess.run([
    "ffmpeg", 
    "-i", "input_video.mp4", 
    "-i", "input_audio.mp4" , 
    "-c:v", 
    "libx264", 
    "-crf" , 
    "18", 
    "-c:a", 
    "aac", 
    max_res_vstream.default_filename,
    "&&",
    "rm",
    "input_video.mp4", 
    "input_audio.mp4" , 
], shell=True, cwd=SAVE_PATH)