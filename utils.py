import yt_dlp  # For checking if FFmpeg is installed 

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
