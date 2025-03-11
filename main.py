import yt_dlp # for downloading videos
import os  # For handling folder creation

def download(url, selected_format="best", output_folder="downloads"): # Define video/playlist download function
    """
    Downloads a video or an entire playlist using yt-dlp.
    Saves files in the specified folder.

    :param url: str - The URL of the video or playlist to download.
    :param output_folder: str - Directory where files will be saved.
    :param selected_format: str - The format in which the video should be downloaded.
    """
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

    # Check if the URL is a playlist by looking for "list=" in the URL
    if "list=" in url:
        output_template = os.path.join(output_folder, '%(playlist_title)s/%(title)s.%(ext)s')
    else:
        output_template = os.path.join(output_folder, '%(title)s.%(ext)s')

    options = {
        'format': selected_format,  # Use selected format
        'outtmpl': output_template,  # Saves single videos differently from playlists
        'noplaylist': False,  # Allow playlist downloads
    }
    
    with yt_dlp.YoutubeDL(options) as ydl: # Create a YoutubeDL instance
        ydl.download([url]) # Start download

if __name__ == "__main__":
    url = input("Enter Video/Playlist URL: ").strip() # Prompt user for video/playlist URL

    # Prompt user for output folder / default to "downloads/"
    output_folder = input("Enter output folder (leave empty for 'downloads'): ").strip() or "downloads"

    # Print format list
    print("\nChoose a format:")
    print("1 - Best quality (default)")
    print("2 - MP4")
    print("3 - WEBM")
    print("4 - Best quality (audio only)")
    # Prompt user to choose format
    format_option = input("Enter format number: ").strip() or "1"  # Default to "1" (best quality)

    # Mapping user choice to yt-dlp format codes
    format_map = {
        "1": "best",  # Best available quality
        "2": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",  # MP4
        "3": "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]",  # WEBM
        "4": "bestaudio/best",  # Audio only (best available quality)
    }

    # Get the format string from the mapping (default to "best")
    selected_format = format_map.get(format_option, "best")

    download(url, selected_format, output_folder) # Call download function