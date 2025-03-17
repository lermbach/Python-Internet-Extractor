from download_options import format_map
from utils import is_ffmpeg_installed
import sys  # For exiting the program on validation failure
from urllib.parse import urlparse # For extracting the domain from the URL

def validate_url(url, supported_sites):
    """
    Validates that the URL is not empty and belongs to a supported site.

    :param url: str - The URL entered by the user.
    :param supported_sites: list - The list of supported site names.
    """
    if not url:
        print("❌ Error: URL cannot be empty.")
        sys.exit(1)

    # Extract the domain from the URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()  # Extract domain (e.g., "youtube.com")

    # Check if the domain matches any supported sites
    if not any(site in domain for site in supported_sites):
        print(f"❌ Error: This site is not supported.\nUse `?` to see supported sites.")
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

