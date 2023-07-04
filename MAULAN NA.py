import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3

class Catermate(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("CaterMate")
        self.geometry("1482x670")
        self.current_time = tk.StringVar()
        self.current_date = tk.StringVar()
        
        all_frame = tk.Frame(self)
        all_frame.pack(side="top", fill="both", expand=True)
        all_frame.rowconfigure(0, weight=1)
        all_frame.columnconfigure(0, weight=1)
        self.frames = {}
        for F in (TransactionRecords, Home, OrderRepository):
            frame = F(all_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show(Home)
        self.update_time_date()

    def show(self, page_number):
        frame = self.frames[page_number]
        frame.tkraise()

    def update_time_date(self):
        now = datetime.now()
        time_string = now.strftime("%H:%M:%S")
        date_string = now.strftime("%Y-%m-%d")
        self.current_time.set(time_string)
        self.current_date.set(date_string)
        self.after(1000, self.update_time_date)

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label_catermate = tk.Label(self, text="CATERMATE", borderwidth=8, relief="ridge",
                                        font=("Courier", 60, "bold"), bg="darkslategray", fg="white")
        self.label_catermate.place(x=0, y=5, width=920, height=200)

        self.label_time = tk.Label(self, text="Time:", font=("Courier", 14, "bold"),
                                   bg="lightslategray", fg="white")
        self.label_time.place(x=1020, y=200)

        self.label_current_time = tk.Label(self, textvariable=controller.current_time, font=("Courier", 14, "bold"),
                                           bg="lightslategray", fg="white")
        self.label_current_time.place(x=1100, y=200)

        self.label_date = tk.Label(self, text="Date:", font=("Courier", 14, "bold"),
                                   bg="lightslategray", fg="white")
        self.label_date.place(x=1020, y=230)

        self.label_current_date = tk.Label(self, textvariable=controller.current_date, font=("Courier", 14, "bold"),
                                           bg="lightslategray", fg="white")
        self.label_current_date.place(x=1100, y=230)

        self.label_time.lift()  # Bring time label to the front
        self.label_current_time.lift()  # Bring current time label to the front
        self.label_date.lift()  # Bring date label to the front
        self.label_current_date.lift()  # Bring current date label to the front

        self.animate_label()

        label_phrase = tk.Label(self, text="Welcome to CaterMate:\n\n\nYour Order Organizer for Effortless Catering Excellence!",
                                borderwidth=8, relief="ridge", font=("MS Serif", 18),
                                bg="darkslategray", fg="white")
        label_phrase.place(x=0, y=210, width=920, height=445)

        label_vipc = tk.Label(self, text="VIPC", borderwidth=8, relief="raised", font=("Algerian", 29),
                              bg="lightslategray", fg="lightslategray")
        label_vipc.place(x=920, y=5, width=562, height=650)
        
        self.label_time.lift()  # Bring time label to the front of label_vipc
        self.label_current_time.lift()  # Bring current time label to the front of label_vipc
        self.label_date.lift()  # Bring date label to the front of label_vipc
        self.label_current_date.lift()  # Bring current date label to the front of label_vipc

        button_courses = tk.Button(self, text="ORDER REPOSITORY", font=("Courier", 16), bd=7, width=18, height=1,
                                   fg="white", bg="darkslategray", relief='ridge',
                                   command=lambda: controller.show(OrderRepository))
        button_courses.place(x=1020, y=300)
        button_courses.config(cursor="hand2")

        button_registration = tk.Button(self, text="TRANSACTION RECORDS", font=("Courier", 15), bd=7, width=20,
                                         height=1, fg="white", bg="darkslategray", relief='ridge',
                                         command=lambda: controller.show(TransactionRecords))
        button_registration.place(x=1020, y=400)
        button_registration.config(cursor="hand2")

        button_exit = tk.Button(self, text="EXIT", font=("Courier", 16), bd=7, width=18,
                                height=1, fg="white", bg="darkslategray", relief='ridge',
                                command=iExit)
        button_exit.place(x=1020, y=500)
        button_exit.config(cursor="hand2")

    def animate_label(self, font_size=60, direction=1):
        current_font_size = self.label_catermate.cget("font").split(" ")[1]
        current_font_size = int(current_font_size)

        new_font_size = current_font_size + direction

        if new_font_size <= 60:
            direction = 1
        elif new_font_size >= 80:
            direction = -1

        self.label_catermate.config(font=("Courier", new_font_size, "bold"))
        self.label_catermate.after(100, self.animate_label, new_font_size, direction)

class OrderRepository(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Establish a connection to the SQLite database
        self.conn = sqlite3.connect('catermate.db')
        self.cursor = self.conn.cursor()

        # Create the Customer and FoodPackage tables if they don't exist
        self.create_customer_table()
        self.create_food_package_table()

        # Add your code for the OrderRepository screen here

    def create_customer_table(self):
        # Create the Customer table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                middle_name TEXT,
                last_name TEXT,
                contact_number TEXT,
                address TEXT
            )
        ''')
        self.conn.commit()

    def create_food_package_table(self):
        # Create the FoodPackage table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS FoodPackage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                transaction_date TEXT,
                status TEXT,
                delivery_location TEXT,
                number_of_pax INTEGER,
                name TEXT,
                price REAL,
                FOREIGN KEY (customer_id) REFERENCES Customer (id)
            )
        ''')
        self.conn.commit()

        # Add your code for the OrderRepository screen here
        self.configure(bg="darkslategray")

        # Frame for customer information
        info_frame = tk.Frame(self, bg="darkslategray", bd=1)
        info_frame.pack(padx=20, pady=10, anchor="w")

        # Customer's Information Label
        self.label_add_customer = tk.Label(info_frame, text="CUSTOMER'S INFORMATION", font=("Courier", 18, "bold"),
                                           bg="darkslategray", fg="white", bd=30, relief="sunken", highlightthickness=4)
        self.label_add_customer.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        # First Name
        self.label_fname = tk.Label(info_frame, text="First Name:", font=("Courier", 12), bg="lightgray",
                                    anchor="w", bd=4, relief="sunken")
        self.label_fname.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_fname = tk.Entry(info_frame, font=("Courier", 12))
        self.entry_fname.grid(row=1, column=1, sticky="w", pady=5)

        # Middle Name
        self.label_mname = tk.Label(info_frame, text="Middle Name:", font=("Courier", 12), bg="lightgray",
                                    anchor="w", bd=4, relief="sunken")
        self.label_mname.grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_mname = tk.Entry(info_frame, font=("Courier", 12))
        self.entry_mname.grid(row=2, column=1, sticky="w", pady=5)

        # Surname
        self.label_sname = tk.Label(info_frame, text="Surname:", font=("Courier", 12), bg="lightgray",
                                    anchor="w", bd=4, relief="sunken")
        self.label_sname.grid(row=3, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_sname = tk.Entry(info_frame, font=("Courier", 12))
        self.entry_sname.grid(row=3, column=1, sticky="w", pady=5)

        # Customer ID
        self.label_customer_id = tk.Label(info_frame, text="Customer ID:", font=("Courier", 12), bg="lightgray",
                                          anchor="w", bd=4, relief="sunken")
        self.label_customer_id.grid(row=4, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_customer_id = tk.Entry(info_frame, font=("Courier", 12))
        self.entry_customer_id.grid(row=4, column=1, sticky="w", pady=5)

        # Contact Number
        self.label_contact_number = tk.Label(info_frame, text="Contact Number:", font=("Courier", 12),
                                             bg="lightgray", anchor="w", bd=4, relief="sunken")
        self.label_contact_number.grid(row=5, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_contact_number = tk.Entry(info_frame, font=("Courier", 12))
        self.entry_contact_number.grid(row=5, column=1, sticky="w", pady=5)

        # Address
        self.label_address = tk.Label(info_frame, text="Address:", font=("Courier", 12), bg="lightgray",
                                       anchor="w", bd=4, relief="sunken")
        self.label_address.grid(row=6, column=0, sticky="w", padx=(0, 10), pady=5)
        self.entry_address = tk.Entry(info_frame, font=("Courier", 12))
        self.entry_address.grid(row=6, column=1, sticky="w", pady=5)

        # Add Customer Button
        self.button_add_customer = tk.Button(self, text="Add Customer", font=("Courier", 12), command=self.add_customer)
        self.button_add_customer.pack(side="left", anchor="n", padx=225, pady=10)

        self.frame_buttons = tk.Frame(self, bg="darkslategray")
        self.frame_buttons.pack(pady=20)

        # Start the animation
        self.animate_label()

    def animate_label(self):
        alpha = 1.0
        direction = -0.01

        def update_label():
            nonlocal alpha, direction

            alpha += direction
            self.label_add_customer.configure(fg=f"#{int(alpha * 255):02x}{int(alpha * 255):02x}{int(alpha * 255):02x}")

            if alpha <= 0.1 or alpha >= 1.0:
                direction *= -1

            self.after(10, update_label)

        update_label()

    def add_customer(self):
        fname = self.entry_fname.get()
        mname = self.entry_mname.get()
        sname = self.entry_sname.get()
        customer_id = self.entry_customer_id.get()
        contact_number = self.entry_contact_number.get()
        address = self.entry_address.get()

        # Check if any required information is missing
        if not fname or not customer_id:
            messagebox.showerror("Invalid Information", "Please provide at least the first name and customer ID.")
            return

        # Connect to the SQLite database
        conn = sqlite3.connect('catermate.db')
        c = conn.cursor()

        # Insert the customer data into the database
        c.execute("INSERT INTO Customer (first_name, middle_name, last_name, contact_number, address) VALUES (?, ?, ?, ?, ?)",
                (fname, mname, sname, contact_number, address))
        conn.commit()

        # Close the database connection
        conn.close()

        # Show success message
        messagebox.showinfo("Success", "Customer data saved successfully.")

        # Clear the entry fields
        self.entry_fname.delete(0, tk.END)
        self.entry_mname.delete(0, tk.END)
        self.entry_sname.delete(0, tk.END)
        self.entry_customer_id.delete(0, tk.END)
        self.entry_contact_number.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
            
    def read_customer(self):
        # Get the customer ID from the entry field
        customer_id = self.entry_customer_id.get()

        # Fetch customer information from the database based on the customer ID
        # Assuming you have a function called 'fetch_customer_info' that retrieves the customer details
        customer_info = fetch_customer_info(customer_id)

        if customer_info is not None:
            # Populate the entry fields with the retrieved customer information
            self.entry_fname.delete(0, tk.END)
            self.entry_fname.insert(0, customer_info['first_name'])

            self.entry_mname.delete(0, tk.END)
            self.entry_mname.insert(0, customer_info['middle_name'])

            self.entry_sname.delete(0, tk.END)
            self.entry_sname.insert(0, customer_info['surname'])

            self.entry_contact_number.delete(0, tk.END)
            self.entry_contact_number.insert(0, customer_info['contact_number'])

            self.entry_address.delete(0, tk.END)
            self.entry_address.insert(0, customer_info['address'])
        else:
            # Clear the entry fields if customer information is not found
            self.entry_fname.delete(0, tk.END)
            self.entry_mname.delete(0, tk.END)
            self.entry_sname.delete(0, tk.END)
            self.entry_contact_number.delete(0, tk.END)
            self.entry_address.delete(0, tk.END)

            self.button_read_customer = tk.Button(
                self.frame_buttons,
                text="Read Customer",
                font=("Courier", 12),
                command=self.read_customer
            )
            self.button_read_customer.pack(side="left", padx=10)
     
    def __del__(self):
        # Close the database connection when the OrderRepository object is destroyed
        self.cursor.close()
        self.conn.close()

class TransactionRecords(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Add your code for the TransactionRecords screen here


def iExit():
    iExit = messagebox.askyesno("CaterMate", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()


# Create an instance of the Catermate class
root = Catermate()

# Start the main event loop
root.mainloop()
