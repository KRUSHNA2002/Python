import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="mydb",
            user="postgres",
            password="AI@123456",
            port="5432"
        )
        return conn

    except Exception as e:
        print("Database connection error:", e)
        return None