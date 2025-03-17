import yt_dlp  # For downloading videos 
from download_options import get_yt_dlp_options  # Import function that handles yt-dlp options

def download(url, selected_format, format_option, output_folder="downloads"):
    """
    Downloads a video or an entire playlist using yt-dlp.
    Saves files in the specified output folder.

    :param url: str - The URL of the video or playlist to download.
    :param selected_format: str - The selected format for the download.
    :param format_option: str - The user's selection from main.py (1-5).
    :param output_folder: str - The directory where the files will be saved (default: "downloads").
    """
    # Get yt-dlp options dynamically from download_options.py
    options = get_yt_dlp_options(selected_format, output_folder, format_option)

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])  # Start the download process using yt-dlp
    except yt_dlp.utils.DownloadError as e:
        raise RuntimeError(f"\n❌ Error: Failed to download video.\nDetails: {e}")
    except Exception as e:
        raise RuntimeError(f"\n❌ Unexpected Download Error: {e}")
