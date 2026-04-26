import os
import sys
import subprocess
from urllib.parse import urlparse
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QComboBox, 
                             QFileDialog, QScrollArea, QFrame, QTextEdit, QApplication, 
                             QTabWidget, QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal, QSize
from PyQt6.QtGui import QClipboard, QIcon, QPixmap

from engine.downloader import Downloader, DownloadSignals
from ui.styles import DARK_STYLE, LIGHT_STYLE
from ui.widgets.download_item import DownloadItem
from utils.config import load_config, save_config, add_to_history, load_history
from utils.helpers import get_resource_path

TRANSLATIONS = {
    "es": {
        "title": "Ndownloader",
        "url_placeholder": "Pega un enlace de YouTube, Twitter, m3u8...",
        "add_queue": "Añadir descarga",
        "paste_clip": "Pegar desde portapapeles",
        "save_to": "Carpeta:",
        "browse": "Buscar",
        "format": "Formato:",
        "quality": "Calidad:",
        "tab_queue": "Cola",
        "tab_completed": "Completadas",
        "tab_errors": "Errores",
        "tab_logs": "Registro",
        "logs_placeholder": "Los registros aparecerán aquí...",
        "fetching": "Obteniendo información...",
        "copyright": "© 2026 Shoropio Corporation. Todos los derechos reservados.",
        "best": "Mejor",
        "video": "Video (MP4)",
        "audio": "Audio (MP3)"
    },
    "en": {
        "title": "Ndownloader",
        "url_placeholder": "Paste a link from YouTube, Twitter, m3u8...",
        "add_queue": "Add download",
        "paste_clip": "Paste from clipboard",
        "save_to": "Folder:",
        "browse": "Browse",
        "format": "Format:",
        "quality": "Quality:",
        "tab_queue": "Queue",
        "tab_completed": "Completed",
        "tab_errors": "Errors",
        "tab_logs": "Logs",
        "logs_placeholder": "Logs will appear here...",
        "fetching": "Fetching info...",
        "copyright": "© 2026 Shoropio Corporation. All rights reserved.",
        "best": "Best",
        "video": "Video (MP4)",
        "audio": "Audio (MP3)"
    }
}

