import sqlite3

# Define table names as constants
ADMINS_TABLE = "admins"

# Your code for connecting to the database goes here

# Function to insert admin credentials into the database
def insert_admin_credentials(username, password):
    with sqlite3.connect("chatbot_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {ADMINS_TABLE} (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
# Call the insert_admin_credentials function to add a new admin
new_admin_username = "admin"
new_admin_password = "1234"
insert_admin_credentials(new_admin_username, new_admin_password)
