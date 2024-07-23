import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',  # Download the best quality format available
        'outtmpl': 'downloaded_video.%(ext)s',  # Output file name template
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 format after download
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Replace this URL with the actual video URL you found via browser developer tools
    video_url = 'blob:https://learning.oreilly.com/e73d1dfd-fac7-4de7-b908-bb82636b22ec'
    download_video(video_url)
