import subprocess, os, math

ffmeg_dir = "C:/Users/Pedro Muniz/Desktop/ffmpeg/bin"
SAVE_PATH = "C:/Users/Pedro Muniz/Desktop/Berkeley/eecs16b/lectures"
SAVE_PATH1 = "C:/Users/Pedro Muniz/Desktop/Berkeley/eecs16b/lectures"

os.chdir(ffmeg_dir)
files = os.listdir(SAVE_PATH1)


files = {os.path.splitext(f)[0] for f in files}
print(files)
print(len(files))

# ffmpeg -i INPUT_FILE.mp4 -i AUDIO.wav -c:v copy -c:a aac OUTPUT_FILE.mp4
for i in range(1, len(files) + 1, 2):
    i = math.ceil(i / 2)
    video = SAVE_PATH + f'/lecture_{i}_video.mp4'
    audio = SAVE_PATH + f'/lecture_{i}_audio.webm'
    out_file = SAVE_PATH + f'/lecture_{i}.mp4'
    print(video)
    print(audio)
    print(out_file)
    print(subprocess.check_output(["ffmpeg", "-i", f"\"{video}\"", "-i", audio, "-c:v", 'copy', '-c:a', 'aac', out_file]))




