import yt_dlp # for downloading videos
import os  # For handling folder creation

def download(url, output_folder="downloads"): # Define video/playlist download function
    """
    Downloads a YouTube video or an entire playlist using yt-dlp.
    Saves files in the specified folder.

    :param url: str - The URL of the video or playlist to download.
    :param output_folder: str - Directory where files will be saved.
    """
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

    options = { 'format': 'best',
                'outtmpl': os.path.join(output_folder, '%(playlist_title)s/%(title)s.%(ext)s'),  
                # Saves as "output_folder/Playlist Name/Video Title.mp4"
                'noplaylist': False,  # Allow playlist downloads
            } 
    
    with yt_dlp.YoutubeDL(options) as ydl: # Create a YoutubeDL instance
        ydl.download([url]) # Start download

if __name__ == "__main__":
    url = input("Enter Video/Playlist URL: ") # Prompt user for video/playlist URL

    # Prompt user for output folder / default to "downloads/"
    output_folder = input("Enter output folder (leave empty for 'downloads'): ") or "downloads"

    download(url, output_folder) # Call download function