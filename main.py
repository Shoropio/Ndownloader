import sys
import os
from PyQt6.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow
from utils.helpers import check_ffmpeg

def main():
    app = QApplication(sys.argv)
    
    if not check_ffmpeg():
        QMessageBox.warning(None, "FFmpeg Not Found", 
                            "FFmpeg is required for merging video/audio and downloading HLS streams.\n\n"
                            "Please install FFmpeg and add it to your PATH for full functionality.")
    
    app.setApplicationName("Ndownloader")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
