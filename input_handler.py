from download_options import format_map, format_options  
from validation import validate_format_selection, validate_url  
from utils import format_supported_sites

def get_user_input(supported_sites):
    """
    Handles user input for URL, format selection, and output folder.
    Returns the user-selected values.
    """
    while True:
        url = input("Enter Video/Playlist URL (or ? for supported sites): ").strip()

        if url == "?":  
            print("\n🌍 Supported Websites:\n")
            print(format_supported_sites(supported_sites))  # Display formatted list in columns
            continue  # Restart input prompt if user requests site list

        try:
            validate_url(url, supported_sites)  # Validate user input
            break  # Exit loop when a valid URL is provided
        except ValueError as e:
            print(e)  # Print the error message
            continue  # Restart input prompt on invalid URL

    output_folder = input("Enter output folder (leave empty for 'downloads'): ").strip() or "downloads"

    print("\nChoose a format:")

    for text, tag in format_options:  
        print(f"{text.ljust(37)} {tag}")  # Aligns text for readability

    while True:  # Keep looping until a valid format is entered
        try:
            format_option = input("Enter format number: ").strip() or "1"
            validate_format_selection(format_option) 
            break  # Exit loop if valid format is entered
        except ValueError as e:
            print(e)  # Catch FFmpeg error and let the user pick again
            continue  # Restart format selection prompt
    
    selected_format = format_map[format_option]
    return url, selected_format, format_option, output_folder
