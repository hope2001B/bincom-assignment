def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
print(fibonacci(10))

import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    database="babydb",
    user="postgres",
    password="HopeO123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# ✅ Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
""")
conn.commit()

# Add a task
def add_task(task):
    cur.execute("INSERT INTO todos (task) VALUES (%s);", (task,))
    conn.commit()

# List all tasks
def list_tasks():
    cur.execute("SELECT * FROM todos;")
    for row in cur.fetchall():
        print(row)

# Mark a task as done
def mark_done(task_id):
    cur.execute("UPDATE todos SET done = TRUE WHERE id = %s;", (task_id,))
    conn.commit()

# Delete a task
def delete_task(task_id):
    cur.execute("DELETE FROM todos WHERE id = %s;", (task_id,))
    conn.commit()

# Example usage
add_task("Finish assignment")
list_tasks()
mark_done(1)
delete_task(1)

cur.close()
conn.close()

import re
import psycopg2

# Example data
data = "Top baby names: Olivia, Emma, Noah, Liam, Sophia."

# Extract names using regex
names = re.findall(r'\b[A-Z][a-z]+\b', data)

# Connect to PostgreSQL
conn = psycopg2.connect(
    database="babydb",
    user="postgres",
    password="HopeO123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# ✅ Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS babynames (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
""")
conn.commit()

# Insert each name
for name in names:
    cur.execute("INSERT INTO babynames (name) VALUES (%s);", (name,))
conn.commit()

print("Baby names saved to database.")

cur.close()
conn.close()






