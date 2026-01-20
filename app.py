import mysql.connector

# ---- RDS MySQL connection details ----
DB_HOST = "database-1.chkmyoawyrbb.ap-south-1.rds.amazonaws.com"
DB_USER = "admin"             # replace with your username
DB_PASSWORD = "admin1234"  # replace with your password
DB_NAME = "testdb"            # replace with your database name

def main():
    try:
        # Connect to RDS MySQL
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        print("Connected to RDS!")

        # ---- 1. Create table ----
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """

        cursor.execute(create_table_sql)
        print("Table 'employees' created (or already exists).")

        # ---- 2. Insert sample data ----
        insert_sql = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        sample_data = [
            ("Priyanka", "Training"),
            ("Alex", "IT"),
            ("Sam", "Finance")
        ]

        cursor.executemany(insert_sql, sample_data)
        conn.commit()
        print("Inserted sample records.")

        # ---- 3. Select all records ----
        cursor.execute("SELECT * FROM employees;")
        rows = cursor.fetchall()

        print("\n---- EMPLOYEES TABLE ----")
        for row in rows:
            print(row)

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
