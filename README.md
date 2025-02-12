# Employee Management System  

## Overview  
The **Employee Management System (EMS)** is a Python-based application that allows users to manage employee records efficiently. It provides functionality for adding, updating, deleting, and searching employee details using an SQLite database.  

## Features  
- Add Employee – Store employee details such as name, age, department, and salary.  
- Search Employee – Retrieve employee records based on various filters.  
- Update Employee – Modify existing employee details.  
- Delete Employee – Remove employee records from the system.  
- Database Storage – Uses SQLite for persistent data storage.  
- GUI Support – Developed using Tkinter for an interactive interface (if applicable).  

## Technologies Used  
| Technology | Description |
|------------|------------|
| Python | Main programming language |
| SQLite | Database management |
| Tkinter | GUI framework (if applicable) |
| SQLAlchemy | ORM for database handling (if used) |

## Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/employee-management-system.git
   cd employee-management-system
   ```

2. **Install dependencies**  
   If your project has a `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**  
   ```bash
   python main.py
   ```

## Database Schema  
The system stores employee details in an SQLite database with the following structure:  

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | INTEGER (Primary Key) | Unique employee ID |
| name | TEXT | Employee's full name |
| age | INTEGER | Employee's age |
| department | TEXT | Department where the employee works |
| salary | REAL | Monthly salary of the employee |

## Usage  
1. Launch the application.  
2. Use the UI (or CLI) to perform operations like adding, updating, and searching employees.  
3. The data is stored persistently in `employees.db` (or another specified database file).  

## Future Enhancements  
- Export employee data to Excel/CSV.  
- Implement user authentication for role-based access.  
- Add REST API support using Flask/Django.  

## Contributing  
Contributions are welcome! Feel free to fork the repository and submit a pull request.  

## Contact Me  
**Name:** Bhumika Murthy  
**Institute:** New Horizon College of Engineering  
**Internship Domain:** Java Development  
**Email:** bhumikamurthy2004@gmail.com  
**Date:** December 1st, 2024  
