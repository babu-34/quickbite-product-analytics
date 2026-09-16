import csv
import random
from datetime import datetime, date, timedelta
from collections import defaultdict
from pathlib import Path

# =========================================================
# QUICKBITE DATA GENERATOR - V2
# Product Analytics & PRD Project
# =========================================================

random.seed(42)

# -----------------------------
# SETTINGS
# -----------------------------
NUM_USERS = 10000
NUM_RESTAURANTS = 300
NUM_MENU_ITEMS = 5000
NUM_ORDERS = 20000
NUM_BROWSE_SESSIONS = 30000

START_DATE = date(2026, 1, 1)
END_DATE = date(2026, 6, 30)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

# -----------------------------
# MASTER DATA
# -----------------------------
CITIES = [
    "Hyderabad",
    "Visakhapatnam",
    "Bengaluru",
    "Chennai",
    "Pune",
    "Mumbai",
    "Delhi"
]

CUISINES = [
    "Indian",
    "South Indian",
    "North Indian",
    "Chinese",
    "Biryani",
    "Fast Food",
    "Pizza",
    "Desserts",
    "Healthy",
    "Cafe"
]

DEVICES = ["Android", "iOS"]

ACQUISITION_CHANNELS = [
    "Organic",
    "Google Ads",
    "Instagram",
    "Referral",
    "YouTube",
    "Push Notification"
]

PAYMENT_METHODS = [
    "UPI",
    "Card",
    "Wallet",
    "Cash"
]

ORDER_STATUSES = [
    "Completed",
    "Cancelled",
    "Payment Failed"
]

AGE_GROUPS = [
    "18-24",
    "25-34",
    "35-44",
    "45+"
]

MENU_CATEGORIES = [
    "Main Course",
    "Starter",
    "Beverage",
    "Dessert",
    "Combo"
]

DISH_NAMES = [
    "Chicken Biryani",
    "Veg Biryani",
    "Paneer Biryani",
    "Chicken Fried Rice",
    "Veg Fried Rice",
    "Paneer Butter Masala",
    "Chicken Curry",
    "Butter Naan",
    "Masala Dosa",
    "Idli",
    "Vada",
    "Chicken 65",
    "Paneer Tikka",
    "Veg Noodles",
    "Chicken Noodles",
    "Margherita Pizza",
    "Farmhouse Pizza",
    "Burger",
    "French Fries",
    "Momos",
    "Cold Coffee",
    "Fresh Lime Soda",
    "Gulab Jamun",
    "Brownie",
    "Ice Cream"
]


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def random_date(start_date, end_date):
    days = (end_date - start_date).days
    return start_date + timedelta(days=random.randint(0, days))


