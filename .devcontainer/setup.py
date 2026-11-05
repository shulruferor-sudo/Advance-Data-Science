"""Prepare the repository-wide Jupyter workspace without executing research notebooks."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS = ROOT / ".devcontainer" / "requirements-codespaces.txt"
ASSIGNMENT = ROOT / "projects" / "Bureau of Statistics" / "Assignment_Solution.ipynb"

def main():
    if not REQUIREMENTS.is_file() or not ASSIGNMENT.is_file():
        raise FileNotFoundError("Repository files required for Codespaces setup are missing")

    subprocess.run(
        [sys.executable, "-m", "pip", "install", "--disable-pip-version-check", "-r", str(REQUIREMENTS)],
        cwd=ROOT, check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "ipykernel", "install", "--user",
         "--name", "advance-data-science", "--display-name", "Python 3 (Advance Data Science)"],
        cwd=ROOT, check=True,
    )
    print("Jupyter environment configured for the complete repository", flush=True)

if __name__ == "__main__":
    main()
