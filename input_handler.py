from download_options import format_map, format_options  
from validation import validate_format_selection, validate_url  
import os  # For handling file paths

def get_user_input():
    """
    Handles user input for URL, format selection, and output folder.
    Returns the user-selected values.
    """
    while True:
        url = input("Enter Video/Playlist URL: ").strip()

        try:
            validate_url(url)  # Validate user input
            break  # Exit loop when a valid URL is provided
        except ValueError as e:
            print(e)  # Print the error message
            continue  # Restart input prompt on invalid URL

    # Default output folder is the user's Downloads folder
    default_output_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Allow user to enter a custom path
    output_folder = input(f"Enter output folder path (leave empty for '{default_output_folder}'): ").strip()

    # If blank, use the default Downloads folder
    if not output_folder:
        output_folder = default_output_folder

    # Expand user path (~) and convert relative paths to absolute paths
    output_folder = os.path.abspath(os.path.expanduser(output_folder))

    print(f"\nOutput Folder Set To: {output_folder}")  # Inform the user

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
