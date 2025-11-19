import git
import os

# 👇 Change this to your repo folder
REPO_PATH = r"C:\Users\jonat\Documents\Mobile-Robots"


def main():
    repo = git.Repo(REPO_PATH)

    # Check if anything changed (including untracked files)
    if not repo.is_dirty(untracked_files=True):
        print("✅ No local changes to sync.")
        return

    print("🔍 Changes detected. Staging all (git add -A)...")
    repo.git.add(A=True)  # same as: git add -A

    # After staging, if index == HEAD, nothing to commit
    if not repo.is_dirty(untracked_files=False):
        print("ℹ️ Nothing new to commit after staging.")
        return

    default_msg = "Sync local changes"
    msg = input(f"Commit message [{default_msg}]: ").strip() or default_msg

    repo.index.commit(msg)
    print(f"✅ Committed with message: {msg!r}")

    origin = repo.remote(name="origin")
    branch = repo.active_branch.name

    print(f"⬇️ Pulling latest from origin/{branch} (may fail if conflicts)...")
    try:
        origin.pull(branch)
    except Exception as e:
        print("⚠️ Pull failed (maybe merge conflict). Details:")
        print(e)
        print("Fix conflicts manually, then run sync_repo.py again.")
        return

    print(f"⬆️ Pushing to origin/{branch}...")
    origin.push(branch)

    print(f"🚀 Repo synced with origin/{branch}")


if __name__ == "__main__":
    main()
#how to use: in terminal, navigate to the directory where this script is saved and run:
# python Auto Synvc.py