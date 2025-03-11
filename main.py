import yt_dlp # for downloading videos

def download_video(url): # Define video download function
    """
    Downloads a video using yt-dlp.

    :param url: str - The URL of the video to download.
    """
    options = { 'format': 'best'} # Define download options
    
    with yt_dlp.YoutubeDL(options) as ydl: # Create a YoutubeDL instance
        ydl.download([url]) # Start download

if __name__ == "__main__":
    video_url = input("Enter Video URL: ") # Prompt user for video URL
    download_video(video_url) # Call download function