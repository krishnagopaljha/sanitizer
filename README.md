# Sanitizer

**Sanitizer** is a Python command-line tool designed to securely delete files by overwriting their contents multiple times, renaming them, and finally deleting them. This ensures that the original data is irretrievable, even with forensic tools.

## Features

- **Multi-Pass Overwriting:** Overwrite the file with random data multiple times.
- **File Renaming:** Rename the file with random strings to destroy metadata.
- **Final Deletion:** Securely delete the file from the filesystem after overwriting and renaming.
- **Customizable Passes:** Specify the number of overwrite passes for increased security.

## Installation

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/yourusername/Sanitizer.git
   cd Sanitizer
