import os
import requests
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QPushButton, QFrame
from PyQt6.QtCore import Qt, pyqtSignal, QThread, pyqtSlot
from PyQt6.QtGui import QPixmap, QImage

class ThumbnailWorker(QThread):
    loaded = pyqtSignal(QImage)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                image = QImage()
                image.loadFromData(response.content)
                self.loaded.emit(image)
        except:
            pass

class DownloadItem(QWidget):
    cancel_requested = pyqtSignal()
    pause_requested = pyqtSignal()
    open_requested = pyqtSignal()

    def __init__(self, title, url, thumbnail_url=None, source_domain=None, parent=None):
        super().__init__(parent)
        self.setObjectName("DownloadItem")
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(16, 16, 16, 16)
        self.layout.setSpacing(20)

        # Thumbnail
        self.thumb_label = QLabel()
        self.thumb_label.setFixedSize(140, 80)
        self.thumb_label.setObjectName("Thumbnail")
        self.thumb_label.setStyleSheet("background-color: #0A0C10; border-radius: 0px;")
        self.thumb_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.thumb_label)

        if thumbnail_url:
            self.thumb_worker = ThumbnailWorker(thumbnail_url)
            self.thumb_worker.loaded.connect(self.set_thumbnail)
            self.thumb_worker.start()
        else:
            self.thumb_label.setText("No Image")

        # Info & Progress Container
        info_container = QWidget()
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(4)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("ItemTitle")
        self.title_label.setWordWrap(True)
        info_layout.addWidget(self.title_label)

        source_text = f"Source: {source_domain}" if source_domain else "Source: Unknown"
        self.source_label = QLabel(source_text)
        self.source_label.setObjectName("SecondaryLabel")
        info_layout.addWidget(self.source_label)

        self.stats_label = QLabel("Waiting...")
        self.stats_label.setObjectName("SecondaryLabel")
        info_layout.addWidget(self.stats_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        info_layout.addWidget(self.progress_bar)

        # Actions Row
        actions_hbox = QHBoxLayout()
        actions_hbox.setSpacing(10)
        
        self.pause_btn = QPushButton("Pause")
        self.pause_btn.setObjectName("secondary")
        self.pause_btn.setFixedSize(85, 32)
        self.pause_btn.clicked.connect(self.pause_requested.emit)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setObjectName("secondary")
        self.cancel_btn.setFixedSize(85, 32)
        self.cancel_btn.setStyleSheet("color: #EF4444;")
        self.cancel_btn.clicked.connect(self.cancel_requested.emit)

        self.open_btn = QPushButton("Open")
        self.open_btn.setObjectName("secondary")
        self.open_btn.setFixedSize(85, 32)
        self.open_btn.clicked.connect(self.open_requested.emit)
        self.open_btn.hide() # Hidden until finished

        actions_hbox.addWidget(self.pause_btn)
        actions_hbox.addWidget(self.cancel_btn)
        actions_hbox.addWidget(self.open_btn)
        actions_hbox.addStretch()
        
        info_layout.addLayout(actions_hbox)
        self.layout.addWidget(info_container, 1)

    @pyqtSlot(QImage)
    def set_thumbnail(self, image):
        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(self.thumb_label.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.thumb_label.setPixmap(scaled_pixmap)

    def update_progress(self, data):
        if 'percentage' in data:
            try:
                p_str = data.get('_percent_str', '0%').replace('%', '').strip()
                p_val = int(float(p_str))
                self.progress_bar.setValue(p_val)
                
                # Update stats string
                speed = data.get('_speed_str', 'N/A')
                eta = data.get('_eta_str', 'N/A')
                size = data.get('_total_bytes_str', data.get('_total_bytes_estimate_str', 'N/A'))
                
                self.stats_label.setText(f"{p_val}% downloaded | {speed} | {eta} remaining")
            except:
                pass

    def set_status(self, status, color=None):
        self.stats_label.setText(status)
        if color:
            self.stats_label.setStyleSheet(f"color: {color}; font-size: 12px;")
        
        if "Finished" in status or "Done" in status:
            self.pause_btn.hide()
            self.cancel_btn.hide()
            self.open_btn.show()
            self.progress_bar.setStyleSheet("QProgressBar::chunk { background-color: #22C55E; }")
        elif "Error" in status:
            self.progress_bar.setStyleSheet("QProgressBar::chunk { background-color: #EF4444; }")
        elif "Pause" in status:
            self.progress_bar.setStyleSheet("QProgressBar::chunk { background-color: #FACC15; }")
