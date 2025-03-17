from download_options import format_map
from utils import is_ffmpeg_installed
import sys  # exiting the program on validation failure

def validate_url(url):
    """
    Validates that the URL is not empty.

    :param url: str - The URL entered by the user.
    """
    if not url:
        print("❌ Error: URL cannot be empty.")
        sys.exit(1) 

def validate_format_selection(format_option):
    """
    Validates the format selection.
    Ensures the user entered a valid format (1-5).
    Also checks for FFmpeg requirement if MP3 is selected.

    :param format_option: str - The format number chosen by the user (should be between "1" and "5").
    """
    if format_option not in format_map:
        print("\n❌ Error: Invalid format selection. Please enter a number between 1-5.")
        sys.exit(1)

    if format_option == "5" and not is_ffmpeg_installed():
        print("\n❌ Error: FFmpeg is required for MP3 conversion.")
        sys.exit(1)

