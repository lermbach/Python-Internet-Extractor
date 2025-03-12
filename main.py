import yt_dlp # for downloading videos
import os  # For handling folder creation
import sys  # To exit script on errors

def progress_hook(d):
    """
    Progress tracking callback function for yt-dlp.
    This function is automatically called by yt-dlp during the download process
    to provide live updates on the progress.

    :param d: dict - The progress dictionary from yt-dlp containing various details
        about the current download status.
    """
    # If the video is currently downloading, show progress updates
    if d['status'] == 'downloading':
        percentage = d.get('_percent_str', '0%').strip()  # Download progress percentage
        speed = d.get('_speed_str', 'N/A').strip()  # Current download speed
        eta = d.get('_eta_str', 'N/A').strip()  # Estimated time remaining

        # Print the progress dynamically (overwrites previous output on the same line)
        print(f"\r⬇️ Downloading... {percentage} | Speed: {speed} | ETA: {eta}", end='', flush=True)

    # When the download is finished, print a completion message
    elif d['status'] == 'finished':
        print("\n✅ Download complete!\n")  # Move to a new line after completion

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
        'progress_hooks': [progress_hook], # Add progress tracking
    }
    try: 
        with yt_dlp.YoutubeDL(options) as ydl: # Create a YoutubeDL instance
            ydl.download([url]) # Start download
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Error: Failed to download video.\nDetails: {e}")
        sys.exit(1)  # Exit the script with an error code
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        sys.exit(1) 

if __name__ == "__main__":
    try:
        url = input("Enter Video/Playlist URL: ").strip()  # Prompt user for video/playlist URL
        if not url:
            raise ValueError("URL cannot be empty.")

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
        if format_option not in format_map:
            raise ValueError("Invalid format selection. Please enter a number between 1-4.")

        # Get the format string from the mapping (default to "best")
        selected_format = format_map.get(format_option, "best")

        download(url, selected_format, output_folder) # Call download function

    except ValueError as e:
        print(f"\n❌ Input Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        sys.exit(1)