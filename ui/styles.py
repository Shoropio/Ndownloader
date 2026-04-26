COMMON_STYLE = """
/* Global Styles */
QWidget {
    font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;
    font-size: 14px;
    color: #E2E8F0;
    outline: none;
}

QMainWindow {
    background-color: #0F1115;
}

/* ScrollBar - Discord style */
QScrollBar:vertical {
    border: none;
    background: transparent;
    width: 6px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: #2D333B;
    min-height: 20px;
    border-radius: 3px;
}
QScrollBar::handle:vertical:hover {
    background: #3B82F6;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Tabs - VS Code style */
QTabWidget::pane {
    border: none;
    background-color: transparent;
}
QTabBar::tab {
    background: transparent;
    color: #94A3B8;
    padding: 12px 24px;
    font-weight: 500;
    border-bottom: 2px solid transparent;
}
QTabBar::tab:selected {
    color: #3B82F6;
    background-color: rgba(59, 130, 246, 0.05);
    border-bottom: 2px solid #3B82F6;
}
QTabBar::tab:hover:!selected {
    color: #E2E8F0;
    background-color: rgba(255, 255, 255, 0.03);
}

/* Input Fields */
QLineEdit {
    background-color: #1A1D23;
    border: 1px solid #2D333B;
    border-radius: 8px;
    padding: 8px 16px;
    color: #F8FAFC;
    selection-background-color: #3B82F6;
}
QLineEdit:focus {
    border: 1px solid #3B82F6;
    background-color: #1F232B;
}
QLineEdit::placeholder {
    color: #64748B;
}

/* Buttons */
QPushButton {
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    background-color: #3B82F6;
    color: #FFFFFF;
}
QPushButton:hover {
    background-color: #2563EB;
}
QPushButton:pressed {
    background-color: #1D4ED8;
}
QPushButton:disabled {
    background-color: #1E293B;
    color: #475569;
}

QPushButton#secondary {
    background-color: #262A33;
    border: 1px solid #2D333B;
    color: #CBD5E1;
}
QPushButton#secondary:hover {
    background-color: #2D333B;
    border-color: #3B82F6;
    color: #F8FAFC;
}

/* Combo Box */
QComboBox {
    background-color: #1A1D23;
    border: 1px solid #2D333B;
    border-radius: 8px;
    padding: 6px 12px;
    color: #E2E8F0;
}
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid #94A3B8;
    margin-right: 10px;
}
QComboBox QAbstractItemView {
    background-color: #1A1D23;
    border: 1px solid #2D333B;
    selection-background-color: #3B82F6;
    color: #E2E8F0;
}

/* Progress Bar */
QProgressBar {
    border: none;
    background-color: #0F1115;
    height: 4px;
    border-radius: 2px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #3B82F6;
    border-radius: 2px;
}

/* Labels */
#TitleLabel {
    font-size: 20px;
    font-weight: 700;
    color: #F8FAFC;
    letter-spacing: 0.5px;
}
#SecondaryLabel {
    color: #94A3B8;
    font-size: 13px;
}
#Footer {
    font-size: 12px;
    color: #475569;
}

/* Panels */
#TopBar {
    background-color: #1A1D23;
    border-bottom: 1px solid #262A33;
}

#InputCard {
    background-color: #1A1D23;
    border: 1px solid #262A33;
    border-radius: 12px;
}

#DownloadItem {
    background-color: #1A1D23;
    border: 1px solid #262A33;
    border-radius: 12px;
}
#DownloadItem:hover {
    border: 1px solid #3B82F6;
    background-color: #1E232B;
}

#LogPanel {
    background-color: #0A0C10;
    color: #94A3B8;
    border: 1px solid #1A1D23;
    border-radius: 8px;
    font-family: 'JetBrains Mono', 'Consolas', 'Courier New', monospace;
    font-size: 12px;
    padding: 10px;
}
"""

DARK_STYLE = COMMON_STYLE

# Light Style (Minimalist adaptation)
LIGHT_STYLE = COMMON_STYLE.replace("#0F1115", "#F8FAFC").replace("#1A1D23", "#FFFFFF").replace("#262A33", "#E2E8F0").replace("#2D333B", "#CBD5E1").replace("#E2E8F0", "#1E293B").replace("#F8FAFC", "#0F172A").replace("#94A3B8", "#64748B")

