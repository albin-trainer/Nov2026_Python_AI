# Logged-in employee ID
LOGGED_IN_USER_ID = 101


def get_employee_details(emp_id: int):

    employees = {
        101: {
            "name": "A",
            "department": "IT",
            "salary": 80000
        },
        102: {
            "name": "B",
            "department": "HR",
            "salary": 60000
        },
        103: {
            "name": "C",
            "department": "Finance",
            "salary": 70000
        }
    }

    # SECURITY CHECK
    if emp_id != LOGGED_IN_USER_ID:
        return {
            "error": "Access Denied! You can access only your own details."
        }

    return employees.get(emp_id, {
        "error": "Employee not found"
    })