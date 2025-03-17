from utils import progress_hook 
import os  # For checking and creating output folder

# General yt-dlp options (used for all downloads)
BASE_YTDLP_OPTIONS = {
    'outtmpl': '%(title)s.%(ext)s',  # Default filename format
    'noplaylist': False,  # Explicitly allow downloading playlists
    'progress_hooks': [progress_hook],  # Attach progress tracking function
}

# MP3 conversion settings (used only if format_option == "5")
MP3_POSTPROCESSING = [{
    'key': 'FFmpegExtractAudio',  # Uses FFmpeg to extract audio
    'preferredcodec': 'mp3',  # Converts the extracted audio to MP3
    'preferredquality': '192'  # MP3 quality: 192kbps
}]

# Format selection menu for the user
format_options = [
    ("1 - Best quality (default)", "[📺 Video]"),
    ("2 - Best quality (audio only)", "[📺 Video (No Video Track)]"),
    ("3 - MP4", "[📺 Video]"),
    ("4 - WEBM", "[📺 Video]"),
    ("5 - Convert to MP3 (Requires FFmpeg)", "[🎵 Audio File]")
]

# Mapping of user selections to yt-dlp format strings
format_map = {
    "1": "best",  # Best quality (any format)
    "2": "bestaudio/best",  # Best quality (audio only)
    "3": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",  # MP4 format
    "4": "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]",  # WEBM format
    "5": "bestaudio/best"  # Best quality (audio only for MP3 conversion)
}

def get_yt_dlp_options(selected_format, output_folder, format_option):
    """
    Returns yt-dlp options based on user preferences.

    :param selected_format: str - The chosen download format.
    :param output_folder: str - The directory to save the downloaded file.
    :param format_option: str - The format number chosen by the user.
    :return: dict - yt-dlp options.
    """
    # Ensure the output folder exists before using it
    os.makedirs(output_folder, exist_ok=True)

    options = BASE_YTDLP_OPTIONS.copy()  # Start with base options

    # Update options dynamically based on user input
    options.update({
        'format': selected_format,
        'outtmpl': os.path.join(output_folder, BASE_YTDLP_OPTIONS['outtmpl']),  # Use dynamic folder
    })

    # If MP3 conversion is selected, add FFmpeg post-processing
    if format_option == "5":
        options['postprocessors'] = MP3_POSTPROCESSING

    return options  # Return the final yt-dlp options dictionary
