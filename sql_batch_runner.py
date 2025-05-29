from dotenv import load_dotenv
import os
import oracledb
from time import time
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

user = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
dsn = os.getenv("DB_DSN")

oracledb.init_oracle_client(lib_dir="C:/oracle2/instantclient_23_6")

def connect_database():
    try:
        return oracledb.connect(user=user, password=senha, dsn=dsn)
    except oracledb.Error as e:
        print(f"\n✖ CONNECTION ERROR: {str(e)}")
        raise

def format_time(seconds):
    return f"{seconds:.2f}s"

def execute_operation(title, query, conn, cursor):
    print(f"\n[step] {title}...")
    start = time()
    try:
        cursor.execute(query)
        conn.commit()
        print(f"Completed on {format_time(time() - start)}")
    except Exception as e:
        conn.rollback()
        print(f"✖ Operation error: {str(e)}")
        print("Help: https://docs.oracle.com/error-help/db/")
        return False
    return True

# Steps
# local files with sensitive data (step1.sql, step2.sql, etc.)
def step1(conn, cursor):
    with open("step1.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "1. STEP1", query, conn, cursor
    )

def step2(conn, cursor):
    with open("step2.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "2. STEP2", query, conn, cursor
    )

def step3(conn, cursor):
    with open("step3.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "3. STEP3", query, conn, cursor
    )

def step4(conn, cursor):
    with open("step4.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "4. STEP4", query, conn, cursor
    )

def step5(conn, cursor):
    with open("step5.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "5. STEP5", query, conn, cursor
    )

def step6(conn, cursor):
    with open("step6.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "6. STEP6", query, conn, cursor
    )

def step7(conn, cursor):
    with open("step7.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "7. STEP7", query, conn, cursor
    )

def step8(conn, cursor):
    with open("step8.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "8. STEP8", query, conn, cursor
    )

def step9(conn, cursor):
    with open("step9.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "9. STEP9", query, conn, cursor
    )

def step10(conn, cursor):
    with open("step10.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "10. STEP10", query, conn, cursor
    )

def step11(conn, cursor):
    with open("step11.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "11. STEP11", query, conn, cursor
    )

def step12(conn, cursor):
    with open("step12.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "12. STEP12", query, conn, cursor
    )

def step13(conn, cursor):
    with open("step13.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "13. STEP13", query, conn, cursor
    )  

def step14(conn, cursor):
    with open("step14.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "14. STEP14", query, conn, cursor
    )

def step15(conn, cursor):
    with open("step15.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "15. STEP15", query, conn, cursor
    )

def step16(conn, cursor):
    with open("step16.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "16. STEP16", query, conn, cursor
    )

def step17(conn, cursor):
    with open("step17.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "17. STEP17", query, conn, cursor
    )

def step18(conn, cursor):
    with open("step18.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "18. STEP18", query, conn, cursor
    )

def step19(conn, cursor):
    with open("step19.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "19. STEP19", query, conn, cursor
    )

def step20(conn, cursor):
    with open("step20.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "20. STEP20", query, conn, cursor
    )

def step21(conn, cursor):
    with open("step21.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "21. STEP21", query, conn, cursor
    )

def step22(conn, cursor):
    with open("step22.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "22. STEP22", query, conn, cursor
    )

def step23(conn, cursor):
    with open("step23.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "23. STEP23", query, conn, cursor
    )

def step24(conn, cursor):
    with open("step24.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "24. STEP24", query, conn, cursor
    )

def step25(conn, cursor):
    with open("step25.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "25. STEP25", query, conn, cursor
    )

def step26(conn, cursor):
    with open("step26.sql", "r", encoding="utf-8") as file:
        query = file.read()
    return execute_operation(
        "26. STEP26", query, conn, cursor
    )

def main():
    print("\n" + "=" * 50)
    print(f"START OF PROCESSING - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 50)

    conn = connect_database()
    cursor = conn.cursor()

    steps = [
        ("step 1", step1),
        ("step 2", step2),
        ("step 3", step3),
        ("step 4", step4),
        ("step 5", step5),
        ("step 6", step6),
        ("step 7", step7),
        ("step 8", step8),
        ("step 9", step9),
        ("step 10", step10),
        ("step 11", step11),
        ("step 12", step12),
        ("step 13", step13),
        ("step 14", step14),
        ("step 15", step15),
        ("step 16", step16),
        ("step 17", step17),
        ("step 18", step18),
        ("step 19", step19),
        ("step 20", step20),
        ("step 21", step21),
        ("step 22", step22),
        ("step 23", step23),
        ("step 24", step24),
        ("step 25", step25),
        ("step 26", step26),
    ]

    for name, func in steps:
        try:
            func(conn, cursor)
        except Exception as e:
            print(f"✖ Unexpected failure in {name}: {e}")

    print("\n" + "=" * 50)
    print(f"END OF PROCESSING - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 50)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
