import pytube 

def download_youtube_video(youtube_url):
  """Downloads a YouTube video to the specified output file.

  Args:
    youtube_url: The URL of the YouTube video to download.
    output_filename: The name of the output file.
  """

  yt = pytube.YouTube(youtube_url)

  # Get the 360p video stream.
  video_stream = yt.streams.filter(progressive=True, file_extension="mp4", resolution="360p").first()


  # Download the video stream to the specified output path.
  try:
    video_stream.download(output_path="D:/Music/")
  except Exception as e:
    pass
  print("downloading...")


l = [
  "https://www.youtube.com/watch?v=oDpUmayryjg",
  "https://www.youtube.com/watch?v=UowOrIX6Hzo",
  "https://www.youtube.com/watch?v=lyXCWmow7xo",
  "https://www.youtube.com/watch?v=GNnClkZ9BM4",
  "https://www.youtube.com/watch?v=oXswkBr-Zxc",
  "https://www.youtube.com/watch?v=AWLNbdQf4eU",
  "https://www.youtube.com/watch?v=KMEydCaVyow"
]

l1 = [
  "https://www.youtube.com/watch?v=WYDmXp03SHw"
]
if __name__ == "__main__":
  # Get the YouTube URL from the user.
  for i in range(len(l1)):
    print(i)
    youtube_url = l[i]
    # Download the YouTube video.
    download_youtube_video(youtube_url)
