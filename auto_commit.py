import git
import os
import sys

# 👇 Change this to the folder where your repo lives
REPO_PATH = r"C:\Users\jonat\Documents\Mobile-Robots"


def main():
    if len(sys.argv) < 2:
        print("Usage: python add_one_file.py <path/to/file>")
        sys.exit(1)

    file_arg = sys.argv[1]

    # If they gave a relative path, make it relative to the repo
    if not os.path.isabs(file_arg):
        file_path = os.path.join(REPO_PATH, file_arg)
    else:
        file_path = file_arg

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    repo = git.Repo(REPO_PATH)

    # Stage the file
    repo.git.add(file_path)
    print(f"✅ Staged: {file_path}")

    # Commit message
    default_msg = f"Add {os.path.basename(file_path)}"
    msg = input(f"Commit message [{default_msg}]: ").strip() or default_msg

    repo.index.commit(msg)
    print(f"✅ Committed with message: {msg!r}")

    # Push to current branch
    origin = repo.remote(name="origin")
    branch = repo.active_branch.name
    origin.push(branch)
    print(f"🚀 Pushed to origin/{branch}")


if __name__ == "__main__":
    main()

#how to use: in terminal, navigate to the directory where this script is saved and run:
# python Auto Commit.py <path/to/file>
