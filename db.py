import mysql.connector

def save_to_database(color_counts):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bincom-test"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS color_frequency (
            color VARCHAR(50) PRIMARY KEY,
            frequency INT
        )
    """)

    for color, count in color_counts.items():
        cursor.execute("""
            INSERT INTO color_frequency (color, frequency)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE frequency = %s
        """, (color, count, count))

    conn.commit()
    conn.close()
