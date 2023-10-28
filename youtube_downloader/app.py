import pytube 

def download_youtube_video(youtube_url):
  """Downloads a YouTube video to the specified output file.

  Args:
    youtube_url: The URL of the YouTube video to download.
    output_filename: The name of the output file.
  """

  yt = pytube.YouTube(youtube_url)

  # Get the 720p video stream.
  video_stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

  # Download the video stream to the specified output path.
  try:
    video_stream.download(output_path="D:/Music/")
  except Exception as e:
    pass
  print("downloading...")


l = [
  "https://youtu.be/lOvzcjTzudc" 
, "https://youtu.be/0UdoWWwvkgI"
, "https://youtu.be/0qqnYDiMSZs"
, "https://youtu.be/rPiUSs8JE6Y"
, "https://youtu.be/cVlXimmjliU"
, "https://youtu.be/O0lrx0-VW8c"
, "https://youtu.be/TK8uvD-MDkE"
, "https://youtu.be/-wUD7rkIsms"
, "https://youtu.be/GNnClkZ9BM4"
, "https://youtu.be/qJO9LL_KofY"
, "https://youtu.be/dB78dH1NqJU"
, "https://youtu.be/oDpUmayryjg"
, "https://youtu.be/4wxTQ2-P3EY"
, "https://youtu.be/BXGxMYXU_sk"
, "https://youtu.be/cAf3NGkoMnA"
, "https://youtu.be/_mYpvqJTgC0"
, "https://youtu.be/lHV3mfjk_AA"
, "https://youtu.be/0XfMDlNKC6Q"
, "https://youtu.be/u9n_djhNoQs"
, "https://youtu.be/I97SecQg9vg"
, "https://youtu.be/lOvzcjTzudc"
, "https://youtu.be/UowOrIX6Hzo"
, "https://youtu.be/lyXCWmow7xo"
, "https://youtu.be/fsrQLToqu9E"
, "https://youtu.be/P0OOGm2OFZ4"
, "https://youtu.be/zCXb8HAS96U"
, "https://youtu.be/fnfLkvG5bz4"
, "https://youtu.be/O6fMzVHXWTQ"
, "https://youtu.be/R7xgUs30PJI"
, "https://youtu.be/oVmuGgnAPYE"
, "https://youtu.be/EZ3k69cPqvw"
, "https://youtu.be/ETacIorvEvk"
, "https://youtu.be/klIG3ZZUUl4"
, "https://youtu.be/I97SecQg9vg"
, "https://youtu.be/COShkmxW3VU"
, "https://youtu.be/2SlrFEJFxvg"
, "https://youtu.be/AWLNbdQf4eU"
, "https://youtu.be/2SlrFEJFxvg"
, "https://youtu.be/AWLNbdQf4eU"
, "https://youtu.be/obJ7Zos-haI"
, "https://youtu.be/-r-PMDXH3as"
, "https://youtu.be/y37l9QiZdLI"
, "https://youtu.be/oXswkBr-Zxc"
, "https://youtu.be/jBJNStCp0W8"
, "https://youtu.be/7KSinnKb2eU"
, "https://youtu.be/ixj_nJmhb68"
, "https://youtu.be/cVlXimmjliU?si=ZUBh1PErW-7DN1p6"
, "https://youtu.be/C4h1PHa6xr0?si=RFMCy80zrFTy_QQZ"
, "https://youtu.be/DpE9K63P8as?si=wSnjw9U68bdN6GOZ"
, "https://youtu.be/HlYvQWZYkVI?si=mCSzksnK718TH_EP"
, "https://youtu.be/O0lrx0-VW8c?si=GDRT6PFI2i4U_C5M"
, "https://youtu.be/uGXv_x5OJm0?si=HW7Hab6TUR6992FA"
, "https://youtu.be/G2Fd_XwPz0U?si=MdpvU3z29xcJik-6"
, "https://youtu.be/KMEydCaVyow?si=aOHLUzhfQ8_smafu"
, "https://youtu.be/0qqnYDiMSZs?si=x4vXkJR8LhCvAuMs"
, "https://youtu.be/sKrlsUhnyPk?si=_6xOh3JMTakql7bv"
, "https://youtu.be/QfLwSNBc2y4?si=2BayhaH_6YQLBOKr"
, "https://youtu.be/lOvzcjTzudc?si=sPfCLr2rdauJpltt"
, "https://youtu.be/GGQbbC-8lGg?si=8s4oJJ72sVapR-Q4"
, "https://youtu.be/cUzPXmqaJyA?si=IjYJVKBj3YrxVl2u"
, "https://youtu.be/uU9nSuVrwK8?si=-4U9Vs78ZdrH7CAH"
, "https://youtu.be/X9DY8e5e_w8?si=AvNZdRA_UpQu58KM"
, "https://youtu.be/DpE9K63P8as?si=wyBt16YQx8Q5K8tP"
, "https://youtu.be/5AkcXS2Iozo?si=A7ntuaidYr1gSHbx"
, "https://youtu.be/Mto0R7EKROk?si=-sTLtWTFg-SNuM8h"
, "https://youtu.be/ZQrQgHiT99c?si=MmFLv1NoLvhfxnOf"
]

l1 = [
  "https://www.youtube.com/watch?v=ipg5yCU4Qb8",
  "https://www.youtube.com/watch?v=HAQM4zHdXaA",
  "https://www.youtube.com/watch?v=KgHXGBix7Qk",
  "https://www.youtube.com/watch?v=Vu5qpdoU5Fo",
  "https://www.youtube.com/watch?v=jxAklJ1SMy0",
  "https://www.youtube.com/watch?v=WYDmXp03SHw"
]
if __name__ == "__main__":
  # Get the YouTube URL from the user.
  for i in range(len(l1)):
    print(i)
    youtube_url = l1[i]
    # Download the YouTube video.
    download_youtube_video(youtube_url)