import sqlite3


class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("data/finance.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            jenis TEXT,
            kategori TEXT,
            nominal INTEGER,
            metode TEXT,
            catatan TEXT
        )
        """

        self.conn.execute(query)
        self.conn.commit()

    def add_transaction(self, data):
        query = """
        INSERT INTO transactions
        (tanggal, jenis, kategori, nominal, metode, catatan)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        self.conn.execute(query, (
            data["tanggal"],
            data["jenis"],
            data["kategori"],
            data["nominal"],
            data["metode"],
            data["catatan"]
        ))

        self.conn.commit()

    def get_transactions(self):
        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM transactions
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    def update_transaction(self, data, transaction_id):
        query = """
        UPDATE transactions
        SET tanggal=?,
            jenis=?,
            kategori=?,
            nominal=?,
            metode=?,
            catatan=?
        WHERE id=?
        """

        self.conn.execute(query, (
            data["tanggal"],
            data["jenis"],
            data["kategori"],
            data["nominal"],
            data["metode"],
            data["catatan"],
            transaction_id
        ))

        self.conn.commit()

    def delete_transaction(self, transaction_id):
        self.conn.execute(
            "DELETE FROM transactions WHERE id=?",
            (transaction_id,)
        )

        self.conn.commit()