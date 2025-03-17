from core import download
from input_handler import get_user_input
from utils import show_ffmpeg_warning, get_supported_sites
import sys  # To handle system exit on errors

# Fetch the supported sites when the program starts
SUPPORTED_SITES = get_supported_sites()

print("\nPress Ctrl+C to exit the program.\n")  

def main():
    """
    Main script execution loop.
    Continuously runs until the user exits with Ctrl+C.
    
    - Displays FFmpeg warning (if applicable).
    - Gets user input (URL, format, output folder).
    - Calls the download function with user-selected options.
    - Catches and displays errors to prevent crashes.
    """
    while True: 
        try:
            # Get user input (URL, format, output folder)
            url, selected_format, format_option, output_folder = get_user_input(SUPPORTED_SITES)
            # Start the download process with the selected options
            download(url, selected_format, format_option, output_folder)
        except KeyboardInterrupt:
            # Handle user interrupt (Ctrl + C)
            print("\n\nProgram Exited...\n")
            sys.exit(0)  # Exit with status code 0 (normal termination) 
        except Exception as e:
            # Catch any unexpected errors and display the message
            print(f"\n❌ Unexpected Error: {e}")
            sys.exit(1)  # Exit with status code 1 (indicates failure)

if __name__ == "__main__":
    show_ffmpeg_warning()  # Display warning if FFmpeg is missing
    main()  # Start the main execution flow
