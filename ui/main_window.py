from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
    QTableWidgetItem, QToolBar, QPushButton, QComboBox, QLineEdit,
    QMessageBox, QLabel, QAbstractItemView, QHeaderView,
    QSizePolicy, QDateEdit
)
from PySide6.QtGui import QColor, QAction
from PySide6.QtCore import Qt, QDate

from database.db_manager import DatabaseManager
from ui.transaction_dialog import TransactionDialog
from ui.about_dialog import AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("💰 Smart Finance Tracker")
        self.resize(1000, 650)

        self.db = DatabaseManager()

        self.setup_menu()
        self.setup_toolbar()
        self.setup_table()

        self.load_data()

    def setup_menu(self):
        menu = self.menuBar()
        help_menu = menu.addMenu("Bantuan")

        about_action = QAction("Tentang Aplikasi", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def setup_toolbar(self):
       
        toolbar_action = QToolBar()
        toolbar_action.setMovable(False)
        self.addToolBar(toolbar_action)

        add_btn = QPushButton("+ Tambah")
        add_btn.setObjectName("btn_add")
        add_btn.clicked.connect(self.add_transaction)

        edit_btn = QPushButton("✏ Edit")
        edit_btn.setObjectName("btn_edit")
        edit_btn.clicked.connect(self.edit_transaction)

        delete_btn = QPushButton("🗑 Hapus")
        delete_btn.setObjectName("btn_delete")
        delete_btn.clicked.connect(self.delete_transaction)

        toolbar_action.addWidget(add_btn)
        toolbar_action.addWidget(edit_btn)
        toolbar_action.addWidget(delete_btn)

        spacer_action = QWidget()
        spacer_action.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar_action.addWidget(spacer_action)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Cari catatan...")
        self.search_input.setFixedWidth(250)
        self.search_input.textChanged.connect(self.load_data)
        toolbar_action.addWidget(self.search_input)


        self.addToolBarBreak()
        toolbar_filter = QToolBar()
        toolbar_filter.setMovable(False)
        self.addToolBar(toolbar_filter)

        lbl_jenis = QLabel("Jenis: ")
        lbl_jenis.setObjectName("filter_lbl")
        toolbar_filter.addWidget(lbl_jenis)

        self.filter_box = QComboBox()
        self.filter_box.addItems(["Semua", "Pemasukan", "Pengeluaran"])
        self.filter_box.currentTextChanged.connect(self.load_data)
        toolbar_filter.addWidget(self.filter_box)

        spacer1 = QWidget()
        spacer1.setFixedWidth(15)
        toolbar_filter.addWidget(spacer1)

        lbl_kategori = QLabel("Kategori: ")
        lbl_kategori.setObjectName("filter_lbl")
        toolbar_filter.addWidget(lbl_kategori)

        self.category_filter = QComboBox()
        self.category_filter.addItems([
            "Semua", "Makan", "Minum", "Belanja", "Transportasi", 
            "Kuliah", "Freelance", "Gaji", "Bonus"
        ])
        self.category_filter.currentTextChanged.connect(self.load_data)
        toolbar_filter.addWidget(self.category_filter)

        spacer2 = QWidget()
        spacer2.setFixedWidth(15)
        toolbar_filter.addWidget(spacer2)

        current_date = QDate.currentDate()
        
        lbl_dari = QLabel("Dari: ")
        lbl_dari.setObjectName("filter_lbl")
        toolbar_filter.addWidget(lbl_dari)

        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QDate(current_date.year(), current_date.month(), 1))
        self.start_date.dateChanged.connect(self.load_data)
        toolbar_filter.addWidget(self.start_date)

        spacer3 = QWidget()
        spacer3.setFixedWidth(10)
        toolbar_filter.addWidget(spacer3)

        lbl_sampai = QLabel("Sampai: ")
        lbl_sampai.setObjectName("filter_lbl")
        toolbar_filter.addWidget(lbl_sampai)

        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(current_date)
        self.end_date.dateChanged.connect(self.load_data)
        toolbar_filter.addWidget(self.end_date)

    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "No", "Tanggal", "Jenis", "Kategori", "Nominal", "Metode", "Catatan"
        ])

        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setShowGrid(True)
        
        self.table.setAlternatingRowColors(False)

        self.table.verticalHeader().setDefaultSectionSize(50)
        self.table.setMinimumHeight(500)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(18)

        dash_layout = QHBoxLayout()

        self.lbl_income = QLabel()
        self.lbl_expense = QLabel()
        self.lbl_balance = QLabel()

        for lbl in [self.lbl_income, self.lbl_expense, self.lbl_balance]:
            lbl.setObjectName("dash_card")
            lbl.setAlignment(Qt.AlignCenter)
            dash_layout.addWidget(lbl)

        layout.addLayout(dash_layout)

        layout.addWidget(self.table)

        footer = QLabel("Dodi Wijaya  |  F1D02310047")
        footer.setObjectName("footer_info")
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)

        self.setCentralWidget(container)

    def load_data(self):
        self.table.setRowCount(0)
        data = self.db.get_transactions()

        global_income = sum(int(row[4]) for row in data if row[2] == "Pemasukan")
        global_expense = sum(int(row[4]) for row in data if row[2] == "Pengeluaran")
        global_balance = global_income - global_expense

        filter_jenis = self.filter_box.currentText()
        filter_kategori = self.category_filter.currentText()
        start_date = self.start_date.date()
        end_date = self.end_date.date()
        keyword = self.search_input.text().lower()

        filtered_income = 0
        filtered_expense = 0
        nomor = 1

        for row_data in data:
            if filter_jenis != "Semua" and row_data[2] != filter_jenis:
                continue
            if filter_kategori != "Semua" and row_data[3] != filter_kategori:
                continue
            
            row_date = QDate.fromString(row_data[1], "yyyy-MM-dd")
            if not (start_date <= row_date <= end_date):
                continue
            
            if keyword not in row_data[3].lower() and keyword not in str(row_data[6]).lower():
                continue

            row = self.table.rowCount()
            self.table.insertRow(row)

            formatted_amount = f"Rp {int(row_data[4]):,}"
            
            table_data = [
                nomor,
                row_data[1],
                row_data[2],
                row_data[3],
                formatted_amount,
                row_data[5],
                row_data[6]
            ]

            for col, value in enumerate(table_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)

                if col == 0:
                    item.setData(Qt.UserRole, row_data[0])

                if col == 4:
                    item.setData(Qt.UserRole, row_data[4])

                if row_data[2] == "Pemasukan":
                    item.setBackground(QColor("#DCFCE7")) 
                    item.setForeground(QColor("#064E3B")) 
                else:
                    item.setBackground(QColor("#FEE2E2"))
                    item.setForeground(QColor("#7F1D1D"))

                self.table.setItem(row, col, item)
            
            if row_data[2] == "Pemasukan":
                filtered_income += int(row_data[4])
            else:
                filtered_expense += int(row_data[4])

            nomor += 1

        self.lbl_income.setText(
            f"<div style='text-align: center;'>"
            f"<span style='font-size: 13px; color: #64748B; font-weight: normal;'>📥 Pemasukan (Filter)</span><br><br>"
            f"<span style='font-size: 26px; color: #059669; font-weight: bold;'>Rp {filtered_income:,}</span>"
            f"</div>"
        )

        self.lbl_expense.setText(
            f"<div style='text-align: center;'>"
            f"<span style='font-size: 13px; color: #64748B; font-weight: normal;'>📤 Pengeluaran (Filter)</span><br><br>"
            f"<span style='font-size: 26px; color: #E11D48; font-weight: bold;'>Rp {filtered_expense:,}</span>"
            f"</div>"
        )

        self.lbl_balance.setText(
            f"<div style='text-align: center;'>"
            f"<span style='font-size: 13px; color: #64748B; font-weight: normal;'>💰 Total Saldo Tersedia</span><br><br>"
            f"<span style='font-size: 26px; color: #0F172A; font-weight: bold;'>Rp {global_balance:,}</span>"
            f"</div>"
        )

        self.statusBar().showMessage(
            f"Ditampilkan -> Pemasukan: Rp {filtered_income:,} | Pengeluaran: Rp {filtered_expense:,} | Saldo Aktual: Rp {global_balance:,}"
        )

    def add_transaction(self):
        dialog = TransactionDialog(self)
        if dialog.exec():
            self.db.add_transaction(dialog.get_data())
            self.load_data()

    def edit_transaction(self):
        row = self.table.currentRow()
        if row < 0:
            return

        transaction_id = self.table.item(row, 0).data(Qt.UserRole)
        raw_amount = self.table.item(row, 4).data(Qt.UserRole)

        data = (
            transaction_id,
            self.table.item(row, 1).text(),
            self.table.item(row, 2).text(),
            self.table.item(row, 3).text(),
            raw_amount,
            self.table.item(row, 5).text(),
            self.table.item(row, 6).text(),
        )

        dialog = TransactionDialog(self, data)
        if dialog.exec():
            self.db.update_transaction(dialog.get_data(), transaction_id)
            self.load_data()

    def delete_transaction(self):
        row = self.table.currentRow()
        if row < 0:
            return

        confirm = QMessageBox.question(
            self, "Konfirmasi", "Yakin ingin menghapus transaksi ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            transaction_id = self.table.item(row, 0).data(Qt.UserRole)
            self.db.delete_transaction(transaction_id)
            self.load_data()

    def show_about(self):
        dialog = AboutDialog()
        dialog.exec()