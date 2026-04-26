COMMON_STYLE = """
/* Global Styles */
QWidget {
    font-family: 'Segoe UI';
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
    border-radius: 0px;
}
QScrollBar::handle:vertical:hover {
    background: #3B82F6;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Tabs - VS Code style */
QTabWidget::pane {
    border: 1px solid #262A33;
    background-color: transparent;
    border-radius: 0px;
    margin-top: -1px;
}
QScrollArea {
    background-color: transparent;
    border: none;
}
QScrollArea > QWidget > QWidget {
    background-color: #0F1115;
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
    border-radius: 0px;
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
    border-radius: 0px;
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
    background-color: #2D333B;
    border: 1px solid #3F444D;
    color: #E2E8F0;
    border-radius: 0px;
}
QPushButton#secondary[class="danger"] {
    color: #EF4444;
}
QPushButton#secondary:hover {
    background-color: #3F444D;
    border-color: #3B82F6;
    color: #F8FAFC;
}

/* Combo Box */
QComboBox {
    background-color: #1A1D23;
    border: 1px solid #2D333B;
    border-radius: 0px;
    padding: 6px 30px 6px 12px;
    color: #E2E8F0;
}
QComboBox::drop-down {
    border: none;
    width: 30px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #94A3B8;
    margin-top: 2px;
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
    border-radius: 0px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #3B82F6;
    border-radius: 0px;
}
QProgressBar[status="success"]::chunk { background-color: #22C55E; }
QProgressBar[status="error"]::chunk { background-color: #EF4444; }
QProgressBar[status="warning"]::chunk { background-color: #FACC15; }

/* Labels */
#TitleLabel {
    font-size: 20px;
    font-weight: 700;
    color: #F8FAFC;
    letter-spacing: 0.5px;
}
#ItemTitle {
    font-size: 15px;
    font-weight: 600;
    color: #F8FAFC;
}
#SecondaryLabel {
    color: #94A3B8;
    font-size: 13px;
    background: transparent;
    border: none;
}
#SecondaryLabel[status="error"] { color: #EF4444; }
#SecondaryLabel[status="success"] { color: #22C55E; }
#SecondaryLabel[status="warning"] { color: #FACC15; }

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
    border-radius: 0px;
}

#DownloadItem {
    background-color: #1A1D23;
    border: 1px solid #262A33;
    border-radius: 0px;
}
#DownloadItem:hover {
    border: 1px solid #3B82F6;
    background-color: #1E232B;
}

#LogPanel {
    background-color: #0A0C10;
    color: #94A3B8;
    border: 1px solid #1A1D23;
    border-radius: 0px;
    font-family: 'JetBrains Mono', 'Consolas', 'Courier New', monospace;
    font-size: 12px;
    padding: 10px;
}
"""

DARK_STYLE = COMMON_STYLE

# Explicitly defined Light Style for better aesthetics
LIGHT_STYLE = """
QWidget {
    font-family: 'Segoe UI';
    font-size: 14px;
    color: #1E293B;
}
QMainWindow {
    background-color: #F8FAFC;
}
QScrollBar:vertical {
    background: transparent;
    width: 6px;
}
QScrollBar::handle:vertical {
    background: #CBD5E1;
    border-radius: 0px;
}
QTabWidget::pane {
    border: 1px solid #E2E8F0;
    background-color: transparent;
    border-radius: 0px;
    margin-top: -1px;
}
QScrollArea {
    background-color: transparent;
    border: none;
}
QScrollArea > QWidget > QWidget {
    background-color: #F8FAFC;
}
QTabBar::tab {
    background: transparent;
    color: #64748B;
    padding: 12px 24px;
    font-weight: 500;
    border-bottom: 2px solid transparent;
}
QTabBar::tab:selected {
    color: #3B82F6;
    background-color: rgba(59, 130, 246, 0.06);
    border-bottom: 2px solid #3B82F6;
}
QTabBar::tab:hover:!selected {
    color: #0F172A;
    background-color: rgba(15, 23, 42, 0.04);
}
QLineEdit {
    background-color: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 0px;
    color: #0F172A;
}
QPushButton {
    background-color: #3B82F6;
    color: #FFFFFF;
    border-radius: 0px;
}
QPushButton#secondary {
    background-color: #F1F5F9;
    border: 1px solid #E2E8F0;
    color: #1E293B;
}
QPushButton#secondary:hover {
    background-color: #E2E8F0;
}
QComboBox {
    background-color: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 0px;
    padding: 6px 30px 6px 12px;
    color: #0F172A;
}
QComboBox::drop-down {
    border: none;
    width: 30px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #64748B;
}
QProgressBar {
    background-color: #E2E8F0;
    border-radius: 0px;
}
#TopBar {
    background-color: #FFFFFF;
    border-bottom: 1px solid #E2E8F0;
}
#InputCard {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 0px;
}
#DownloadItem {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 0px;
}
#ItemTitle {
    font-size: 15px;
    font-weight: 600;
    color: #0F172A;
}
#LogPanel {
    background-color: #F8FAFC;
    color: #475569;
    border: 1px solid #E2E8F0;
    border-radius: 0px;
}
#SecondaryLabel {
    color: #64748B;
}
#Footer {
    color: #94A3B8;
}
"""
