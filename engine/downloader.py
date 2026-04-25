import yt_dlp
import os
import threading
from PyQt6.QtCore import QObject, pyqtSignal
from utils.helpers import get_ffmpeg_path

class DownloadSignals(QObject):
    progress = pyqtSignal(dict)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    info_received = pyqtSignal(dict)

class DownloadCancelled(Exception):
    pass

class Downloader:
    def __init__(self):
        self.signals = DownloadSignals()
        self._stop_event = threading.Event()

    def get_info(self, url):
        """Fetch video information without downloading."""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                self.signals.info_received.emit(info)
                return info
        except Exception as e:
            self.signals.error.emit(str(e))
            return None

    def download(self, url, options):
        def progress_hook(d):
            if self._stop_event.is_set():
                raise DownloadCancelled("Download cancelled by user")
            
            if d['status'] == 'downloading':
                self.signals.progress.emit(d)
            elif d['status'] == 'finished':
                self.signals.finished.emit(d['filename'])

        ffmpeg_path = get_ffmpeg_path()
        if ffmpeg_path:
            # yt-dlp expects the path to the directory containing ffmpeg or the path to ffmpeg itself
            # If it's a full path to the exe, we should use its directory
            options['ffmpeg_location'] = os.path.dirname(ffmpeg_path)

        ydl_opts = {
            'progress_hooks': [progress_hook],
            **options
        }

        # Ensure we can stop
        if self._stop_event.is_set():
            return

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except DownloadCancelled:
            self.signals.error.emit("Cancelled")
        except Exception as e:
            self.signals.error.emit(str(e))

    def stop(self):
        self._stop_event.set()
