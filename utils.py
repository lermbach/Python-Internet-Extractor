import yt_dlp  # For checking if FFmpeg is installed
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