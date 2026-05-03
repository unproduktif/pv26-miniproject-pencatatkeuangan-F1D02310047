from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QComboBox,
    QTextEdit, QPushButton, QDateEdit, QMessageBox, QLabel
)
from PySide6.QtCore import QDate, Qt

class TransactionDialog(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)

        self.setWindowTitle("Form Transaksi")
        self.setFixedWidth(400)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        title = QLabel("📝 Detail Transaksi")
        title.setObjectName("dialog_title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        form = QFormLayout()
        form.setSpacing(12)

        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)

        self.type_input = QComboBox()
        self.type_input.addItems(["Pemasukan", "Pengeluaran"])

        self.category_input = QComboBox()
        self.category_input.addItems([
            "Makan", "Minum", "Belanja", "Transportasi", 
            "Kuliah", "Freelance", "Gaji", "Bonus"
        ])

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Contoh: 50000")

        self.method_input = QComboBox()
        self.method_input.addItems(["Cash", "Bank", "QRIS", "Dana", "OVO", "GoPay"])

        self.note_input = QTextEdit()
        self.note_input.setPlaceholderText("Tulis catatan di sini...")
        self.note_input.setFixedHeight(80)

        form.addRow("Tanggal", self.date_input)
        form.addRow("Jenis", self.type_input)
        form.addRow("Kategori", self.category_input)
        form.addRow("Nominal", self.amount_input)
        form.addRow("Metode", self.method_input)
        form.addRow("Catatan", self.note_input)

        layout.addLayout(form)

        self.save_button = QPushButton("✨ Simpan Transaksi")
        self.save_button.setObjectName("btn_save")
        self.save_button.clicked.connect(self.validate_input)
        layout.addWidget(self.save_button)

        if data:
            self.date_input.setDate(QDate.fromString(data[1], "yyyy-MM-dd"))
            self.type_input.setCurrentText(data[2])
            self.category_input.setCurrentText(data[3])
            self.amount_input.setText(str(data[4]))
            self.method_input.setCurrentText(data[5])
            self.note_input.setText(data[6])

    def validate_input(self):
        if not self.amount_input.text().isdigit():
            QMessageBox.warning(self, "Oops!", "Nominal harus berupa angka dan tidak boleh kosong.")
            return
        self.accept()

    def get_data(self):
        return {
            "tanggal": self.date_input.date().toString("yyyy-MM-dd"),
            "jenis": self.type_input.currentText(),
            "kategori": self.category_input.currentText(),
            "nominal": self.amount_input.text(),
            "metode": self.method_input.currentText(),
            "catatan": self.note_input.toPlainText()
        }