class InfoWorker(QThread):
    info_received = pyqtSignal(dict)
    error = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            import yt_dlp
            ydl_opts = {'quiet': True, 'noplaylist': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                self.info_received.emit(info)
        except Exception as e:
            self.error.emit(str(e))

class DownloadWorker(QThread):
    progress = pyqtSignal(dict)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, url, options):
        super().__init__()
        self.url = url
        self.options = options
        self.downloader = Downloader()

    def run(self):
        self.downloader.signals.progress.connect(self.progress.emit)
        self.downloader.signals.finished.connect(self.finished.emit)
        self.downloader.signals.error.connect(self.error.emit)
        self.downloader.download(self.url, self.options)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.lang = self.config.get("language", "es")
        self.theme = self.config.get("theme", "dark")
        
        self.setWindowTitle("Ndownloader")
        self.setMinimumSize(950, 750)
        
        # Window Icon
        logo_path = get_resource_path(os.path.join("assets", "logo.png"))
        if os.path.exists(logo_path):
            self.setWindowIcon(QIcon(logo_path))
            
        self.apply_theme()

        self.downloads = {} # url -> widget
        self.init_ui()
        
        self.path_input.setText(self.config["output_path"])

        self.clipboard = QApplication.clipboard()
        self.last_clipboard = ""
        self.clipboard_timer = QTimer()
        self.clipboard_timer.timeout.connect(self.check_clipboard)
        self.clipboard_timer.start(1000)

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def apply_theme(self):
        if self.theme == "dark":
            self.setStyleSheet(DARK_STYLE)
        else:
            self.setStyleSheet(LIGHT_STYLE)

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.config["theme"] = self.theme
        save_config(self.config)
        self.apply_theme()
        self.theme_btn.setText("LIGHT" if self.theme == "dark" else "DARK")

    def toggle_lang(self):
        self.lang = "en" if self.lang == "es" else "es"
        self.config["language"] = self.lang
        save_config(self.config)
        self.refresh_ui_text()

    def refresh_ui_text(self):
        self.title_label.setText(self.t("title"))
        self.url_input.setPlaceholderText(self.t("url_placeholder"))
        self.download_btn.setText(self.t("add_queue"))
        self.paste_btn.setText(self.t("paste_clip"))
        self.path_label.setText(self.t("save_to"))
        self.path_btn.setText(self.t("browse"))
        self.format_label.setText(self.t("format"))
        self.quality_label.setText(self.t("quality"))
        self.copyright_label.setText(self.t("copyright"))
        self.lang_btn.setText("EN" if self.lang == "es" else "ES")
        
        # Tabs
        self.tabs.setTabText(0, self.t("tab_queue"))
        self.tabs.setTabText(1, self.t("tab_completed"))
        self.tabs.setTabText(2, self.t("tab_errors"))
        self.tabs.setTabText(3, self.t("tab_logs"))

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 1. Top Bar
        top_bar = QWidget()
        top_bar.setObjectName("TopBar")
        top_bar.setMinimumHeight(64)
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(20, 0, 20, 0)

        # Logo & Title
        self.logo_label = QLabel()
        logo_path = get_resource_path(os.path.join("assets", "logo.png"))
        if os.path.exists(logo_path):
            pix = QPixmap(logo_path).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.logo_label.setPixmap(pix)
        top_layout.addWidget(self.logo_label)

        self.title_label = QLabel(self.t("title"))
        self.title_label.setObjectName("TitleLabel")
        top_layout.addWidget(self.title_label)
        top_layout.addStretch()

        # Action Buttons
        self.lang_btn = QPushButton("ES" if self.lang == "en" else "EN")
        self.lang_btn.setObjectName("secondary")
        self.lang_btn.setFixedSize(50, 36)
        self.lang_btn.clicked.connect(self.toggle_lang)
        
        self.theme_btn = QPushButton("LIGHT" if self.theme == "dark" else "DARK")
        self.theme_btn.setObjectName("secondary")
        self.theme_btn.setFixedSize(60, 36)
        self.theme_btn.clicked.connect(self.toggle_theme)

        top_layout.addWidget(self.lang_btn)
        top_layout.addWidget(self.theme_btn)
        main_layout.addWidget(top_bar)

        # 2. Main Content
        content_container = QWidget()
        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(30, 30, 30, 10)
        content_layout.setSpacing(25)

        # Input Card
        input_card = QFrame()
        input_card.setObjectName("InputCard")
        card_layout = QVBoxLayout(input_card)
        card_layout.setContentsMargins(25, 25, 25, 25)
        card_layout.setSpacing(20)

        # No shadows per user request (strict minimalist)
        # input_card.setGraphicsEffect(None)

        # URL Row
        url_hbox = QHBoxLayout()
        url_hbox.setSpacing(12)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText(self.t("url_placeholder"))
        self.url_input.setMinimumHeight(48)
        
        self.download_btn = QPushButton(self.t("add_queue"))
        self.download_btn.setMinimumHeight(48)
        self.download_btn.setFixedWidth(160)
        self.download_btn.clicked.connect(self.add_download)

        self.paste_btn = QPushButton(self.t("paste_clip"))
        self.paste_btn.setObjectName("secondary")
        self.paste_btn.setMinimumHeight(48)
        self.paste_btn.clicked.connect(self.paste_from_clipboard)

        url_hbox.addWidget(self.url_input, 1)
        url_hbox.addWidget(self.paste_btn)
        url_hbox.addWidget(self.download_btn)
        card_layout.addLayout(url_hbox)

        # Options Row
        options_hbox = QHBoxLayout()
        options_hbox.setSpacing(15)

        # Save to
        self.path_label = QLabel(self.t("save_to"))
        self.path_label.setObjectName("SecondaryLabel")
        self.path_input = QLineEdit()
        self.path_input.setReadOnly(True)
        self.path_input.setMinimumHeight(40)
        self.path_btn = QPushButton(self.t("browse"))
        self.path_btn.setObjectName("secondary")
        self.path_btn.setFixedSize(90, 40)
        self.path_btn.clicked.connect(self.browse_folder)

        options_hbox.addWidget(self.path_label)
        options_hbox.addWidget(self.path_input, 1)
        options_hbox.addWidget(self.path_btn)

        # Format
        self.format_label = QLabel(self.t("format"))
        self.format_label.setObjectName("SecondaryLabel")
        self.format_combo = QComboBox()
        self.format_combo.setFixedSize(130, 40)
        self.format_combo.addItems([self.t("video"), self.t("audio")])
        options_hbox.addWidget(self.format_label)
        options_hbox.addWidget(self.format_combo)

        # Quality
        self.quality_label = QLabel(self.t("quality"))
        self.quality_label.setObjectName("SecondaryLabel")
        self.quality_combo = QComboBox()
        self.quality_combo.setFixedSize(110, 40)
        self.quality_combo.addItems([self.t("best"), "1080p", "720p", "480p"])
        options_hbox.addWidget(self.quality_label)
        options_hbox.addWidget(self.quality_combo)

        card_layout.addLayout(options_hbox)
        content_layout.addWidget(input_card)

        # 3. Tabs
        self.tabs = QTabWidget()
        
        # Queue Tab
        self.queue_scroll = QScrollArea()
        self.queue_scroll.setWidgetResizable(True)
        self.queue_content = QWidget()
        self.queue_layout = QVBoxLayout(self.queue_content)
        self.queue_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.queue_scroll.setWidget(self.queue_content)
        self.tabs.addTab(self.queue_scroll, self.t("tab_queue"))

        # Completed Tab
        self.done_scroll = QScrollArea()
        self.done_scroll.setWidgetResizable(True)
        self.done_content = QWidget()
        self.done_layout = QVBoxLayout(self.done_content)
        self.done_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.done_scroll.setWidget(self.done_content)
        self.tabs.addTab(self.done_scroll, self.t("tab_completed"))

        # Errors Tab
        self.error_scroll = QScrollArea()
        self.error_scroll.setWidgetResizable(True)
        self.error_content = QWidget()
        self.error_layout = QVBoxLayout(self.error_content)
        self.error_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.error_scroll.setWidget(self.error_content)
        self.tabs.addTab(self.error_scroll, self.t("tab_errors"))

        # Logs Tab
        self.log_panel = QTextEdit()
        self.log_panel.setObjectName("LogPanel")
        self.log_panel.setReadOnly(True)
        self.log_panel.setPlaceholderText(self.t("logs_placeholder"))
        self.tabs.addTab(self.log_panel, self.t("tab_logs"))

        content_layout.addWidget(self.tabs)
        main_layout.addWidget(content_container, 1)

        # Footer
        footer = QWidget()
        footer.setFixedHeight(40)
        footer_layout = QHBoxLayout(footer)
        self.copyright_label = QLabel(self.t("copyright"))
        self.copyright_label.setObjectName("Footer")
        footer_layout.addStretch()
        footer_layout.addWidget(self.copyright_label)
        footer_layout.addStretch()
        main_layout.addWidget(footer)

    def paste_from_clipboard(self):
        text = self.clipboard.text()
        if text.startswith("http"):
            self.url_input.setText(text)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.t("browse"))
        if folder:
            self.path_input.setText(folder)
            self.config["output_path"] = folder
            save_config(self.config)

    def log(self, message):
        self.log_panel.append(message)

    def check_clipboard(self):
        text = self.clipboard.text()
        if text != self.last_clipboard and (text.startswith("http://") or text.startswith("https://")):
            self.last_clipboard = text
            if not self.url_input.text():
                self.url_input.setText(text)

    def add_download(self):
        url = self.url_input.text().strip()
        if not url or url in self.downloads:
            return

        self.log(f"{self.t('fetching')} {url}")
        self.download_btn.setEnabled(False)
        
        worker = InfoWorker(url)
        worker.info_received.connect(lambda info: self.start_download(url, info))
        worker.error.connect(lambda err: self.on_info_error(url, err))
        worker.finished.connect(lambda: self.download_btn.setEnabled(True))
        self.info_worker = worker
        worker.start()

    def on_info_error(self, url, error):
        self.log(f"Error fetching info: {error}")
        self.download_btn.setEnabled(True)

    def start_download(self, url, info):
        title = info.get('title', 'Unknown Title')
        thumb = info.get('thumbnail')
        domain = urlparse(url).netloc
        
        self.log(f"Starting: {title}")

        output_path = self.path_input.text()
        fmt = self.format_combo.currentText()
        quality = self.quality_combo.currentText()

        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'restrictfilenames': True,
            'noplaylist': True,
        }

        if "Audio" in fmt or "(MP3)" in fmt:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            q_map = {
                self.t("best"): "bestvideo+bestaudio/best",
                "1080p": "bestvideo[height<=1080]+bestaudio/best",
                "720p": "bestvideo[height<=720]+bestaudio/best",
                "480p": "bestvideo[height<=480]+bestaudio/best"
            }
            ydl_opts['format'] = q_map.get(quality, "bestvideo+bestaudio/best")
            ydl_opts['merge_output_format'] = 'mp4'

        item = DownloadItem(title, url, thumbnail_url=thumb, source_domain=domain)
        item.cancel_requested.connect(lambda: self.cancel_download(url))
        item.open_requested.connect(lambda: self.open_folder(output_path))
        
        self.queue_layout.insertWidget(0, item)
        self.downloads[url] = item

        worker = DownloadWorker(url, ydl_opts)
        worker.progress.connect(item.update_progress)
        worker.finished.connect(lambda f: self.on_finished(url, title, f))
        worker.error.connect(lambda e: self.on_error(url, e))
        
        item.worker = worker
        worker.start()
        self.url_input.clear()

    def cancel_download(self, url):
        if url in self.downloads:
            item = self.downloads[url]
            if hasattr(item, 'worker'):
                item.worker.downloader.stop()
            item.set_status("Cancelled", color="#EF4444")

    def open_folder(self, path):
        if os.path.exists(path):
            os.startfile(path)

    def on_finished(self, url, title, filename):
        if url in self.downloads:
            item = self.downloads[url]
            item.set_status("Finished!", color="#22C55E")
            item.progress_bar.setValue(100)
            
            # Move to completed tab
            self.queue_layout.removeWidget(item)
            self.done_layout.insertWidget(0, item)
            
            self.log(f"Done: {title}")
            add_to_history({"title": title, "url": url, "path": filename})

    def on_error(self, url, error):
        if url in self.downloads:
            item = self.downloads[url]
            item.set_status(f"Error", color="#EF4444")
            
            # Move to error tab
            self.queue_layout.removeWidget(item)
            self.error_layout.insertWidget(0, item)
            
            self.log(f"Error: {error}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
