import mysql.connector
import csv

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="bob12345",
    database="quickbite"
)

cursor = connection.cursor()

file_path = r"C:\Users\91939\OneDrive\Desktop\QuickBite-Product-Analytics\data\events.csv"

query = """
INSERT INTO events
(event_id, user_id, event_time, event_name, restaurant_id, item_id, session_id)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

batch = []
batch_size = 10000
total = 0

try:
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            # Convert empty CSV values to SQL NULL
            row = [None if value == "" else value for value in row]

            batch.append(row)

            if len(batch) >= batch_size:
                cursor.executemany(query, batch)
                connection.commit()

                total += len(batch)
                print(f"Imported: {total}")
                batch.clear()

        if batch:
            cursor.executemany(query, batch)
            connection.commit()
            total += len(batch)

    print(f"\nEvents import completed: {total} rows")

except Exception as e:
    connection.rollback()
    print("\nIMPORT FAILED:")
    print(e)

finally:
    cursor.close()
    connection.close()