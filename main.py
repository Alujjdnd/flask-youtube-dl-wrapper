from pytube import YouTube

#ask for the link from user
link = "https://www.youtube.com/watch?v=o_czzvTTdHg"
yt = YouTube(link)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

YouTube('https://www.youtube.com/watch?v=o_czzvTTdHg').streams.get_highest_resolution().download()