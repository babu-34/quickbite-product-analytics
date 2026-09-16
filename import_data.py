import mysql.connector
import csv
import os

# -----------------------------
# MySQL connection
# -----------------------------
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="bob12345",
    database="quickbite"
)

cursor = connection.cursor()

# CSV folder
DATA_FOLDER = r"C:\Users\91939\OneDrive\Desktop\QuickBite-Product-Analytics\data"

# Large batch for faster import
BATCH_SIZE = 10000


def import_csv(filename, table_name, columns):
    file_path = os.path.join(DATA_FOLDER, filename)

    print(f"\nImporting {filename}...")

    query = f"""
        INSERT INTO {table_name} ({", ".join(columns)})
        VALUES ({", ".join(["%s"] * len(columns))})
    """

    batch = []
    total = 0

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        # Skip CSV header
        next(reader)

        for row in reader:
    # Convert empty values to NULL
            row = [None if value == "" else value for value in row]
            batch.append(row)

            if len(batch) >= BATCH_SIZE:
                cursor.executemany(query, batch)
                connection.commit()

                total += len(batch)
                print(f"  Imported: {total}")
                batch.clear()

        # Remaining rows
        if batch:
            cursor.executemany(query, batch)
            connection.commit()
            total += len(batch)

    print(f"Completed {table_name}: {total} rows")


try:
    # Temporarily disable foreign-key checks for bulk loading
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    import_csv(
        "users.csv",
        "users",
        ["user_id", "signup_date", "city", "age_group",
         "device_type", "acquisition_channel"]
    )

    import_csv(
        "restaurants.csv",
        "restaurants",
        ["restaurant_id", "restaurant_name", "city",
         "cuisine", "rating", "delivery_time"]
    )

    import_csv(
        "menu_items.csv",
        "menu_items",
        ["item_id", "restaurant_id", "item_name",
         "category", "price"]
    )

    import_csv(
        "orders.csv",
        "orders",
        ["order_id", "user_id", "restaurant_id", "order_date",
         "order_status", "subtotal", "delivery_fee",
         "discount", "total_amount", "payment_method"]
    )

    import_csv(
        "order_items.csv",
        "order_items",
        ["order_item_id", "order_id", "item_id",
         "quantity", "price"]
    )

    import_csv(
        "events.csv",
        "events",
        ["event_id", "user_id", "event_time", "event_name",
         "restaurant_id", "item_id", "session_id"]
    )

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

    print("\n======================================")
    print("QUICKBITE DATA IMPORT COMPLETE")
    print("======================================")

except Exception as e:
    connection.rollback()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    print("\nIMPORT FAILED:")
    print(e)

finally:
    cursor.close()
    connection.close()