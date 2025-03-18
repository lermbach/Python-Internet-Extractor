from download_options import format_map
from utils import is_ffmpeg_installed
import yt_dlp  # For url validation
import re  # Regex 

def validate_url(url):
    """
    Uses yt-dlp's built-in validation to check if the URL belongs to a supported site.

    :param url: str - The URL entered by the user.
    """
    # Ensure the URL is not empty or just whitespace
    if not url.strip():
        raise ValueError("❌ Error: URL cannot be empty.")
    
    # Check if input looks like a valid URL
    url_pattern = re.compile(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", re.IGNORECASE)
    if not url_pattern.match(url):
        raise ValueError("❌ Error: Invalid input. Please enter a valid URL.")
    
    # Let yt-dlp determine if the site is supported
    try:
        # Attempt to extract metadata for the URL using yt-dlp
        # `download=False`: Do not download the video, just check its validity.
        # `process=False`: Skip further processing, only validate the URL.
        yt_dlp.YoutubeDL().extract_info(url, download=False, process=False)
    except yt_dlp.utils.UnsupportedError:
        raise ValueError("❌ Error: This site is not supported by yt-dlp.")
    except yt_dlp.utils.DownloadError:
        # Catch download-related errors (e.g., network issues, failed extraction)
        raise ValueError("❌ Error: Failed to retrieve video information. The site may require login or be temporarily unavailable.")
    except Exception:
        # Catch any other unexpected errors
        raise ValueError("❌ Error: Could not validate the URL. Please check the link and try again.")

def validate_format_selection(format_option):
    """
    Validates the format selection.
    Ensures the user entered a valid format (1-5).
    Also checks for FFmpeg requirement if MP3 is selected.

    :param format_option: str - The format number chosen by the user (should be between "1" and "5").
    """
    if format_option not in format_map:
        raise ValueError("❌ Error: Invalid format selection. Please enter a number between 1-5.")

    if format_option == "5" and not is_ffmpeg_installed():
        raise ValueError("❌ Error: FFmpeg is required for MP3 conversion.")

