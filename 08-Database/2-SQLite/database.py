import sqlite3
from schema import BaseShipment, UpdateShipment


class Database:
    def __init__(self, db_path: str = "store.db"):
        self.db_path = db_path
        self.create_table()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn

    def create_table(self):
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS Shipments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    price REAL NOT NULL
                )
            """)

    def insert_data(self, data: BaseShipment) -> int:
        with self.get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO Shipments (product, quantity, status, price)
                VALUES (:product, :quantity, :status, :price)
                """,
                data.model_dump(),
            )
            return cursor.lastrowid

    def update_data(self, data: UpdateShipment) -> bool:
        with self.get_connection() as conn:
            cursor = conn.execute(
                """
                UPDATE Shipments 
                SET status = :status 
                WHERE id = :id
                """,
                data.model_dump(),
            )
            return cursor.rowcount > 0

    def get_data(self, shipment_id: int) -> dict | None:
        with self.get_connection() as conn:
            cursor = conn.execute(
                "SELECT * FROM Shipments WHERE id = :id",
                {"id": shipment_id},
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def delete_data(self, shipment_id: int) -> bool:
        with self.get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM Shipments WHERE id = :id",
                {"id": shipment_id},
            )
            return cursor.rowcount > 0