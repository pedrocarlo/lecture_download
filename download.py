from pytube import YouTube

# where to save
SAVE_PATH = "C:/Users/Pedro Muniz/Desktop/Berkeley/eecs16b/lectures"  # to_do

# link of the video to be downloaded
# opening the file
link = open('links_file.txt', 'r')
count = 1
for i in link:
    try:

        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(i, use_oauth=True)
    except:

        # to handle exception
        print("Connection Error")

        # filters out all the files with "mp4" extension
    mp4files = yt.streams.filter(file_extension='mp4')

    # get the video with the extension and
    # resolution passed in the get() function
    d_video = mp4files.order_by("resolution").desc().first()
    d_audio = yt.streams.filter(type="audio").order_by("abr").desc().first()
    try:

        # downloading the video
        # d_video.download(output_path=SAVE_PATH, filename=f"lecture_{count}_video.mp4")
        d_audio.download(output_path=SAVE_PATH, filename=f"lecture_{count}_audio.webm")
    except:
        print("Some Error!")
    count += 1
print('Task Completed!')
