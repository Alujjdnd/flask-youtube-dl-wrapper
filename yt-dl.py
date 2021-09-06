import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=jXLZjwkbBik',
        download=False  # We just want to extract the info
    )

video = result

print(video)
for item in video["formats"]:
    format = item["format_note"]
    video_url = item["url"]
    print(format)
    print(video_url, "\n")
