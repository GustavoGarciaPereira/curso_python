from pytube import YouTube
YouTube('https://www.youtube.com/embed/BzYMFd-lQL4?si=S8-fQxmITW_9ulNG').streams.first().download()
# yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()