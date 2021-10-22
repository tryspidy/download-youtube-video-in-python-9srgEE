import YouTube from pytube

yt = YouTube(url)
t = yt.streams.filter(only_audio=True)
t[0].download(/path)