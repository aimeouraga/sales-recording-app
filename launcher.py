import subprocess
import sys
import os
import time
import webbrowser

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            os.path.join(base_dir, "🚀_Application.py"),
            "--server.headless=true",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True
    )

    time.sleep(5)  # Wait for the server to start

    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    main()
