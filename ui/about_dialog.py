from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PySide6.QtCore import Qt

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tentang Aplikasi")
        self.setFixedSize(350, 220)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        label = QLabel("""
        <div style='text-align: center;'>
            <h2 style='color: #0F172A; margin-bottom: 0px;'>Smart Finance</h2>
            <p style='color: #64748B; margin-top: 5px;'>Tracker Keuangan Pribadi</p>
            <hr style='border: 1px solid #E2E8F0; margin: 15px 0;'>
            <p style='font-size: 14px; color: #1E293B;'><b>i'm DODI WIJAYA</b></p>
            <p style='font-size: 13px; color: #64748B;'>NIM: F1D02310047</p>
        </div>
        """)

        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)