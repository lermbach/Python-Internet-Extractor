import yt_dlp  # For checking if FFmpeg is installed and getting supported sites

def get_supported_sites():
    """
    Fetches the list of supported websites from yt-dlp.

    :return: list - A sorted list of supported site names.
    """
    try:
        # Get a list of supported sites from yt-dlp
        extractors = yt_dlp.extractor.gen_extractors()
        sites = sorted(set(e.IE_NAME for e in extractors if hasattr(e, "IE_NAME")))

        return sites  # Return the raw site list
    except Exception as e:
        print(f"⚠️ Error fetching sites: {e}")
        return []  # Return an empty list if an error occurs
    
def format_supported_sites(supported_sites):
    """
    Formats the supported sites list into multiple columns for user readability.

    :param supported_sites: list - The raw list of supported site names.
    :return: str - Formatted string with site names arranged in columns.
    """
    if not supported_sites:
        return "⚠️ No supported sites available."

    num_cols = 3  # Number of columns for display
    max_length = max(len(site) for site in supported_sites)  # Find longest site name
    col_width = max(max_length + 2, 30)  # Set column width dynamically, minimum 30

    formatted_sites = ""  # Initialize output string

    for i, site in enumerate(supported_sites, 1):
        formatted_sites += site.ljust(col_width)  # Align site names evenly
        if i % num_cols == 0:  # Insert a new line after every 'num_cols' entries
            formatted_sites += "\n"

    return formatted_sites.strip()  # Return the formatted string


def is_ffmpeg_installed():
    """
    Checks if FFmpeg is available for post-processing.

    :return: bool - True if FFmpeg is installed, False otherwise.
    """
    # Uses yt-dlp's built-in method to check if FFmpeg is installed.
    return yt_dlp.postprocessor.FFmpegPostProcessor().available

def show_ffmpeg_warning():
    """
    Displays a warning if FFmpeg is not installed.
    """
    if not is_ffmpeg_installed():
        print("\n⚠️  WARNING: FFmpeg not found.")
        print("   - The downloaded format may not be the best available.")
        print("   - FFmpeg is required for converting videos to MP3.")
        print("   - 🔗 Official FFmpeg Download: https://ffmpeg.org/download.html\n")

def progress_hook(d):
    """
    Callback function to track download progress in real-time.
    This function is passed to yt-dlp's 'progress_hooks' option.

    :param d: dict - Contains progress data from yt-dlp.
    """
    if d['status'] == 'downloading':
        # Extract progress details or use default values
        percentage = d.get('_percent_str', '0%').strip()  # Download percentage
        speed = d.get('_speed_str', 'N/A').strip()  # Download speed
        eta = d.get('_eta_str', 'N/A').strip()  # Estimated time remaining

        # Print progress information dynamically (overwrites previous line)
        print(f"\r⬇️ Downloading... {percentage} | Speed: {speed} | ETA: {eta}", end='\r', flush=True)

    elif d['status'] == 'finished':
        print("\n✅ Download complete!\n")  # Print a completion message when download is done
