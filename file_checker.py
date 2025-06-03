import hashlib
import json
import os

# Function 1: Calculate the SHA-256 hash of a file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Function 2: Save hash of a file into hashes.json
def save_hash(file_path, hash_store="hashes.json"):
    file_hash = calculate_hash(file_path)

    # Load existing hashes if the file exists
    if os.path.exists(hash_store):
        with open(hash_store, "r") as f:
            hashes = json.load(f)
    else:
        hashes = {}

    # Add/update the hash
    hashes[file_path] = file_hash

    # Write the updated hashes back to file
    with open(hash_store, "w") as f:
        json.dump(hashes, f, indent=4)

    print(f"✅ Hash saved for '{file_path}'")

# Function 3: Check if file hash matches the stored ones

def verify_file(file_path, hash_store="hashes.json"):
    if not os.path.exists(hash_store):
        print("⚠ Error: hashes.json not found. Please save hashes first.")
        return

    with open(hash_store, "r") as f:
        hashes = json.load(f)

    current_hash = calculate_hash(file_path)
    saved_hash = hashes.get(file_path)

    if saved_hash is None:
        print(f"⚠ No saved hash found for {file_path}.")
    elif current_hash == saved_hash:
        print(f"✅ File '{file_path}' is safe and unchanged.")
    else:
        print(f"❌ ALERT: File '{file_path}' has been modified!")

# --------- Run One at a Time ---------
# Uncomment one of these to use:

# Step A: Save the original file hash
# save_hash("example.txt")

# Step B: Check if file is modified
verify_file("example.txt")
