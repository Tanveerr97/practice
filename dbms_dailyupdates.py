from dbms_func_dailyupdates import PostgresConnector

db = PostgresConnector(
    host="localhost",
    database="tanveer",
    user="root",
    password="12345"
)

conn = db.connect()
# db.create_table("Daily_updates")
db.show_tables()
db.fetch_all_data("Daily_updates")
db.close()
#db.reset_serial_sequence("Daily_updates")
#db.insert_data("Daily_updates", "2025-04-14", "Send an email with Python using a cron job", "Completed")
#db.delete_row_by_sno("daily_updates", 7)