import hashlib
import os
import json

def calculate_hash(filepath):
    """Calculates the SHA-256 hash of a file."""
    try:
        with open(filepath, "rb") as file:
            file_content = file.read()
            file_hash = hashlib.sha256(file_content).hexdigest()
            return file_hash
    except FileNotFoundError:
        return None  # Return None if the file is not found

def check_integrity(filepath, original_hash):
    """Compares the current hash with the original hash."""
    current_hash = calculate_hash(filepath)
    if current_hash is None:
        return "Error: File not found. Cannot check integrity."
    elif current_hash == original_hash:
        return "File integrity verified. No changes detected."
    else:
        return "File integrity compromised! Changes detected."

def load_hashes(filename="file_hashes.json"):
    """Loads file hashes from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_hashes(hashes, filename="file_hashes.json"):
    """Saves file hashes to a JSON file."""
    with open(filename, "w") as f:
        json.dump(hashes, f, indent=4)  # Use indent for better readability

def monitor_file(filepath):
    """Monitors a single file for changes."""

    hashes = load_hashes()  # Load existing hashes

    if filepath not in hashes:
        # First run: Calculate and store the initial hash
        original_hash = calculate_hash(filepath)
        if original_hash is not None:
            hashes[filepath] = original_hash
            save_hashes(hashes)  # Save the hash immediately
            print(f"Stored original hash for {filepath}.")
        else:
            print(f"Error: Could not calculate hash for {filepath}.")
            return  # Exit the function if hash calculation fails
    else:
        # Subsequent runs: Check for changes
        original_hash = hashes[filepath]
        result = check_integrity(filepath, original_hash)
        print(f"{filepath}: {result}")

# Example Usage (Replace with your file path)
file_to_monitor = "my_document.txt"
monitor_file(file_to_monitor)