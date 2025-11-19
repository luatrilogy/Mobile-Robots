import git
import os

repo_path = r"C:\Users\jonat\Documents\Mobile-Robots"  # your repo directory
file_to_add = os.path.join(repo_path, "Testing.py")  # file to add

# --- Create the file (example) ---
with open(file_to_add, "w") as f:
    f.write("This is a test file added from Python.\n")

# --- Open repo ---
repo = git.Repo(repo_path)

# --- Add file ---
repo.git.add(file_to_add)

# --- Commit ---
repo.index.commit("Add testfile.txt from Python")

# --- Push to GitHub ---
origin = repo.remote(name="origin")
origin.push()
