import yt_dlp  # For checking if FFmpeg is installed and getting supported sites

def get_supported_sites():
    """
    Fetches the list of supported websites from yt-dlp and formats them into multiple columns.

    :return: str - Formatted string containing the names of supported sites.
    """
    try:
        # Generate a list of all available extractors (site handlers)
        extractors = yt_dlp.extractor.gen_extractors()

        # Collect and sort site names, ensuring only valid ones are included
        sites = sorted(set(e.IE_NAME for e in extractors if hasattr(e, "IE_NAME")))

        col_width = 30  # Define fixed width for each column
        num_cols = 3  # Number of columns in the output display
        formatted_sites = ""  # Initialize the output string

        # Iterate through the site names and format them into columns
        for i, site in enumerate(sites, 1):
            formatted_sites += site.ljust(col_width)  # Align site names evenly
            if i % num_cols == 0:  # Insert a new line after every 'num_cols' entries
                formatted_sites += "\n"

        return formatted_sites.strip() 
    except Exception as e:
        # Handle any errors encountered during site retrieval
        return f"⚠️ Error fetching sites: {e}"


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
