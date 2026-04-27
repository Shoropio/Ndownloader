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

#FieldLabel {
    color: #CBD5E1;
    font-size: 13px;
    font-weight: 700;
    background: transparent;
    border: none;
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

#Thumbnail {
    background-color: #0A0C10;
    border: 1px solid #262A33;
    border-radius: 0px;
    color: #64748B;
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
    color: #172033;
    outline: none;
}
QMainWindow {
    background-color: #EEF3F8;
}
QScrollBar:vertical {
    background: transparent;
    width: 6px;
    margin: 0px;
}
QScrollBar::handle:vertical {
    background: #B7C4D4;
    min-height: 20px;
    border-radius: 0px;
}
QScrollBar::handle:vertical:hover {
    background: #2563EB;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QTabWidget::pane {
    border: 1px solid #C9D4E2;
    background-color: #F8FAFC;
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
    font-weight: 600;
    border-bottom: 2px solid transparent;
}
QTabBar::tab:selected {
    color: #1D4ED8;
    background-color: #EAF2FF;
    border-bottom: 2px solid #2563EB;
}
QTabBar::tab:hover:!selected {
    color: #172033;
    background-color: #F1F5F9;
}
QLineEdit {
    background-color: #FFFFFF;
    border: 1px solid #AEBCCE;
    border-radius: 0px;
    padding: 8px 16px;
    color: #0F172A;
    selection-background-color: #2563EB;
}
QLineEdit:hover {
    border: 1px solid #7F91A8;
    background-color: #FFFFFF;
}
QLineEdit:focus {
    border: 1px solid #2563EB;
    background-color: #FCFDFF;
}
QLineEdit:read-only {
    background-color: #F8FAFC;
    color: #334155;
}
QLineEdit::placeholder {
    color: #7C8BA1;
}
QPushButton {
    border: 1px solid #1D4ED8;
    border-radius: 0px;
    padding: 10px 20px;
    font-weight: 700;
    background-color: #2563EB;
    color: #FFFFFF;
}
QPushButton:hover {
    background-color: #1D4ED8;
    border-color: #1E40AF;
}
QPushButton:pressed {
    background-color: #1E40AF;
    border-color: #1E3A8A;
}
QPushButton:disabled {
    background-color: #D9E2EE;
    border-color: #C7D2E0;
    color: #8290A4;
}
QPushButton#secondary {
    background-color: #F8FAFC;
    border: 1px solid #AEBCCE;
    color: #1E293B;
    border-radius: 0px;
}
QPushButton#secondary[class="danger"] {
    color: #DC2626;
}
QPushButton#secondary:hover {
    background-color: #EAF2FF;
    border-color: #2563EB;
    color: #0F172A;
}
QPushButton#secondary:pressed {
    background-color: #DCEBFF;
    border-color: #1D4ED8;
}
QComboBox {
    background-color: #FFFFFF;
    border: 1px solid #AEBCCE;
    border-radius: 0px;
    padding: 6px 30px 6px 12px;
    color: #0F172A;
}
QComboBox:hover {
    border: 1px solid #7F91A8;
}
QComboBox:focus {
    border: 1px solid #2563EB;
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
    margin-top: 2px;
}
QComboBox QAbstractItemView {
    background-color: #FFFFFF;
    border: 1px solid #AEBCCE;
    selection-background-color: #2563EB;
    color: #0F172A;
}
QProgressBar {
    border: none;
    background-color: #DDE6F0;
    height: 4px;
    border-radius: 0px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #2563EB;
    border-radius: 0px;
}
QProgressBar[status="success"]::chunk { background-color: #16A34A; }
QProgressBar[status="error"]::chunk { background-color: #DC2626; }
QProgressBar[status="warning"]::chunk { background-color: #CA8A04; }
#TitleLabel {
    font-size: 20px;
    font-weight: 700;
    color: #0F172A;
    letter-spacing: 0.5px;
}
#TopBar {
    background-color: #FFFFFF;
    border-bottom: 1px solid #C9D4E2;
}
#InputCard {
    background-color: #FFFFFF;
    border: 1px solid #C4D0DE;
    border-radius: 0px;
}
#DownloadItem {
    background-color: #FFFFFF;
    border: 1px solid #C9D4E2;
    border-radius: 0px;
}
#DownloadItem:hover {
    border: 1px solid #2563EB;
    background-color: #FBFDFF;
}
#Thumbnail {
    background-color: #E8EEF6;
    border: 1px solid #C9D4E2;
    border-radius: 0px;
    color: #64748B;
}
#ItemTitle {
    font-size: 15px;
    font-weight: 700;
    color: #0F172A;
}
#LogPanel {
    background-color: #F4F7FB;
    color: #334155;
    border: 1px solid #C4D0DE;
    border-radius: 0px;
    font-family: 'JetBrains Mono', 'Consolas', 'Courier New', monospace;
    font-size: 12px;
    padding: 10px;
}
#SecondaryLabel {
    color: #64748B;
    font-size: 13px;
    background: transparent;
    border: none;
}
#SecondaryLabel[status="error"] { color: #DC2626; }
#SecondaryLabel[status="success"] { color: #16A34A; }
#SecondaryLabel[status="warning"] { color: #CA8A04; }
#FieldLabel {
    color: #263449;
    font-size: 13px;
    font-weight: 700;
    background: transparent;
    border: none;
}
#Footer {
    font-size: 12px;
    color: #7C8BA1;
}
"""
