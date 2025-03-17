from download_options import format_map, format_options  
from validation import validate_format_selection, validate_url  
from utils import get_supported_sites 

def get_user_input():
    """
    Handles user input for URL, format selection, and output folder.
    Returns the user-selected values.
    """
    while True:
        url = input("Enter Video/Playlist URL (or ? for supported sites): ").strip()

        if url == "?":  
            print("\n🌍 Supported Websites:\n")
            print(get_supported_sites())  # Display supported sites list
            continue  # Restart input prompt after showing sites
        
        validate_url(url)  
        break  # Exit loop when valid URL is provided

    output_folder = input("Enter output folder (leave empty for 'downloads'): ").strip() or "downloads"

    print("\nChoose a format:")

    for text, tag in format_options:  
        print(f"{text.ljust(37)} {tag}")  # Aligns text for readability

    format_option = input("Enter format number: ").strip() or "1"

    validate_format_selection(format_option)
    
    selected_format = format_map[format_option]
    return url, selected_format, format_option, output_folder
