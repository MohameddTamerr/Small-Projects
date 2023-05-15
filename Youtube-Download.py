from pytube import YouTube
url="https://youtu.be/lTxn2BuqyzU"
the_video = YouTube(url)
print("The Youtube Title is " )
print(the_video.title)
print("Thumbnail here ")
print(the_video.thumbnail_url)
for stream in the_video.streams:
    print(stream)
desired_resolution = "720p"
streams = the_video.streams.filter(res=desired_resolution)
chosen_stream = streams.first()
chosen_stream.download()
