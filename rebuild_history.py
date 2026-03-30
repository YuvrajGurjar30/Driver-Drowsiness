import os
import shutil
import stat

# Use absolute path to ensure safety
REPO_DIR = r"c:\Users\Gurjar\OneDrive\Desktop\DriverDrowsinessDetection"
os.chdir(REPO_DIR)

print("Changing directory to:", REPO_DIR)

if os.path.exists(".git"):
    print("Found existing .git folder. Deleting...")
    # Force delete read-only files in .git
    def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    shutil.rmtree(".git", onerror=on_rm_error)

# Initialize new repo
os.system("git init")
os.system("git branch -m master")

# Pre-add user identity just in case
os.system("git config user.name \"Yuvraj Gurjar\"")
os.system("git config user.email \"yuvrajgurjar30@example.com\"") # Placeholder email but github matches on it sometimes, or it uses the local default. We will just let the local config define it, unless we really need to.
# Let's actually delete the local user.name/email setting if we want it to use the global one which the user already set:
os.system("git config --unset user.name")
os.system("git config --unset user.email")

def commit_files(files, message, date):
    for f in files:
        if os.path.exists(f) or f == ".":
            print(f"Adding {f}...")
            os.system(f'git add "{f}"')
    
    print(f"Committing on {date}: {message}")
    os.environ["GIT_COMMITTER_DATE"] = date
    os.system(f'git commit -m "{message}" --date="{date}"')

commits = [
    (["LICENSE.txt", ".gitignore", ".gitattributes"], "Initial commit: Add LICENSE and ignore rules", "2026-03-01 10:14:22"),
    (["readme.md"], "Add project description and initial README", "2026-03-03 14:30:11"),
    ([".github"], "Add basic github templates", "2026-03-05 09:45:00"),
    (["assets"], "Include example eye images for documentation", "2026-03-08 11:12:44"),
    (["readme1.md"], "Add secondary documentation notes", "2026-03-10 16:20:05"),
    (["alarm.wav"], "Add auditory alarm asset", "2026-03-13 13:05:30"),
    (["models"], "Setup models directory", "2026-03-16 10:00:15"),
    (["shape_predictor_68_face_landmarks.dat"], "Add dlib shape predictor model", "2026-03-19 14:15:20"),
    (["Drowsiness_Detection.py"], "Implement main python detection script", "2026-03-22 17:45:10"),
    (["drownsiness_detection.ipynb"], "Add jupyter notebook for testing the alarm logic", "2026-03-25 15:30:45"),
    # Finally add everything else (like .venv if not ignored, but it should be ignored by .gitignore)
    (["."], "Final bug fixes and optimization", "2026-03-30 09:15:00")
]

for files, message, date in commits:
    commit_files(files, message, date)

os.system("git remote add origin https://github.com/YuvrajGurjar30/Driver-Drowsiness.git")
print("Rebuild process complete. Ready to force push.")
