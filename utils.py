import yt_dlp  # For checking if FFmpeg is installed and getting supported sites
import sys  # For low-level output handling
import time  # For adding delays to simulate typewriter-style printing

def print_ascii_art():
    """
    Prints an ASCII banner when the program starts.
    """
    ascii_art = """                                                                                          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠯⠿⠟⢹⣇⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⡀⠀⢀⣠⣤⢿⣭⠛⠲⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠞⠁⢰⡞⠁⠀⠈⠀⠀⠀⠛⢁⣀⣚⡲⢤⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠉⠓⢦⣄⠀⠀⠀⣠⠞⠛⠛⠛⠛⠀⠙⢷⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣴⠞⢁⡄⠀⠀⢀⣤⣤⣶⣶⣍⠳⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠁⠀⢀⣠⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⣴⣿⠀⣠⠀⠀⠀⠀⠴⠛⠋⠁⠿⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠛⠁⠀⠀⠀⢰⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡧⠀⠀⠀⠠⣶⡶⠾⢿⣿⣶⣽⡳⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⡀⠀⠀⠀⠴⠞⠛⠋⠉⠀⣸⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡿⠃⠀⠀⠀⠀⣤⣤⣶⣶⣶⣤⡙⢦⡀
⠀⠀⠀⠀⠀⢀⣤⠖⠋⠁⠠⠤⠖⠒⠂⠀⠈⠓⠒⠒⠶⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⢀⠤⠄⠈⠙⠁⢠⡗
⠀⠀⣀⣤⣾⣋⣠⣀⣀⣠⣤⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⠟⠙⣳⣤⣤⣀⣈⣷
⠀⠾⣭⡥⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣉⣉⠉⠉⠉⠛⠒⠒⠒⠲⠶⠶⠶⠒⠒⠒⠒⠋⠉⠉⠙⠓⠶⠦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠖⠛⠉⠀⠀⠀⠈⣿
⢀⡞⠁⢀⡄⡙⢿⡟⠉⠙⢿⣿⡿⠿⡛⠛⢿⣿⡷⠒⠒⠲⣤⣤⣤⣤⣀⣤⣤⣤⣶⣦⣤⣀⡀⠀⣀⣀⣀⣀⣀⡉⠉⠉⠛⠛⠛⠿⠖⠚⠉⠉⠁⠀⠀⠀⠀⠀⠀⢀⣠⡶⠋
⢸⡇⠀⠘⠲⣵⠈⣷⠀⠀⢸⡏⠀⠀⢳⢇⢸⡏⠀⠀⠀⠀⢹⡿⠋⠀⠀⠀⠀⠀⠹⣧⣉⣿⠉⠉⠉⠉⢉⣉⡉⠙⣿⣿⠓⠒⠲⠶⠶⠶⢶⣦⡄⠀⠀⢀⡼⠒⠒⠋⠁
⠘⢧⣄⣀⣀⣠⡾⠃⠀⠀⣸⡇⠀⠀⠈⠉⣼⠃⠀⣀⣠⡀⣿⡁⠀⠀⠶⣶⡄⠀⠀⢸⣿⣇⠀⠀⠀⠀⠚⢦⣹⢀⣿⣿⡀⠀⠀⠀⠀⠀⢠⡿⠁⣠⡴⠋
⠀⢀⣿⡿⢋⣉⠛⢷⣦⣴⣿⣧⣀⠀⣀⣰⡇⠀⠘⠣⠼⣤⣿⣷⣄⣀⠀⠈⠁⠀⣠⡿⠃⠻⣦⣀⠀⠀⠀⣀⣿⣿⠏⠈⠻⠶⠤⠤⣤⣴⡟⠁⣰⠏⠀⠀⠀⠀⠀
⠀⣼⢻⡀⡎⣟⠀⠀⢙⣿⠟⠛⠛⠛⠛⡙⠻⠶⣤⣤⡞⠋⠁⠀⠈⠙⢳⣦⣠⣴⡯⢤⣤⣀⡀⢉⣿⣿⣟⠛⠛⣿⣄⠀⠀⠀⠀⢀⣼⠏⢀⡴⠁⠀⠀⠀⠀⠀
⠀⣿⣌⣧⡈⠁⠀⠀⢹⣯⠀⠀⠀⠶⣉⡇⠀⣰⠛⣿⣄⠀⠀⠀⠀⠀⢀⣿⠏⠀⠀⠀⠠⡌⡙⢿⣿⠈⠉⠀⠀⠈⠙⠓⣶⣤⣴⠟⠁⢠⠟⠁⠀⠀⠀⠀⠀
⠀⠳⠼⠭⣟⣓⣒⣛⠛⠛⢷⡀⠀⠀⠀⣠⠾⢅⣀⣨⠽⠷⠲⠤⠤⠴⣾⣯⣀⠀⠀⠀⠀⠃⢃⣼⣿⣄⡀⠀⠀⠀⢀⣰⣿⡿⠁⣠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠻⣅⢀⣚⣿⠖⠒⠒⠲⠶⠤⠤⠤⠤⠤⠤⠤⠾⣏⠀⠀⠀⢶⣏⣉⣉⣉⣉⣉⣉⣉⣉⣉⣁⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣒⣋⣀⣀⣠⠖⠛⠛⠀⠀⠀⠀⠀⠀⠉⠉

Python Internet Extractor. Press Ctrl+C to exit the program."""

    for char in ascii_art:
        sys.stdout.write(char)  # Print character without newline
        sys.stdout.flush()  # Force immediate output
        time.sleep(0.001)  # Delay for slow printing 

    print("\n")  # Move to the next line after ASCII art is fully printed

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
        print("⚠️  WARNING: FFmpeg not found.")
        print("   - The downloaded format may not be the best available.")
        print("   - FFmpeg is required for converting videos to MP3.")
        print("   - 🔗 Official FFmpeg Download: https://ffmpeg.org/download.html\n")

def progress_hook(d):
    """
    Displays a real-time progress bar.

    :param d: dict - Contains progress data from yt-dlp.
    """
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes', 0) or d.get('total_bytes_estimate', 0)
        downloaded = d.get('downloaded_bytes', 0)
        percentage = d.get('_percent_str', '0%').strip()  # Get percentage string
        speed = d.get('_speed_str', 'N/A').strip()  # Download speed
        eta = d.get('_eta_str', 'N/A').strip()  # Estimated time remaining

        # Define progress bar length
        bar_length = 30

        if total_size:
            # Calculate the number of blocks to display
            filled_blocks = int((downloaded / total_size) * bar_length)
            empty_blocks = bar_length - filled_blocks
            progress_bar = "█" * filled_blocks + "-" * empty_blocks
        else:
            progress_bar = "-" * bar_length  # If total size unknown, show empty bar

        # Print progress bar dynamically (overwrites previous output)
        sys.stdout.write(f"\r{percentage} | {progress_bar} | Speed: {speed} | ETA: {eta}")
        sys.stdout.flush()

    elif d['status'] == 'finished':
        print("\n✅ Download complete!\n")  # Print a completion message when the download is done