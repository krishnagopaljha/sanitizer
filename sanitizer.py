import os
import random
import string
import argparse

def logo():
    """Prints the custom logo and information banner."""
    print(r"""
  _____             _ _   _              
 / ____|           (_) | (_)             
| (___   __ _ _ __  _| |_ _ _______ _ __ 
 \___ \ / _` | '_ \| | __| |_  / _ \ '__|
 ____) | (_| | | | | | |_| |/ /  __/ |   
|_____/ \__,_|_| |_|_|\__|_/___\___|_| 

|--------------------------------------------------------------------|
| Created By: Krishna Gopal Jha                                      |
| Checkout my LinkedIn: https://www.linkedin.com/in/krishnagopaljha/ |
| Lookup at my insta: https://instagram.com/theindianpsych           |
|--------------------------------------------------------------------|
    """)

def generate_random_data(size):
    """Generate random data of the specified size."""
    return random.randbytes(size)

def secure_delete(file_path, passes=3):
    """Securely delete a file by overwriting, renaming, and then deleting it."""
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found")
        return
    
    # Get the size of the file
    file_size = os.path.getsize(file_path)
    
    # Overwrite the file with random data multiple times
    with open(file_path, "ba+", buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            f.write(generate_random_data(file_size))
    
    # Rename the file multiple times to destroy file metadata
    for _ in range(passes):
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
        file_path = new_path
    
    # Finally, delete the file
    os.remove(file_path)
    print(f"File {file_path} securely deleted")

def main():
    # Print the logo
    logo()
    
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Securely delete a file by overwriting, renaming, and deleting it.")
    parser.add_argument("file", type=str, help="The file to securely delete.")
    parser.add_argument("--passes", type=int, default=3, help="The number of passes for overwriting the file (default: 3).")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call secure delete function with provided arguments
    secure_delete(args.file, args.passes)

if __name__ == "__main__":
    main()
