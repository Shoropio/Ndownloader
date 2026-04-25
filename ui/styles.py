COMMON_STYLE = """
QWidget {
    font-family: 'Inter', 'Segoe UI', sans-serif;
    font-size: 14px;
}

QMainWindow {
    background-color: #0F1115;
}

/* ScrollBar */
QScrollBar:vertical {
    border: none;
    background: transparent;
    width: 8px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: #2B3240;
    min-height: 20px;
    border-radius: 4px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Tabs */
QTabWidget::pane {
    border: none;
    background-color: transparent;
}
QTabBar::tab {
    background: transparent;
    color: #9AA4B2;
    padding: 10px 20px;
    border-bottom: 2px solid transparent;
}
QTabBar::tab:selected {
    color: #3B82F6;
    border-bottom: 2px solid #3B82F6;
}
QTabBar::tab:hover {
    color: #F4F7FB;
}

/* Input Fields */
QLineEdit {
    background-color: #171A21;
    border: 1px solid #2B3240;
    border-radius: 8px;
    padding: 10px 15px;
    color: #F4F7FB;
}
QLineEdit:focus {
    border-color: #3B82F6;
}

/* Buttons */
QPushButton {
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    background-color: #3B82F6;
    color: #F4F7FB;
}
QPushButton:hover {
    background-color: #2563EB;
}
QPushButton#secondary {
    background-color: #1F2430;
    border: 1px solid #2B3240;
    color: #F4F7FB;
}
QPushButton#secondary:hover {
    background-color: #2B3240;
}

/* Combo Box */
QComboBox {
    background-color: #171A21;
    border: 1px solid #2B3240;
    border-radius: 8px;
    padding: 6px 12px;
    color: #F4F7FB;
}
QComboBox::drop-down {
    border: none;
}

/* Progress Bar */
QProgressBar {
    border: none;
    background-color: #0F1115;
    height: 6px;
    border-radius: 3px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #3B82F6;
    border-radius: 3px;
}

/* Labels */
#TitleLabel {
    font-size: 20px;
    font-weight: 800;
    color: #F4F7FB;
}
#SecondaryLabel {
    color: #9AA4B2;
    font-size: 12px;
}
#Footer {
    font-size: 11px;
    color: #4B5563;
}

/* Cards */
#DownloadItem {
    background-color: #1F2430;
    border: 1px solid #2B3240;
    border-radius: 12px;
    margin-bottom: 10px;
}
#LogPanel {
    background-color: #0A0C10;
    color: #9AA4B2;
    border-radius: 8px;
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    font-size: 12px;
}
"""

DARK_STYLE = COMMON_STYLE

# We will implement Light theme later or keep it as a variant
LIGHT_STYLE = COMMON_STYLE.replace("#0F1115", "#F8FAFC").replace("#171A21", "#FFFFFF").replace("#1F2430", "#F1F5F9").replace("#2B3240", "#E2E8F0").replace("#F4F7FB", "#0F172A").replace("#9AA4B2", "#64748B")
