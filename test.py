from pytube import YouTube

yt = YouTube('https://youtube.com/watch?v=2lAe1cqCOXo')

print(yt.streams.filter(type="audio").order_by('abr').desc())
print(yt.streams.filter(type="video").order_by('resolution').desc())

