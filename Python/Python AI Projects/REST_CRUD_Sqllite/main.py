
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# 1. Database connection
def get_db():
    conn = sqlite3.connect("employees.db") #automatically creates a DB
    conn.row_factory = sqlite3.Row
    return conn


conn = get_db()
# 2. Create table

conn.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        salary REAL NOT NULL,
        department TEXT NOT NULL
    )
""")

conn.commit()
conn.close()


# 3. Pydantic model
class Employee(BaseModel): #Inheritance class Employee inherits BaseModel class
    name: str
    salary: float
    department: str


# 4. CREATE
@app.post("/employees")
def add_employee(emp: Employee):

    conn = get_db()

    cursor = conn.execute(
        "INSERT INTO employees (name, salary, department) VALUES (?, ?, ?)",
        (emp.name, emp.salary, emp.department)
    )

    conn.commit()

    emp_id = cursor.lastrowid

    conn.close()

    return {"message": "Employee added", "id": emp_id}


# 5. READ ALL
@app.get("/employees")
def get_employees():

    conn = get_db()

    rows = conn.execute(
        "SELECT * FROM employees"
    ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


# 6. READ BY ID
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):

    conn = get_db()

    row = conn.execute(
        "SELECT * FROM employees WHERE id = ?",
        (emp_id,)
    ).fetchone()

    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return dict(row)


# 7. UPDATE
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp: Employee):

    conn = get_db()

    cursor = conn.execute(
        """
        UPDATE employees
        SET name = ?, salary = ?, department = ?
        WHERE id = ?
        """,
        (emp.name, emp.salary, emp.department, emp_id)
    )

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    if updated == 0:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee updated"}


# 8. DELETE
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):

    conn = get_db()

    cursor = conn.execute(
        "DELETE FROM employees WHERE id = ?",
        (emp_id,)
    )

    conn.commit()

    deleted = cursor.rowcount

    conn.close()

    if deleted == 0:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted"}
