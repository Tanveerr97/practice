import psycopg2 as psync
from datetime import date

class PostgresConnector:
    def __init__(self, host, database, user, password, port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        try:
            self.connection = psync.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("PostgreSQL connection established.")
            return self.connection
        except psync.Error as e:
            print("Error connecting to PostgreSQL:", e)
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("PostgreSQL connection closed.")

    def create_table(self, table_name):
        if not self.connection:
            print("No active database connection.")
            return

        create_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            s_no SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            topic VARCHAR(200),
            status VARCHAR(20) 
        );
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_query)
                self.connection.commit()
                print(f"Table '{table_name}' created successfully.")
        except Exception as e:
            print("Error creating table:", e)
            self.connection.rollback()

    def show_tables(self):
        if not self.connection:
            print("No active database connection.")
            return

        try:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_type = 'BASE TABLE';
                """)
                tables = cursor.fetchall()
                print("Tables in the database:")
                for table in tables:
                    print("-", table[0])
        except Exception as e:
            print("Error fetching tables:", e)

    def insert_data(self, table_name, date, topic, status):
        if not self.connection:
            print("No active database connection.")
            return

        status = status.lower()

        insert_query = f"""
        INSERT INTO {table_name} (date, topic, status)
        VALUES (%s, %s, %s);
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (date, topic, status))
                self.connection.commit()
                print("Data inserted successfully.")
        except Exception as e:
            print("Error inserting data:", e)
            self.connection.rollback()

    def fetch_all_data(self, table_name):
        if not self.connection:
            print("No active database connection.")
            return

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                print(f"\nData from table '{table_name}':")
                for row in rows:
                    s_no, row_date, topic, status = row
                    print((s_no, row_date.strftime("%Y-%m-%d"), topic, status))
        except Exception as e:
            print("Error fetching data:", e)

    def delete_row_by_sno(self, table_name, s_no):
        if not self.connection:
            print("No active database connection.")
            return

        delete_query = f"""
        DELETE FROM {table_name}
        WHERE s_no = %s;
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(delete_query, (s_no,))
                self.connection.commit()
                print(f"Row with s_no = {s_no} deleted from '{table_name}'.")
        except Exception as e:
            print("Error deleting row:", e)
            self.connection.rollback()

    def reset_serial_sequence(self, table_name, column_name='s_no'):
        if not self.connection:
            print("No active database connection.")
            return

        reset_query = f"""
        SELECT setval(
            pg_get_serial_sequence('{table_name}', '{column_name}'),
            COALESCE((SELECT MAX({column_name}) FROM {table_name}), 0) + 1,
            false
        );
        """

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(reset_query)
                self.connection.commit()
               
        except Exception as e:
            print("Error resetting serial sequence:", e)
            self.connection.rollback()



