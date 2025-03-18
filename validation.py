from download_options import format_map
from utils import is_ffmpeg_installed
from urllib.parse import urlparse # For extracting the domain from the URL

def validate_url(url, supported_sites):
    """
    Validates that the URL is not empty and belongs to a supported site.

    :param url: str - The URL entered by the user.
    :param supported_sites: list - The raw list of supported site names.
    :raises ValueError: If the URL is empty or the site is unsupported.
    """
    if not url.strip():
        raise ValueError("❌ Error: URL cannot be empty.")

    # Extract the domain from the URL
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.lower().split(".")

    # Extract base domain (e.g., 'YouTube' from 'www.YouTube.com')
    base_domain = domain_parts[-2] if len(domain_parts) > 2 else domain_parts[0]

    # Process the raw supported sites list to extract their base names
    processed_sites = {site.split(":")[0].lower() for site in supported_sites}

    # Check if the extracted base domain matches any supported site
    if base_domain in processed_sites:
        return  # URL is valid

    # If no match, raise an error
    raise ValueError("❌ Error: This site is not supported. Use `?` to see supported sites.")

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

