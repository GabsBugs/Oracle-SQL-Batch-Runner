
# 📂 Oracle SQL Batch Runner

A Python-based automation tool that sequentially executes a series of SQL scripts against an Oracle Database. This utility is designed for environments that require structured database updates, initial data loading, or batch processing of DDL/DML operations.

> ⚠️ Note: The `.env` file and `.sql` script files are intentionally excluded from version control to protect sensitive credentials and business logic.

---

## 🚀 Features

- ✅ Loads environment variables securely from a `.env` file (`DB_USER`, `DB_PASSWORD`, `DB_DSN`)
- ✅ Establishes a robust connection to Oracle using the official `oracledb` library
- ✅ Automatically runs up to 26 SQL scripts in a specified order (`step1.sql` to `step26.sql`)
- ✅ Measures and logs the execution time of each step
- ✅ Provides error handling with transaction rollback and helpful debug messages
- ✅ Outputs clear start and end timestamps for the entire process

---

## 🔧 Requirements

- Python 3.8+
- [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) installed and configured (e.g., `instantclient_23_6`)
- `.env` file with database credentials
- SQL scripts placed in the same directory and named `step1.sql`, `step2.sql`, ..., `step26.sql`

---

## 📁 Example `.env` File

```env
DB_USER=my_user
DB_PASSWORD=my_password
DB_DSN=host:port/service_name
```

> ⚠️ **Important:** Do not commit your `.env` file to version control.

---

## 🏁 How to Run

1. Ensure your Oracle Instant Client path is correctly configured in the Python script (`lib_dir=...`).
2. Place all `.sql` files in the project directory with names matching `step1.sql`, `step2.sql`, etc.
3. Run the script using Python:

```bash
python main.py
```

---

## 📌 Folder Structure

```bash
oracle-sql-batch-runner/
│
├── sql_batch_runner.py 
├── .env                  # Hidden file with DB credentials (excluded from version control)
├── step1.sql             # SQL scripts (also hidden/excluded)
├── step2.sql
├── ...
└── step26.sql
```

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## 🔐 Security Notice

To protect sensitive information:

- The `.env` file (containing credentials) and the `.sql` files (containing potentially sensitive SQL operations) are **not included** in the repository.
- These files should be listed in `.gitignore` and handled securely in your deployment environment.
- Always avoid pushing these files to public repositories.

---

## ✅ Recommended `.gitignore` Example

```gitignore
.env
*.sql
```

---

Feel free to open issues or submit pull requests if you have improvements or bug fixes!
