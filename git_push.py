import subprocess
import os

os.chdir(r"D:\User\Y0ungK1ng\projects\ForSignal")

def run(cmd):
    print(f"> {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.stdout: print(r.stdout)
    if r.stderr: print(r.stderr)
    if r.returncode != 0:
        print(f"⚠️  Exit code: {r.returncode}")
    return r

# Check status
run(["git", "status"])

# Add all files
run(["git", "add", "."])

# Check what's staged
run(["git", "diff", "--staged", "--stat"])

# Commit
run(["git", "commit", "-m", "add dashboard and server"])

# Push
run(["git", "push"])

print("Done!")
