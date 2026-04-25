import shutil
import subprocess
import os
import sys

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_ffmpeg_path():
    """Return the path to the ffmpeg executable."""
    # 1. Check if internal ffmpeg exists (for bundled app)
    internal_path = get_resource_path(os.path.join("bin", "ffmpeg.exe"))
    if os.path.exists(internal_path):
        return internal_path
    
    # 2. Check if it's in the bin folder relative to the script
    local_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bin", "ffmpeg.exe")
    if os.path.exists(local_path):
        return local_path

    # 3. Fallback to system PATH
    return shutil.which("ffmpeg")

def check_ffmpeg():
    """Check if ffmpeg is available internally or in the system PATH."""
    return get_ffmpeg_path() is not None

def get_ffmpeg_version():
    ffmpeg_path = get_ffmpeg_path()
    if not ffmpeg_path:
        return "Not found"
    try:
        result = subprocess.run([ffmpeg_path, "-version"], capture_output=True, text=True, check=True)
        return result.stdout.splitlines()[0]
    except:
        return "Error getting version"