def random_datetime_for_user(signup_date):
    """
    Generate a datetime on or after signup_date
    and within the project date range.
    """

    if signup_date >= END_DATE:
        event_date = signup_date
    else:
        event_date = random_date(signup_date, END_DATE)

    hour = random.randint(7, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    return datetime(
        event_date.year,
        event_date.month,
        event_date.day,
        hour,
        minute,
        second
    )


def is_new_user(signup_date, event_time):
    """
    User is considered new if the session happens
    within 14 days of signup.
    """

    return (event_time.date() - signup_date).days <= 14


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def write_csv(filename, rows, fieldnames):
    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created: {filepath} -> {len(rows):,} rows")


# =========================================================
# 1. USERS
# =========================================================

users = []

for user_id in range(1, NUM_USERS + 1):

    signup_date = random_date(START_DATE, END_DATE)

    user = {
        "user_id": user_id,
        "signup_date": signup_date.strftime("%Y-%m-%d"),
        "city": random.choice(CITIES),
        "age_group": random.choice(AGE_GROUPS),
        "device_type": random.choices(
            DEVICES,
            weights=[70, 30]
        )[0],
        "acquisition_channel": random.choice(ACQUISITION_CHANNELS)
    }

    users.append(user)


# =========================================================
# 2. RESTAURANTS
# =========================================================

restaurants = []

for restaurant_id in range(1, NUM_RESTAURANTS + 1):

    city = CITIES[(restaurant_id - 1) % len(CITIES)]

    cuisine = random.choice(CUISINES)

    restaurant = {
        "restaurant_id": restaurant_id,
        "restaurant_name": f"{cuisine} Kitchen {restaurant_id}",
        "city": city,
        "cuisine": cuisine,
        "rating": round(random.uniform(3.2, 4.9), 1),
        "delivery_time": random.randint(20, 60)
    }

    restaurants.append(restaurant)


# =========================================================
# 3. MENU ITEMS
# =========================================================

menu_items = []

restaurant_to_items = defaultdict(list)

for item_id in range(1, NUM_MENU_ITEMS + 1):

    restaurant_id = ((item_id - 1) % NUM_RESTAURANTS) + 1

    dish = random.choice(DISH_NAMES)
    category = random.choice(MENU_CATEGORIES)

    price = round(
        random.uniform(80, 650),
        2
    )

    item = {
        "item_id": item_id,
        "restaurant_id": restaurant_id,
        "item_name": f"{dish} {item_id}",
        "category": category,
        "price": price
    }

    menu_items.append(item)

    restaurant_to_items[restaurant_id].append(item)


# =========================================================
# 4. ORDERS + ORDER ITEMS
# =========================================================

orders = []
order_items = []

user_lookup = {
    user["user_id"]: user
    for user in users
}

restaurants_by_city = defaultdict(list)

for restaurant in restaurants:
    restaurants_by_city[
        restaurant["city"]
    ].append(restaurant)


for order_id in range(1, NUM_ORDERS + 1):

    # Select user
    user = random.choice(users)

    user_id = user["user_id"]
    user_city = user["city"]

    # Restaurant from same city as user
    restaurant = random.choice(
        restaurants_by_city[user_city]
    )

    restaurant_id = restaurant["restaurant_id"]

    # Order date after signup
    signup_date = datetime.strptime(
        user["signup_date"],
        "%Y-%m-%d"
    ).date()

    order_datetime = random_datetime_for_user(
        signup_date
    )

    # Determine whether user is new
    new_user = is_new_user(
        signup_date,
        order_datetime
    )

    # Device effect
    android = user["device_type"] == "Android"

    # -----------------------------
    # Order status
    # -----------------------------

    completed_probability = 0.78
    cancelled_probability = 0.12
    payment_failed_probability = 0.10

    if android:
        completed_probability -= 0.06
        cancelled_probability += 0.02
        payment_failed_probability += 0.04

    if new_user:
        completed_probability -= 0.06
        cancelled_probability += 0.03
        payment_failed_probability += 0.03

    status = random.choices(
        ORDER_STATUSES,
        weights=[
            completed_probability,
            cancelled_probability,
            payment_failed_probability
        ]
    )[0]

    # -----------------------------
    # Order items
    # -----------------------------

    available_items = restaurant_to_items[
        restaurant_id
    ]

    number_of_items = random.choices(
        [1, 2, 3, 4],
        weights=[1, 3, 3, 1]
    )[0]

    selected_items = random.sample(
        available_items,
        number_of_items
    )

    subtotal = 0

    for item in selected_items:

        quantity = random.randint(1, 3)

        item_price = item["price"]

        subtotal += item_price * quantity

        order_items.append({
            "order_item_id": len(order_items) + 1,
            "order_id": order_id,
            "item_id": item["item_id"],
            "quantity": quantity,
            "price": item_price
        })

    subtotal = round(subtotal, 2)

    # -----------------------------
    # Delivery fee
    # -----------------------------

    if subtotal >= 600:
        delivery_fee = 0
    else:
        delivery_fee = random.choice(
            [20, 30, 40, 50, 60]
        )

    # -----------------------------
    # Discount
    # -----------------------------

    if new_user and random.random() < 0.45:

        discount = random.choice(
            [50, 75, 100, 120]
        )

    elif random.random() < 0.20:

        discount = random.choice(
            [20, 30, 50]
        )

    else:

        discount = 0

    discount = min(
        discount,
        subtotal + delivery_fee
    )

    total_amount = round(
        subtotal + delivery_fee - discount,
        2
    )

    payment_method = random.choice(
        PAYMENT_METHODS
    )

    orders.append({
        "order_id": order_id,
        "user_id": user_id,
        "restaurant_id": restaurant_id,
        "order_date": order_datetime.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "order_status": status,
        "subtotal": subtotal,
        "delivery_fee": delivery_fee,
        "discount": discount,
        "total_amount": total_amount,
        "payment_method": payment_method
    })


# =========================================================
# 5. EVENTS
# =========================================================

events = []

event_id = 1


def add_event(
    user_id,
    event_time,
    event_name,
    restaurant_id=None,
    item_id=None,
    session_id=None
):

    global event_id

    events.append({
        "event_id": event_id,
        "user_id": user_id,
        "event_time": event_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "event_name": event_name,
        "restaurant_id": restaurant_id,
        "item_id": item_id,
        "session_id": session_id
    })

    event_id += 1


# =========================================================
# 5A. ORDER JOURNEYS
# =========================================================

for order in orders:

    user = user_lookup[
        order["user_id"]
    ]

    restaurant_id = order["restaurant_id"]

    user_id = user["user_id"]

    signup_date = datetime.strptime(
        user["signup_date"],
        "%Y-%m-%d"
    ).date()

    base_time = random_datetime_for_user(
        signup_date
    )

    session_id = (
        f"S_ORDER_{order['order_id']:05d}"
    )

    # Select one item from the order
    order_item_rows = [
        row for row in order_items
        if row["order_id"] == order["order_id"]
    ]

    selected_item_id = order_item_rows[0]["item_id"]

    # Small time increments make the journey realistic
    add_event(
        user_id,
        base_time,
        "app_open",
        session_id=session_id
    )

    add_event(
        user_id,
        base_time + timedelta(seconds=20),
        "restaurant_view",
        restaurant_id=restaurant_id,
        session_id=session_id
    )

    add_event(
        user_id,
        base_time + timedelta(seconds=50),
        "item_view",
        restaurant_id=restaurant_id,
        item_id=selected_item_id,
        session_id=session_id
    )

    add_event(
        user_id,
        base_time + timedelta(minutes=2),
        "add_to_cart",
        restaurant_id=restaurant_id,
        item_id=selected_item_id,
        session_id=session_id
    )

    add_event(
        user_id,
        base_time + timedelta(minutes=4),
        "checkout_start",
        restaurant_id=restaurant_id,
        session_id=session_id
    )

    # Payment attempt
    if order["order_status"] in [
        "Completed",
        "Payment Failed"
    ]:

        add_event(
            user_id,
            base_time + timedelta(minutes=5),
            "payment_attempt",
            restaurant_id=restaurant_id,
            session_id=session_id
        )

    # Completed order
    if order["order_status"] == "Completed":

        add_event(
            user_id,
            base_time + timedelta(minutes=6),
            "order_completed",
            restaurant_id=restaurant_id,
            session_id=session_id
        )


# =========================================================
# 5B. BROWSING JOURNEYS
# =========================================================

for browse_number in range(
    1,
    NUM_BROWSE_SESSIONS + 1
):

    user = random.choice(users)

    user_id = user["user_id"]

    city = user["city"]

    signup_date = datetime.strptime(
        user["signup_date"],
        "%Y-%m-%d"
    ).date()

    base_time = random_datetime_for_user(
        signup_date
    )

    new_user = is_new_user(
        signup_date,
        base_time
    )

    android = user["device_type"] == "Android"

    restaurant = random.choice(
        restaurants_by_city[city]
    )

    restaurant_id = restaurant["restaurant_id"]

    selected_item = random.choice(
        restaurant_to_items[restaurant_id]
    )

    session_id = (
        f"S_BROWSE_{browse_number:05d}"
    )

    # -----------------------------
    # Mandatory funnel beginning
    # -----------------------------

    add_event(
        user_id,
        base_time,
        "app_open",
        session_id=session_id
    )

    add_event(
        user_id,
        base_time + timedelta(seconds=20),
        "restaurant_view",
        restaurant_id=restaurant_id,
        session_id=session_id
    )

    add_event(
        user_id,
        base_time + timedelta(seconds=50),
        "item_view",
        restaurant_id=restaurant_id,
        item_id=selected_item["item_id"],
        session_id=session_id
    )

    # -----------------------------
    # Add to cart
    # -----------------------------

    add_to_cart_probability = 0.58

    if android:
        add_to_cart_probability -= 0.08

    if new_user:
        add_to_cart_probability -= 0.07

    if random.random() < add_to_cart_probability:

        add_event(
            user_id,
            base_time + timedelta(minutes=2),
            "add_to_cart",
            restaurant_id=restaurant_id,
            item_id=selected_item["item_id"],
            session_id=session_id
        )

        # -----------------------------
        # Checkout
        # -----------------------------

        checkout_probability = 0.76

        if android:
            checkout_probability -= 0.08

        if new_user:
            checkout_probability -= 0.10

        if random.random() < checkout_probability:

            add_event(
                user_id,
                base_time + timedelta(minutes=4),
                "checkout_start",
                restaurant_id=restaurant_id,
                session_id=session_id
            )

            # -----------------------------
            # Payment attempt
            # -----------------------------

            payment_probability = 0.78

            if android:
                payment_probability -= 0.08

            if new_user:
                payment_probability -= 0.08

            if random.random() < payment_probability:

                add_event(
                    user_id,
                    base_time + timedelta(minutes=5),
                    "payment_attempt",
                    restaurant_id=restaurant_id,
                    session_id=session_id
                )


# =========================================================
# 6. WRITE CSV FILES
# =========================================================

write_csv(
    "users.csv",
    users,
    [
        "user_id",
        "signup_date",
        "city",
        "age_group",
        "device_type",
        "acquisition_channel"
    ]
)

write_csv(
    "restaurants.csv",
    restaurants,
    [
        "restaurant_id",
        "restaurant_name",
        "city",
        "cuisine",
        "rating",
        "delivery_time"
    ]
)

write_csv(
    "menu_items.csv",
    menu_items,
    [
        "item_id",
        "restaurant_id",
        "item_name",
        "category",
        "price"
    ]
)

write_csv(
    "orders.csv",
    orders,
    [
        "order_id",
        "user_id",
        "restaurant_id",
        "order_date",
        "order_status",
        "subtotal",
        "delivery_fee",
        "discount",
        "total_amount",
        "payment_method"
    ]
)

write_csv(
    "order_items.csv",
    order_items,
    [
        "order_item_id",
        "order_id",
        "item_id",
        "quantity",
        "price"
    ]
)

write_csv(
    "events.csv",
    events,
    [
        "event_id",
        "user_id",
        "event_time",
        "event_name",
        "restaurant_id",
        "item_id",
        "session_id"
    ]
)


# =========================================================
# 7. FINAL SUMMARY
# =========================================================

print("\n======================================")
print("QUICKBITE DATA GENERATION COMPLETE")
print("======================================")

print(f"Users:          {len(users):,}")
print(f"Restaurants:    {len(restaurants):,}")
print(f"Menu Items:     {len(menu_items):,}")
print(f"Orders:         {len(orders):,}")
print(f"Order Items:    {len(order_items):,}")
print(f"Events:         {len(events):,}")

print("\nFiles saved inside:")
print(OUTPUT_DIR.resolve())

print("\nNext step:")
print("Import the CSV files into MySQL Workbench.")