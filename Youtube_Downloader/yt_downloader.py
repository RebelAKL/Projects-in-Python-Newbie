from pytube import YouTube
video_url = 'https://www.youtube.com/watch?v=BaFdKJxWspk'
yt = YouTube(video_url)
video_stream = yt.streams.filter(res='480p', progressive=True).first()
download_path = 'F:\Projects\Youtube_Downloader'
video_stream.download(output_path=download_path)
print('Download complete!')
