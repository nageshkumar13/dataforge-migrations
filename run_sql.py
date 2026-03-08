import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

SQL_DIR = "sql"

def execute_sql_files():

    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    try:

        files = sorted(os.listdir(SQL_DIR))
        
        for file in files:

            if file.endswith(".sql"):

                path = os.path.join(SQL_DIR, file)

                print(f"\nRunning {file}...")

                with open(path, "r") as f:
                    sql = f.read()

                cursor.execute(sql)
                conn.commit()

                print(f"{file} executed successfully")

        print("\nAll SQL files executed.")

    except Exception as e:

        conn.rollback()
        print("Error occurred:", e)

    finally:

        cursor.close()
        conn.close()


if __name__ == "__main__":
    execute_sql_files()