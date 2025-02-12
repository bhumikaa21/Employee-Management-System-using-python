from tkinter import *
from tkinter import ttk, messagebox, filedialog, simpledialog
from PIL import Image, ImageTk

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1200x600")  # Window size

        # Data storage for employees
        self.employee_data = {}

        # Storage for signed-up users (in-memory for now)
        self.users = {}

        # Start with login page
        self.login_page()

    def login_page(self):
        # Clear any existing widgets from the main window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Centering the login form
        login_frame = Frame(self.root)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        Label(login_frame, text="Login", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        Label(login_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        self.username = Entry(login_frame)
        self.username.grid(row=1, column=1, padx=10)

        Label(login_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
        self.password = Entry(login_frame, show="*")
        self.password.grid(row=2, column=1, padx=10)

        Button(login_frame, text="Login", command=self.login, bg="green", fg="white").grid(row=3, column=0, padx=10, pady=10)
        Button(login_frame, text="Sign Up", command=self.signup_page, bg="blue", fg="white").grid(row=3, column=1, padx=10, pady=10)

    def signup_page(self):
        # Clear the main window and show signup page
        for widget in self.root.winfo_children():
            widget.destroy()

        signup_frame = Frame(self.root)
        signup_frame.place(relx=0.5, rely=0.5, anchor="center")

        Label(signup_frame, text="Sign Up", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        Label(signup_frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        self.new_username = Entry(signup_frame)
        self.new_username.grid(row=1, column=1, padx=10)

        Label(signup_frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
        self.new_password = Entry(signup_frame, show="*")
        self.new_password.grid(row=2, column=1, padx=10)

        Button(signup_frame, text="Sign Up", command=self.signup, bg="blue", fg="white").grid(row=3, column=0, padx=10, pady=10)
        Button(signup_frame, text="Back to Login", command=self.login_page, bg="red", fg="white").grid(row=3, column=1, padx=10, pady=10)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username in self.users and self.users[username] == password:
            self.employee_management_system()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def signup(self):
        new_username = self.new_username.get()
        new_password = self.new_password.get()

        if new_username and new_password:
            if new_username in self.users:
                messagebox.showerror("Error", "Username already exists.")
            else:
                self.users[new_username] = new_password
                messagebox.showinfo("Success", "Signup successful! You can now login.")
                self.login_page()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def employee_management_system(self):
        # Now that the user is logged in, show the employee management system
        for widget in self.root.winfo_children():
            widget.destroy()

        # Header Frame
        header_frame = Frame(self.root, bg="white", height=120)
        header_frame.pack(fill=X, padx=20, pady=10)

        # Placeholder for left and right images
        left_img = Image.open("C:/Users/91987/OneDrive/Desktop/utkarsh/employee/img1.jpg")
        left_img = left_img.resize((150, 120), Image.Resampling.LANCZOS)
        left_img = ImageTk.PhotoImage(left_img)

        right_img = Image.open("C:/Users/91987/OneDrive/Desktop/utkarsh/employee/img2.jpg")
        right_img = right_img.resize((150, 120), Image.Resampling.LANCZOS)
        right_img = ImageTk.PhotoImage(right_img)

        left_label = Label(header_frame, image=left_img, bg="white")
        left_label.image = left_img  # Keep a reference to avoid garbage collection
        left_label.grid(row=0, column=0, padx=10)

        center_label = Label(header_frame, text="EMPLOYEE MANAGEMENT SYSTEM", bg="white", font=("Arial", 20, "bold"))
        center_label.grid(row=0, column=1, padx=10)

        right_label = Label(header_frame, image=right_img, bg="white")
        right_label.image = right_img  # Keep a reference to avoid garbage collection
        right_label.grid(row=0, column=2, padx=10)

        # Employee Details Section
        details_frame = Frame(self.root, bd=2, relief=RIDGE, padx=10, pady=10)
        details_frame.pack(fill=BOTH, padx=20, pady=20)

        Label(details_frame, text="EMPLOYEE DETAILS", font=("Arial", 15, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        # Entry fields
        Label(details_frame, text="Employee ID:").grid(row=1, column=0, sticky=W, pady=5)
        self.emp_id = Entry(details_frame)
        self.emp_id.grid(row=1, column=1, padx=10)

        Label(details_frame, text="Department:").grid(row=1, column=2, sticky=W, pady=5)
        self.department = ttk.Combobox(details_frame, values=["HR", "IT", "Finance"], state="readonly")
        self.department.grid(row=1, column=3, padx=10)

        Label(details_frame, text="Profile Photo:").grid(row=1, column=4, sticky=W, pady=5)
        self.upload_btn = Button(details_frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.grid(row=1, column=5, padx=10)

        self.img_label = Label(details_frame, text="No image selected", bg="white", width=20, height=2)
        self.img_label.grid(row=2, column=5, padx=10)

        Label(details_frame, text="Name:").grid(row=2, column=0, sticky=W, pady=5)
        self.name = Entry(details_frame)
        self.name.grid(row=2, column=1, padx=10)

        Label(details_frame, text="Designation:").grid(row=2, column=2, sticky=W, pady=5)
        self.designation = Entry(details_frame)
        self.designation.grid(row=2, column=3, padx=10)

        Label(details_frame, text="Email:").grid(row=3, column=0, sticky=W, pady=5)
        self.email = Entry(details_frame)
        self.email.grid(row=3, column=1, padx=10)

        Label(details_frame, text="Phone No:").grid(row=3, column=2, sticky=W, pady=5)
        self.phone = Entry(details_frame)
        self.phone.grid(row=3, column=3, padx=10)

        Label(details_frame, text="Gender:").grid(row=4, column=0, sticky=W, pady=5)
        self.gender = StringVar()
        Radiobutton(details_frame, text="Male", variable=self.gender, value="Male").grid(row=4, column=1)
        Radiobutton(details_frame, text="Female", variable=self.gender, value="Female").grid(row=4, column=2)

        Label(details_frame, text="Salary:").grid(row=5, column=0, sticky=W, pady=5)
        self.salary = Entry(details_frame)
        self.salary.grid(row=5, column=1, padx=10)

        Button(details_frame, text="Add Employee", command=self.add_employee, bg="green", fg="white").grid(row=5, column=2, pady=10)
        Button(details_frame, text="Clear", command=self.clear, bg="red", fg="white").grid(row=5, column=3, pady=10)

        Button(details_frame, text="Search Employee", command=self.search_employee).grid(row=6, column=0, pady=10)
        Button(details_frame, text="Update Employee", command=self.update_employee).grid(row=6, column=1, pady=10)
        Button(details_frame, text="Delete Employee", command=self.delete_employee).grid(row=6, column=2, pady=10)

        # Employee Table Section (scrollable)
        table_frame = Frame(self.root)
        table_frame.pack(fill=BOTH, expand=True)

        table_canvas = Canvas(table_frame)
        table_canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar_y = Scrollbar(table_frame, orient=VERTICAL, command=table_canvas.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        table_canvas.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = Scrollbar(table_frame, orient=HORIZONTAL, command=table_canvas.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        table_canvas.configure(xscrollcommand=scrollbar_x.set)

        self.employee_table = ttk.Treeview(table_canvas, columns=("ID", "Name", "Department", "Designation", "Email", "Phone", "Salary"), show="headings")
        table_canvas.create_window((0, 0), window=self.employee_table, anchor=NW)
        self.employee_table.heading("ID", text="Employee ID")
        self.employee_table.heading("Name", text="Name")
        self.employee_table.heading("Department", text="Department")
        self.employee_table.heading("Designation", text="Designation")
        self.employee_table.heading("Email", text="Email")
        self.employee_table.heading("Phone", text="Phone")
        self.employee_table.heading("Salary", text="Salary")

        self.employee_table.bind("<Configure>", lambda e: table_canvas.configure(scrollregion=table_canvas.bbox("all")))

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.profile_image = Image.open(file_path)
            self.profile_image = self.profile_image.resize((100, 100))
            self.profile_image = ImageTk.PhotoImage(self.profile_image)
            self.img_label.config(image=self.profile_image, text="")

    def add_employee(self):
        emp_id = self.emp_id.get()
        name = self.name.get()
        department = self.department.get()
        designation = self.designation.get()
        email = self.email.get()
        phone = self.phone.get()
        gender = self.gender.get()
        salary = self.salary.get()

        # Store the employee details in the dictionary
        self.employee_data[emp_id] = {
            "name": name,
            "department": department,
            "designation": designation,
            "email": email,
            "phone": phone,
            "gender": gender,
            "salary": salary
        }

        self.update_employee_table()
        messagebox.showinfo("Success", "Employee added successfully!")

    def update_employee_table(self):
        # Clear existing table data
        for row in self.employee_table.get_children():
            self.employee_table.delete(row)

        # Insert new data
        for emp_id, emp_details in self.employee_data.items():
            self.employee_table.insert("", "end", values=(
                emp_id,
                emp_details["name"],
                emp_details["department"],
                emp_details["designation"],
                emp_details["email"],
                emp_details["phone"],
                emp_details["salary"]
            ))

    def clear(self):
        self.emp_id.delete(0, END)
        self.name.delete(0, END)
        self.department.set("")
        self.designation.delete(0, END)
        self.email.delete(0, END)
        self.phone.delete(0, END)
        self.salary.delete(0, END)

    def search_employee(self):
        emp_id = simpledialog.askstring("Search Employee", "Enter Employee ID:")

        if emp_id and emp_id in self.employee_data:
            emp = self.employee_data[emp_id]
            emp_details = "\n".join([f"{key}: {value}" for key, value in emp.items()])
            messagebox.showinfo("Employee Found", f"Employee Details:\n{emp_details}")
        else:
            messagebox.showerror("Employee Not Found", "No employee found with that ID.")

    def update_employee(self):
        emp_id = simpledialog.askstring("Update Employee", "Enter Employee ID:")

        if emp_id and emp_id in self.employee_data:
            emp = self.employee_data[emp_id]
            # Populating the form fields with the current data
            self.emp_id.insert(0, emp_id)
            self.name.insert(0, emp["name"])
            self.department.set(emp["department"])
            self.designation.insert(0, emp["designation"])
            self.email.insert(0, emp["email"])
            self.phone.insert(0, emp["phone"])
            self.salary.insert(0, emp["salary"])
            # Allow the user to make changes and save
            self.add_employee()  # Save updated details
        else:
            messagebox.showerror("Employee Not Found", "No employee found with that ID.")

    def delete_employee(self):
        emp_id = simpledialog.askstring("Delete Employee", "Enter Employee ID:")

        if emp_id and emp_id in self.employee_data:
            del self.employee_data[emp_id]
            self.update_employee_table()
            messagebox.showinfo("Success", "Employee deleted successfully!")
        else:
            messagebox.showerror("Employee Not Found", "No employee found with that ID.")

if __name__ == "__main__":
    root = Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
