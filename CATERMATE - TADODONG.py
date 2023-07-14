import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox
from datetime import datetime
import sqlite3

conn = sqlite3.connect('MANIFESTING.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customers (customer_id INT, first_name TEXT, middle_name TEXT, surname TEXT, contact_number TEXT, address TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS packages (package_id INT, package_name TEXT, price FLOAT, number_of_pax INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS dishes (dish_id INT, dish_name TEXT, package_id INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS otherservices (service_id INT, package_id INT, service_name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id INT, customer_id INT, package_id INT, transacted_date TEXT, delivery_location TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS payments (payment_id INT, customer_id INT, package_id INT, payment_status TEXT, payment_date TEXT, total_paid FLOAT, total_amount FLOAT)")

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
        for F in (CustomerInfo, PackageInfo, Home, DishInfo, OtherServices , PlaceOrder, PaymentStatus):
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
        
        # Load the first GIF using PIL
        gif_path = r"C:\Users\admin\CaterMate01.gif"
        gif_image = Image.open(gif_path)

        # Convert the first GIF frames to PIL Image objects
        pil_frames = []
        for frame in ImageSequence.Iterator(gif_image):
            pil_frame = frame.convert("RGBA")  # Convert to RGBA mode
            pil_frames.append(pil_frame)

        # Create a list to store the first PhotoImage objects
        self.gif_frames = []

        # Convert the PIL Image objects to Tkinter-compatible PhotoImage objects
        for frame in pil_frames:
            photo = ImageTk.PhotoImage(frame)
            self.gif_frames.append(photo)

        self.current_frame = 0  # Track the current frame index
        self.label_gif_display = tk.Label(self, bd=10, relief="sunken")  # Set bd=10 for the border width
        self.label_gif_display.place(x=0, y=5, width=920, height=650)



        # Load the second GIF using PIL
        gif_path2 = r"C:\Users\admin\CaterMate0234.gif"
        gif_image2 = Image.open(gif_path2)

        # Convert the second GIF frames to PIL Image objects
        pil_frames2 = []
        for frame2 in ImageSequence.Iterator(gif_image2):
            pil_frame2 = frame2.convert("RGBA")  # Convert to RGBA mode
            pil_frames2.append(pil_frame2)

        # Create a list to store the second PhotoImage objects
        self.gif_frames2 = []

        # Convert the PIL Image objects to Tkinter-compatible PhotoImage objects
        for frame2 in pil_frames2:
            photo2 = ImageTk.PhotoImage(frame2)
            self.gif_frames2.append(photo2)

        self.current_frame2 = 0  # Track the current frame index for the second GIF

        self.label_gif_display2 = tk.Label(self, bd=10, relief="sunken")  # Set bd=10 for the border width
        self.label_gif_display2.place(x=920, y=5, width=450, height=650)
        
        self.label_text = tk.Label(self, bg="darkolivegreen", fg="white")
        self.label_text.place(x=0, y=665, width=1400, height=40)
        
        self.update_gif()
        self.update_gif2()
        

        self.customers_count_label = tk.Label(self, font=("Courier", 14), bg="darkolivegreen", fg="white")
        self.customers_count_label.place(x=10, y=670)

        self.packages_count_label = tk.Label(self, font=("Courier", 14), bg="darkolivegreen", fg="white")
        self.packages_count_label.place(x=600, y=670)

        self.orders_count_label = tk.Label(self, font=("Courier", 14), bg="darkolivegreen", fg="white")
        self.orders_count_label.place(x=1125, y=670)

        self.update_counts()

        button_courses = tk.Button(self, text="COSTUMER'S INFO", font=("Courier", 16), bd=9, width=20, height=1,
                                   fg="white", bg="darkslategray", relief='ridge',
                                   command=lambda: controller.show(CustomerInfo))
        button_courses.place(x=1020, y=100)
        button_courses.config(cursor="hand2")

        button_courses = tk.Button(self, text="PACKAGE INFORMATION", font=("Courier", 16), bd=9, width=20, height=1,
                                   fg="white", bg="darkslategray", relief='ridge',
                                   command=lambda: controller.show(PackageInfo))
        button_courses.place(x=1020, y=175)
        button_courses.config(cursor="hand2")
        
        button_courses = tk.Button(self, text="DISH MENU", font=("Courier", 16), bd=9, width=20, height=1,
                        fg="white", bg="darkslategray", relief='ridge',
                        command=lambda: controller.show(DishInfo))
        button_courses.place(x=1020, y=250)
        button_courses.config(cursor="hand2")
        
        button_courses = tk.Button(self, text="SERVICES", font=("Courier", 16), bd=9, width=20, height=1,
                        fg="white", bg="darkslategray", relief='ridge',
                        command=lambda: controller.show(OtherServices))
        button_courses.place(x=1020, y=325)
        button_courses.config(cursor="hand2")
        
        button_courses = tk.Button(self, text="PLACE ORDER", font=("Courier", 16), bd=9, width=20, height=1,
                                   fg="white", bg="darkslategray", relief='ridge',
                                   command=lambda: controller.show(PlaceOrder))
        button_courses.place(x=1020, y=400)
        button_courses.config(cursor="hand2")

        button_registration = tk.Button(self, text="PAYMENT STATUS", font=("Courier", 15), bd=9, width=22,
                                         height=1, fg="white", bg="darkslategray", relief='ridge',
                                         command=lambda: controller.show(PaymentStatus))
        button_registration.place(x=1020, y=475)
        button_registration.config(cursor="hand2")  
        
        button_exit = tk.Button(self, text="EXIT", font=("Courier", 16), bd=9, width=20,
                                height=1, fg="white", bg="darkslategray", relief='ridge',
                                command=iExit)
        button_exit.place(x=1020, y=550)
        button_exit.config(cursor="hand2") 
        
    def update_gif(self):
        self.label_gif_display.config(image=self.gif_frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.label_gif_display.after(100, self.update_gif)

    def update_gif2(self):
        self.label_gif_display2.config(image=self.gif_frames2[self.current_frame2])
        self.current_frame2 = (self.current_frame2 + 1) % len(self.gif_frames2)
        self.label_gif_display2.after(100, self.update_gif2)
        
    def update_counts(self):
        cursor.execute("SELECT COUNT(*) FROM customers")
        customers_count = cursor.fetchone()[0]
        self.customers_count_label.config(text="Number of Customers: {}".format(customers_count))

        cursor.execute("SELECT COUNT(*) FROM packages")
        packages_count = cursor.fetchone()[0]
        self.packages_count_label.config(text="Number of Packages: {}".format(packages_count))

        cursor.execute("SELECT COUNT(*) FROM orders")
        orders_count = cursor.fetchone()[0]
        self.orders_count_label.config(text="Number of Orders: {}".format(orders_count))

        self.after(5000, self.update_counts)
      
        
class CustomerInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Main Color for the Home Page
        label = tk.Label(self, font=("Times New Roman", 40),bg=("darkslategrey"),fg=("darkslategray"))
        label.place(x=0,y=0,width=1400,height=800)
        
        # Top Title Frame
        self.lblccode = tk.Label(self, font=("Times New Roman", 30, "bold"),bd=5,bg=("darkslategray"),fg=("white"),text="CUSTOMER'S INFORMATION", padx=2, pady=4)
        self.lblccode.place(x=250,y=20,width=880)
        
        # Home Button
        home = tk.Button(self, text="HOME",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(Home))
        home.place(x=1200,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Place Order Button
        home = tk.Button(self, text="ORDERS",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PlaceOrder))
        home.place(x=110,y=50, height=35, width=150, anchor="center")
        home.config(cursor= "hand2")
        
        # Place Order Button
        home = tk.Button(self, text="PACKAGE INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PackageInfo))
        home.place(x=270,y=50, height=35, width=150, anchor="center")
        home.config(cursor= "hand2")

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("CustomerID", "FirstName", "MiddleName", "Surname", "ContactNumber", "Address")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("CustomerID", anchor="w")
        self.tree.column("FirstName", anchor="w")
        self.tree.column("MiddleName", anchor="w")
        self.tree.column("Surname", anchor="w")
        self.tree.column("ContactNumber", anchor="w")
        self.tree.column("Address", anchor="w")
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("FirstName", text="First Name")
        self.tree.heading("MiddleName", text="Middle Name")
        self.tree.heading("Surname", text="Surname")
        self.tree.heading("ContactNumber", text="Contact Number")
        self.tree.heading("Address", text="Address")
        self.tree.place(x=30, y=100, width=1300, height=225)     

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=1330, y=100, height=225)

        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.populate_treeview()

        self.customer_id_entry = tk.Entry(self)
        self.customer_id_entry.place(x=300, y=350, width=350, height=30)
        self.customer_id_label = tk.Label(self, text="Customer ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.customer_id_label.place(x=35, y=350)

        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.place(x=300, y=400, width=350, height=30)
        self.first_name_label = tk.Label(self, text="First Name:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.first_name_label.place(x=35, y=400)

        self.middle_name_entry = tk.Entry(self)
        self.middle_name_entry.place(x=300, y=450, width=350, height=30)
        self.middle_name_label = tk.Label(self, text="Middle Name:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.middle_name_label.place(x=35, y=450)

        self.surname_entry = tk.Entry(self)
        self.surname_entry.place(x=300, y=500, width=350, height=30)
        self.surname_label = tk.Label(self, text="Surname:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.surname_label.place(x=35, y=500)

        self.contact_number_entry = tk.Entry(self)
        self.contact_number_entry.place(x=300, y=550, width=350, height=30)
        self.contact_number_label = tk.Label(self, text="Contact Number:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.contact_number_label.place(x=35, y=550)

        self.address_entry = tk.Entry(self)
        self.address_entry.place(x=300, y=600, width=350, height=30)
        self.address_label = tk.Label(self, text="Address:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.address_label.place(x=35, y=600)

        self.add_customer_button = tk.Button(self, text="Add Customer", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.add_customer)
        self.add_customer_button.place(x=700, y=450, width=300, height=70)
        
        self.delete_customer_button = tk.Button(self, text="Delete Customer", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.delete_customer)
        self.delete_customer_button.place(x=1025, y=450, width=300, height=70)

        self.edit_customer_button = tk.Button(self, text="Edit Customer", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.edit_customer)
        self.edit_customer_button.place(x=700, y=540, width=300, height=70)

        self.update_customer_button = tk.Button(self, text="Update Customer", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.update_customer)
        self.update_customer_button.place(x=1025, y=540, width=300, height=70)

        self.display_all_button = tk.Button(self, text="Display All", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.display_all_customers)
        self.display_all_button.place(x=1090, y=350, width=120, height=40)

        self.clear_button = tk.Button(self, text="Clear", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.clear_entries)
        self.clear_button.place(x=1220, y=350, width=100, height=40)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x=810, y=350, width=270, height=40)

        self.search_button = tk.Button(self, text="Search", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.search_customer)
        self.search_button.place(x=700, y=350, width=100, height=40)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()

        for customer in customers:
            self.tree.insert("", "end", values=customer)

    def add_customer(self):
        customer_id = self.customer_id_entry.get()
        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        surname = self.surname_entry.get()
        contact_number = self.contact_number_entry.get()
        address = self.address_entry.get()

        # Check if customer ID already exists
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id = ?", (customer_id,))
        result_customer = cursor.fetchone()

        if result_customer is not None:
            messagebox.showerror("Add Customer", "Customer ID already exists.")
            return

        # Check if any required field is empty
        if any(field == "" for field in [customer_id, first_name, surname, contact_number, address]):
            messagebox.showerror("Add Customer", "Please fill in all customer information.")
            return

        cursor.execute("INSERT INTO customers (customer_id, first_name, middle_name, surname, contact_number, address) VALUES (?, ?, ?, ?, ?, ?)",
                    (customer_id, first_name, middle_name, surname, contact_number, address))
        conn.commit()
        self.populate_treeview()
        self.clear_entries()
        messagebox.showinfo("Add Customer", "Customer added successfully.")

    def clear_entries(self):
        self.customer_id_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        
    def delete_customer(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Delete Customer", "No customer selected.")
            return

        customer_id = self.tree.item(selected_item, "values")[0]

        # Check if there are associated orders
        cursor.execute("SELECT COUNT(*) FROM orders WHERE customer_id = ?", (customer_id,))
        result_orders = cursor.fetchone()
        order_count = result_orders[0]

        # Check if there are associated payments
        cursor.execute("SELECT COUNT(*) FROM payments WHERE customer_id = ?", (customer_id,))
        result_payments = cursor.fetchone()
        payment_count = result_payments[0]

        if order_count > 0 or payment_count > 0:
            messagebox.showerror("Delete Customer", "Cannot delete customer with associated orders or payments.")
            return

        # Confirm the deletion
        confirm = messagebox.askyesno("Delete Customer", f"Are you sure you want to delete Customer ID {customer_id}?")

        if confirm:
            cursor.execute("DELETE FROM customers WHERE customer_id = ?", (customer_id,))
            conn.commit()
            self.populate_treeview()
            messagebox.showinfo("Delete Customer", "Customer deleted successfully.")

  
            
    def edit_customer(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Edit Customer", "No customer selected.")
            return

        customer_id = self.tree.item(selected_item, "values")[0]
        first_name = self.tree.item(selected_item, "values")[1]
        middle_name = self.tree.item(selected_item, "values")[2]
        last_name = self.tree.item(selected_item, "values")[3]
        contact_number = self.tree.item(selected_item, "values")[4]
        address = self.tree.item(selected_item, "values")[5]

        self.customer_id_entry.delete(0, tk.END)
        self.customer_id_entry.insert(tk.END, customer_id)

        self.first_name_entry.delete(0, tk.END)
        self.first_name_entry.insert(tk.END, first_name)

        self.middle_name_entry.delete(0, tk.END)
        self.middle_name_entry.insert(tk.END, middle_name)

        self.surname_entry.delete(0, tk.END)
        self.surname_entry.insert(tk.END, last_name)

        self.contact_number_entry.delete(0, tk.END)
        self.contact_number_entry.insert(tk.END, contact_number)

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(tk.END, address)

    def update_customer(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Update Customer", "No customer selected.")
            return

        customer_id = self.customer_id_entry.get()
        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.surname_entry.get()
        contact_number = self.contact_number_entry.get()
        address = self.address_entry.get()

        # Update customer in the database
        cursor.execute("UPDATE customers SET customer_id=?, first_name=?, middle_name=?, surname=?, contact_number=?, address=? WHERE customer_id=?",
                       (customer_id, first_name, middle_name, last_name, contact_number, address, customer_id))
        conn.commit()
        self.populate_treeview()
        self.clear_entries()
        messagebox.showinfo("Update Customer", "Customer updated successfully.")  
        
    def display_all_customers(self):
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)
            
    def search_customer(self):
        search_term = self.search_entry.get()
        cursor.execute("SELECT * FROM customers WHERE customer_id LIKE ? OR first_name LIKE ? OR surname LIKE ?",
                       (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)  
        
        
class PackageInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Main Color for the Home Page
        label = tk.Label(self, text="COURSES", font=("Times New Roman", 40),bg=("darkslategray"),fg=("darkslategray"))
        label.place(x=0,y=0,width=1400,height=800)
        
        # Top Title Frame
        self.lblccode = tk.Label(self, font=("Times New Roman", 30, "bold"),bd=5,bg=("darkslategray"),fg=("white"),text="PACKAGE INFORMATION", padx=2, pady=4)
        self.lblccode.place(x=250,y=20,width=880)
        
        # Home Button
        home = tk.Button(self, text="HOME",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(Home))
        home.place(x=1250,y=50, height=35, width=150, anchor="center")
        home.config(cursor= "hand2")
        
        # Customer Information Button
        home = tk.Button(self, text="DISHES",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(DishInfo))
        home.place(x=120,y=50, height=35, width=150, anchor="center")
        home.config(cursor= "hand2")
        
        # Package Information Button
        home = tk.Button(self, text="SERVICES",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(OtherServices))
        home.place(x=275,y=50, height=35, width=150, anchor="center")
        home.config(cursor= "hand2")
        
        # Package Information Button
        home = tk.Button(self, text="ORDER",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PlaceOrder))
        home.place(x=1095,y=50, height=35, width=150, anchor="center")
        home.config(cursor= "hand2")


        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("PackageID", "PackageName", "Price", "NumberOfPax")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("PackageID", anchor="w")
        self.tree.column("PackageName", anchor="w")
        self.tree.column("Price", anchor="w")
        self.tree.column("NumberOfPax", anchor="w")
        self.tree.heading("PackageID", text="Package ID")
        self.tree.heading("PackageName", text="Package Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("NumberOfPax", text="Number of Pax")
        self.tree.place(x=30, y=100, width=1300, height=225)     

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=1330, y=100, height=225)

        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.populate_treeview()

        self.package_id_entry = tk.Entry(self)
        self.package_id_entry.place(x=300, y=350, width=350, height=40)
        self.package_id_label = tk.Label(self, text="Package ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.package_id_label.place(x=35, y=350)

        self.package_name_entry = tk.Entry(self)
        self.package_name_entry.place(x=300, y=420, width=350, height=40)
        self.package_name_label = tk.Label(self, text="Package Name:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.package_name_label.place(x=35, y=420)

        self.number_of_pax_entry = ttk.Combobox(self, values=["10", "20", "30", "40", "50", "70", "100", "150", "200"])
        self.number_of_pax_entry.place(x=300, y=490, width=350, height=40)
        self.number_of_pax_label = tk.Label(self, text="Number of Pax:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.number_of_pax_label.place(x=35, y=490)
        
        self.price_entry = tk.Entry(self)
        self.price_entry.place(x=300, y=560, width=350, height=40)
        self.price_label = tk.Label(self, text="Price:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.price_label.place(x=35, y=560)

        self.add_package_button = tk.Button(self, text="Add Package", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.add_package)
        self.add_package_button.place(x=700, y=450, width=300, height=70)
        
        self.delete_package_button = tk.Button(self, text="Delete Package", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.delete_package)
        self.delete_package_button.place(x=1025, y=450, width=300, height=70)

        self.edit_package_button = tk.Button(self, text="Edit Package", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.edit_package)
        self.edit_package_button.place(x=700, y=540, width=300, height=70)

        self.update_package_button = tk.Button(self, text="Update Package", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.update_package)
        self.update_package_button.place(x=1025, y=540, width=300, height=70)

        self.display_all_button = tk.Button(self, text="Display All", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.display_all_packages)
        self.display_all_button.place(x=1090, y=350, width=120, height=40)

        self.clear_button = tk.Button(self, text="Clear", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.clear_entries)
        self.clear_button.place(x=1220, y=350, width=100, height=40)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x=810, y=350, width=270, height=40)

        self.search_button = tk.Button(self, text="Search", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.search_package)
        self.search_button.place(x=700, y=350, width=100, height=40)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("SELECT * FROM packages")
        packages = cursor.fetchall()

        for package in packages:
            self.tree.insert("", "end", values=package)

    def add_package(self):
        package_id = self.package_id_entry.get()
        package_name = self.package_name_entry.get()
        price = self.price_entry.get()
        number_of_pax = self.number_of_pax_entry.get()

        # Check if any entry field is empty
        if not all([package_id, package_name, price, number_of_pax]):
            messagebox.showerror("Add Package", "Please fill in all entry fields.")
            return

        # Check if package ID already exists
        cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
        result_package = cursor.fetchone()

        if result_package is not None:
            messagebox.showerror("Add Package", "Package ID already exists.")
        else:
            cursor.execute("INSERT INTO packages (package_id, package_name, price, number_of_pax) VALUES (?, ?, ?, ?)",
                        (package_id, package_name, price, number_of_pax))
            conn.commit()
            self.populate_treeview()
            self.clear_entries()
            messagebox.showinfo("Add Package", "Package added successfully.")

    def delete_package(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Delete Package", "No package selected.")
            return

        package_id = self.tree.item(selected_item, "values")[0]

        # Check if there are associated data connected to the package
        cursor.execute("SELECT COUNT(*) FROM dishes WHERE package_id = ?", (package_id,))
        result = cursor.fetchone()
        dish_count = result[0]

        cursor.execute("SELECT COUNT(*) FROM otherservices WHERE package_id = ?", (package_id,))
        result = cursor.fetchone()
        service_count = result[0]

        cursor.execute("SELECT COUNT(*) FROM orders WHERE package_id = ?", (package_id,))
        result = cursor.fetchone()
        order_count = result[0]
        
        cursor.execute("SELECT COUNT(*) FROM payments WHERE package_id = ?", (package_id,))
        result = cursor.fetchone()
        order_count = result[0]

        if dish_count > 0 or service_count > 0 or order_count > 0:
            messagebox.showerror("Delete Package", "Cannot delete package with associated dishes, services, or orders.")
            return

        # Confirm the deletion
        confirm = messagebox.askyesno("Delete Package", f"Are you sure you want to delete Package ID {package_id}?")

        if confirm:
            cursor.execute("DELETE FROM packages WHERE package_id = ?", (package_id,))
            conn.commit()
            self.populate_treeview()
            messagebox.showinfo("Delete Package", "Package deleted successfully.")

            
    def edit_package(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Edit Package", "No package selected.")
            return

        package_id = self.tree.item(selected_item, "values")[0]
        package_name = self.tree.item(selected_item, "values")[1]
        price = self.tree.item(selected_item, "values")[2]
        number_of_pax = self.tree.item(selected_item, "values")[3]

        self.package_id_entry.delete(0, tk.END)
        self.package_id_entry.insert(tk.END, package_id)

        self.package_name_entry.delete(0, tk.END)
        self.package_name_entry.insert(tk.END, package_name)

        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(tk.END, price)

        self.number_of_pax_entry.delete(0, tk.END)
        self.number_of_pax_entry.insert(tk.END, number_of_pax)

    def update_package(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Update Package", "No package selected.")
            return

        package_id = self.package_id_entry.get()
        package_name = self.package_name_entry.get()
        price = self.price_entry.get()
        number_of_pax = self.number_of_pax_entry.get()

        # Update package in the database
        cursor.execute("UPDATE packages SET package_id=?, package_name=?, price=?, number_of_pax=? WHERE package_id=?",
                    (package_id, package_name, price, number_of_pax, package_id))
        conn.commit()
        self.populate_treeview()
        self.clear_entries()
        messagebox.showinfo("Update Package", "Package updated successfully.")

    def clear_entries(self):
        self.package_id_entry.delete(0, tk.END)
        self.package_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.number_of_pax_entry.delete(0, tk.END)
        
    def display_all_packages(self):
        cursor.execute("SELECT * FROM packages")
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def search_package(self):
        search_term = self.search_entry.get()
        cursor.execute("SELECT * FROM packages WHERE package_id LIKE ? OR package_name LIKE ? OR number_of_pax LIKE?",
                       (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)


class DishInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Main Color for the Home Page
        label = tk.Label(self, text="COURSES", font=("Times New Roman", 40),bg=("darkslategray"),fg=("darkslategray"))
        label.place(x=0,y=0,width=1400,height=800)
        
        # Top Title Frame
        self.lblccode = tk.Label(self, font=("Times New Roman", 30, "bold"),bd=5,bg=("darkslategray"),fg=("white"),text="DISH MENU", padx=2, pady=4)
        self.lblccode.place(x=250,y=20,width=880)
        
        # Home Button
        home = tk.Button(self, text="HOME",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(Home))
        home.place(x=1200,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Place Order Button
        home = tk.Button(self, text="PACKAGE INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PackageInfo))
        home.place(x=180,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("DishID", "DishName", "PackageID")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("DishID", anchor="w")
        self.tree.column("DishName", anchor="w")
        self.tree.column("PackageID", anchor="w")
        self.tree.heading("DishID", text="Dish ID")
        self.tree.heading("DishName", text="Dish Name")
        self.tree.heading("PackageID", text="Package ID")
        self.tree.place(x=30, y=100, width=1300, height=225)     

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=1330, y=100, height=225)

        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.dish_id_entry = tk.Entry(self)
        self.dish_id_entry.place(x=300, y=350, width=350, height=40)
        self.dish_id_label = tk.Label(self, text="Dish ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.dish_id_label.place(x=35, y=350)

        self.dish_name_entry = tk.Entry(self)
        self.dish_name_entry.place(x=300, y=420, width=350, height=40)
        self.dish_name_label = tk.Label(self, text="Dish Name:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.dish_name_label.place(x=35, y=420)

        self.package_id_entry = tk.Entry(self)
        self.package_id_entry.place(x=300, y=490, width=350, height=40)
        self.package_id_label = tk.Label(self, text="Package ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.package_id_label.place(x=35, y=490)

        self.add_dish_button = tk.Button(self, text="Add Dish", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.add_dish)
        self.add_dish_button.place(x=700, y=450, width=300, height=70)
        
        self.delete_dish_button = tk.Button(self, text="Delete Dish", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.delete_dish)
        self.delete_dish_button.place(x=1025, y=450, width=300, height=70)

        self.edit_dish_button = tk.Button(self, text="Edit Dish", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.edit_dish)
        self.edit_dish_button.place(x=700, y=540, width=300, height=70)

        self.update_dish_button = tk.Button(self, text="Update Dish", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.update_dish)
        self.update_dish_button.place(x=1025, y=540, width=300, height=70)

        self.display_all_button = tk.Button(self, text="Display All", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.display_all_dishes)
        self.display_all_button.place(x=1090, y=350, width=120, height=40)

        self.clear_button = tk.Button(self, text="Clear", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.clear_entries)
        self.clear_button.place(x=1220, y=350, width=100, height=40)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x=810, y=350, width=270, height=40)

        self.search_button = tk.Button(self, text="Search", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.search_dish)
        self.search_button.place(x=700, y=350, width=100, height=40)

        self.populate_treeview()

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("SELECT dish_id, dish_name, package_id FROM dishes")
        dishes = cursor.fetchall()

        for dish in dishes:
            self.tree.insert("", "end", values=dish)


    def add_dish(self):
        dish_id = self.dish_id_entry.get()
        dish_name = self.dish_name_entry.get()
        package_id = self.package_id_entry.get()

        # Check if any field is empty
        if not all([dish_id, dish_name, package_id]):
            messagebox.showerror("Add Dish", "Please fill in all fields.")
            return

        # Check if dish ID already exists
        cursor.execute("SELECT dish_id FROM dishes WHERE dish_id = ?", (dish_id,))
        result_dish = cursor.fetchone()

        if result_dish is not None:
            messagebox.showerror("Add Dish", "Dish ID already exists.")
        else:
            # Validate if package ID exists
            cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
            result_package = cursor.fetchone()

            if result_package is not None:
                cursor.execute("INSERT INTO dishes (dish_id, dish_name, package_id) VALUES (?, ?, ?)",
                            (dish_id, dish_name, package_id))
                conn.commit()
                self.populate_treeview()
                self.clear_entries()
                messagebox.showinfo("Add Dish", "Dish added successfully.")
            else:
                messagebox.showerror("Add Dish", "Invalid Package ID.")


    def clear_entries(self):
        self.dish_id_entry.delete(0, tk.END)
        self.dish_name_entry.delete(0, tk.END)
        self.package_id_entry.delete(0, tk.END)
        
    def delete_dish(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Delete Dish", "No dish selected.")
            return

        dish_id = self.tree.item(selected_item, "values")[0]
        confirm = messagebox.askyesno("Delete Dish", f"Are you sure you want to delete Dish ID {dish_id}?")

        if confirm:
            cursor.execute("DELETE FROM dishes WHERE dish_id = ?", (dish_id,))
            conn.commit()
            self.populate_treeview()
            messagebox.showinfo("Delete Dish", "Dish deleted successfully.")
            
    def edit_dish(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Edit Dish", "No dish selected.")
            return

        dish_id = self.tree.item(selected_item, "values")[0]
        dish_name = self.tree.item(selected_item, "values")[1]
        package_id = self.tree.item(selected_item, "values")[2]

        self.dish_id_entry.delete(0, tk.END)
        self.dish_id_entry.insert(tk.END, dish_id)

        self.dish_name_entry.delete(0, tk.END)
        self.dish_name_entry.insert(tk.END, dish_name)

        self.package_id_entry.delete(0, tk.END)
        self.package_id_entry.insert(tk.END, package_id)

    def update_dish(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Update Dish", "No dish selected.")
            return

        dish_id = self.dish_id_entry.get()
        dish_name = self.dish_name_entry.get()
        package_id = self.package_id_entry.get()

        # Validate if package ID exists
        cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
        result_package = cursor.fetchone()

        if result_package is not None:
            # Update dish in the database
            cursor.execute("UPDATE dishes SET dish_id=?, dish_name=?, package_id=? WHERE dish_id=?",
                        (dish_id, dish_name, package_id, dish_id))
            conn.commit()
            self.populate_treeview()
            self.clear_entries()
            messagebox.showinfo("Update Dish", "Dish updated successfully.")
        else:
            messagebox.showerror("Update Dish", "Invalid Package ID. Cannot update dish.")

    def display_all_dishes(self):
        cursor.execute("SELECT * FROM dishes")
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def search_dish(self):
        search_term = self.search_entry.get()
        cursor.execute("SELECT * FROM dishes WHERE dish_id LIKE ? OR dish_name LIKE ? OR package_id LIKE ?",
                    (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)


class OtherServices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Main Color for the Home Page
        label = tk.Label(self, text="COURSES", font=("Times New Roman", 40),bg=("darkslategray"),fg=("darkslategray"))
        label.place(x=0,y=0,width=1400,height=800)
        
        # Top Title Frame
        self.lblccode = tk.Label(self, font=("Times New Roman", 30, "bold"),bd=5,bg=("darkslategray"),fg=("white"),text="SERVICES", padx=2, pady=4)
        self.lblccode.place(x=250,y=20,width=880)
        
        # Home Button
        home = tk.Button(self, text="HOME",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(Home))
        home.place(x=1200,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Place Order Button
        home = tk.Button(self, text="PACKAGE INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PackageInfo))
        home.place(x=180,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("ServiceID", "PackageID", "ServiceName")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("ServiceID", anchor="w")
        self.tree.column("PackageID", anchor="w")
        self.tree.column("ServiceName", anchor="w")
        self.tree.heading("ServiceID", text="Service ID")
        self.tree.heading("PackageID", text="Package ID")
        self.tree.heading("ServiceName", text="Service Name")
        self.tree.place(x=30, y=100, width=1300, height=225)     

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=1330, y=100, height=225)

        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.populate_treeview()

        self.service_id_entry = tk.Entry(self)
        self.service_id_entry.place(x=300, y=350, width=350, height=40)
        self.service_id_label = tk.Label(self, text="Service ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.service_id_label.place(x=35, y=350)

        self.package_id_entry = tk.Entry(self)
        self.package_id_entry.place(x=300, y=420, width=350, height=40)
        self.package_id_label = tk.Label(self, text="Package ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.package_id_label.place(x=35, y=420)

        self.service_name_entry = tk.Entry(self)
        self.service_name_entry.place(x=300, y=490, width=350, height=40)
        self.service_name_label = tk.Label(self, text="Service Name:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.service_name_label.place(x=35, y=490)

        self.add_service_button = tk.Button(self, text="Add Service", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.add_service)
        self.add_service_button.place(x=700, y=450, width=300, height=70)
        
        self.delete_service_button = tk.Button(self, text="Delete Service", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.delete_service)
        self.delete_service_button.place(x=1025, y=450, width=300, height=70)

        self.edit_service_button = tk.Button(self, text="Edit Service", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.edit_service)
        self.edit_service_button.place(x=700, y=540, width=300, height=70)

        self.update_service_button = tk.Button(self, text="Update Service", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.update_service)
        self.update_service_button.place(x=1025, y=540, width=300, height=70)

        self.display_all_button = tk.Button(self, text="Display All", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.populate_treeview)
        self.display_all_button.place(x=1090, y=350, width=120, height=40)

        self.clear_button = tk.Button(self, text="Clear", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.clear_entries)
        self.clear_button.place(x=1220, y=350, width=100, height=40)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x=810, y=350, width=270, height=40)

        self.search_button = tk.Button(self, text="Search", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.search_service)
        self.search_button.place(x=700, y=350, width=100, height=40)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("SELECT * FROM otherservices")
        services = cursor.fetchall()

        for service in services:
            self.tree.insert("", "end", values=service)

    def add_service(self):
        service_id = self.service_id_entry.get()
        package_id = self.package_id_entry.get()
        service_name = self.service_name_entry.get()

        # Check if service ID already exists
        cursor.execute("SELECT service_id FROM otherservices WHERE service_id = ?", (service_id,))
        result_service = cursor.fetchone()

        if result_service is not None:
            messagebox.showerror("Add Service", "Service ID already exists.")
        else:
            # Validate if package ID exists
            cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
            result_package = cursor.fetchone()

            if result_package is not None:
                cursor.execute("INSERT INTO otherservices (service_id, package_id, service_name) VALUES (?, ?, ?)",
                               (service_id, package_id, service_name))
                conn.commit()
                self.populate_treeview()
                self.clear_entries()
                messagebox.showinfo("Add Service", "Service added successfully.")
            else:
                messagebox.showerror("Add Service", "Invalid Package ID.")

    def delete_service(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Delete Service", "No service selected.")
            return

        service_id = self.tree.item(selected_item, "values")[0]

        # Confirm the deletion
        confirm = messagebox.askyesno("Delete Service", f"Are you sure you want to delete Service ID {service_id}?")

        if confirm:
            cursor.execute("DELETE FROM otherservices WHERE service_id = ?", (service_id,))
            conn.commit()
            self.populate_treeview()
            messagebox.showinfo("Delete Service", "Service deleted successfully.")

    def edit_service(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Edit Service", "No service selected.")
            return

        service_values = self.tree.item(selected_item, "values")
        self.service_id_entry.delete(0, tk.END)
        self.service_id_entry.insert(tk.END, service_values[0])
        self.package_id_entry.delete(0, tk.END)
        self.package_id_entry.insert(tk.END, service_values[1])
        self.service_name_entry.delete(0, tk.END)
        self.service_name_entry.insert(tk.END, service_values[2])

    def update_service(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Update Service", "No service selected.")
            return

        service_id = self.tree.item(selected_item, "values")[0]
        package_id = self.package_id_entry.get()
        service_name = self.service_name_entry.get()

        # Validate if package ID exists
        cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
        result_package = cursor.fetchone()

        if result_package is not None:
            cursor.execute("UPDATE otherservices SET package_id = ?, service_name = ? WHERE service_id = ?",
                           (package_id, service_name, service_id))
            conn.commit()
            self.populate_treeview()
            self.clear_entries()
            messagebox.showinfo("Update Service", "Service updated successfully.")
        else:
            messagebox.showerror("Update Service", "Invalid Package ID.")

    def search_service(self):
        search_query = self.search_entry.get()

        # Execute the SQL query to search for services based on the search query
        cursor.execute("SELECT * FROM otherservices WHERE service_id = ?", (search_query,))
        search_results = cursor.fetchall()

        # Clear the tree view
        self.tree.delete(*self.tree.get_children())

        if search_results:
            # Insert the search results into the tree view
            for service in search_results:
                self.tree.insert("", "end", values=service)
        else:
            # Display a message if no search results are found
            messagebox.showinfo("Search Service", "No matching services found.")


    def clear_entries(self):
        self.service_id_entry.delete(0, tk.END)
        self.package_id_entry.delete(0, tk.END)
        self.service_name_entry.delete(0, tk.END)


class PlaceOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Main Color for the Home Page
        label = tk.Label(self, text="COURSES", font=("Times New Roman", 40),bg=("darkslategray"),fg=("darkslategray"))
        label.place(x=0,y=0,width=1400,height=800)
        
        # Top Title Frame
        self.lblccode = tk.Label(self, font=("Times New Roman", 30, "bold"),bd=5,bg=("darkslategray"),fg=("white"),text="PLACE ORDER", padx=2, pady=4)
        self.lblccode.place(x=250,y=20,width=880)
        
        # Home Button
        home = tk.Button(self, text="HOME",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(Home))
        home.place(x=1250,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Customer Information Button
        home = tk.Button(self, text="COSTUMER INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(CustomerInfo))
        home.place(x=120,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Package Information Button
        home = tk.Button(self, text="PACKAGE INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PackageInfo))
        home.place(x=320,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Package Information Button
        home = tk.Button(self, text="PAYMENT STATUS",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PaymentStatus))
        home.place(x=1050,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("OrderID", "CustomerID", "PackageID", "TransactedDate", "DeliveryLocation")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("OrderID", anchor="w")
        self.tree.column("CustomerID", anchor="w")
        self.tree.column("PackageID", anchor="w")
        self.tree.column("TransactedDate", anchor="w")
        self.tree.column("DeliveryLocation", anchor="w")
        self.tree.heading("OrderID", text="Order ID")
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("PackageID", text="Package ID")
        self.tree.heading("TransactedDate", text="Transacted Date")
        self.tree.heading("DeliveryLocation", text="Delivery Location")
        self.tree.place(x=30, y=100, width=1300, height=225)     

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=1330, y=100, height=225)

        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.populate_treeview()

        self.order_id_entry = tk.Entry(self)
        self.order_id_entry.place(x=300, y=350, width=350, height=30)
        self.order_id_label = tk.Label(self, text="Order ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.order_id_label.place(x=35, y=350)

        self.customer_id_entry = tk.Entry(self)
        self.customer_id_entry.place(x=300, y=400, width=350, height=30)
        self.customer_id_label = tk.Label(self, text="Customer ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.customer_id_label.place(x=35, y=400)

        self.package_id_entry = tk.Entry(self)
        self.package_id_entry.place(x=300, y=450, width=350, height=30)
        self.package_id_label = tk.Label(self, text="Package ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.package_id_label.place(x=35, y=450)

        self.transacted_date_entry = tk.Entry(self)
        self.transacted_date_entry.place(x=300, y=500, width=350, height=30)
        self.transacted_date_label = tk.Label(self, text="Transacted Date:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.transacted_date_label.place(x=35, y=500)

        self.delivery_location_entry = tk.Entry(self)
        self.delivery_location_entry.place(x=300, y=550, width=350, height=30)
        self.delivery_location_label = tk.Label(self, text="Delivery Location:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.delivery_location_label.place(x=35, y=550)

        self.add_order_button = tk.Button(self, text="Place Order", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.place_order)
        self.add_order_button.place(x=700, y=450, width=300, height=70)
        
        self.delete_order_button = tk.Button(self, text="Delete Order", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.delete_order)
        self.delete_order_button.place(x=1025, y=450, width=300, height=70)

        self.edit_order_button = tk.Button(self, text="Edit Order", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.edit_order)
        self.edit_order_button.place(x=700, y=540, width=300, height=70)

        self.update_order_button = tk.Button(self, text="Update Order", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.update_order)
        self.update_order_button.place(x=1025, y=540, width=300, height=70)

        self.display_all_button = tk.Button(self, text="Display All", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.display_all_orders)
        self.display_all_button.place(x=1090, y=350, width=120, height=40)

        self.clear_button = tk.Button(self, text="Clear", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.clear_entries)
        self.clear_button.place(x=1220, y=350, width=100, height=40)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x=810, y=350, width=270, height=40)

        self.search_button = tk.Button(self, text="Search", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.search_order)
        self.search_button.place(x=700, y=350, width=100, height=40)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

        for order in orders:
            self.tree.insert("", "end", values=order)


    def place_order(self):
        order_id = self.order_id_entry.get()
        customer_id = self.customer_id_entry.get()
        package_id = self.package_id_entry.get()
        transacted_date = self.transacted_date_entry.get()
        delivery_location = self.delivery_location_entry.get()

        # Check if order ID already exists
        cursor.execute("SELECT order_id FROM orders WHERE order_id = ?", (order_id,))
        result_order = cursor.fetchone()

        if result_order is not None:
            messagebox.showerror("Order Rejected", "Order ID already exists.")
            return

        # Validate if customer ID exists
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id = ?", (customer_id,))
        result_customer = cursor.fetchone()

        # Validate if package ID exists
        cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
        result_package = cursor.fetchone()

        if result_customer is not None and result_package is not None:
            cursor.execute("INSERT INTO orders (order_id, customer_id, package_id, transacted_date, delivery_location) VALUES (?, ?, ?, ?, ?)",
                        (order_id, customer_id, package_id, transacted_date, delivery_location))
            conn.commit()
            self.populate_treeview()
            self.clear_entries()
            messagebox.showinfo("Place Order", "Order placed successfully.")
        else:
            messagebox.showerror("Order Rejected", "Invalid Customer ID or Package ID.")

    def clear_entries(self):
        self.order_id_entry.delete(0, tk.END)
        self.customer_id_entry.delete(0, tk.END)
        self.package_id_entry.delete(0, tk.END)
        self.transacted_date_entry.delete(0, tk.END)
        self.delivery_location_entry.delete(0, tk.END)
        
    def delete_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Delete Order", "No order selected.")
            return

        order_id = self.tree.item(selected_item, "values")[0]

        # Confirm the deletion
        confirm = messagebox.askyesno("Delete Order", f"Are you sure you want to delete Order ID {order_id}?")

        if confirm:
            cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
            conn.commit()
            self.populate_treeview()
            messagebox.showinfo("Delete Order", "Order deleted successfully.")

            
    def edit_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Edit Order", "No order selected.")
            return

        order_id = self.tree.item(selected_item, "values")[0]
        customer_id = self.tree.item(selected_item, "values")[1]
        package_id = self.tree.item(selected_item, "values")[2]
        transacted_date = self.tree.item(selected_item, "values")[3]
        delivery_location = self.tree.item(selected_item, "values")[4]

        self.order_id_entry.delete(0, tk.END)
        self.order_id_entry.insert(tk.END, order_id)

        self.customer_id_entry.delete(0, tk.END)
        self.customer_id_entry.insert(tk.END, customer_id)

        self.package_id_entry.delete(0, tk.END)
        self.package_id_entry.insert(tk.END, package_id)

        self.transacted_date_entry.delete(0, tk.END)
        self.transacted_date_entry.insert(tk.END, transacted_date)

        self.delivery_location_entry.delete(0, tk.END)
        self.delivery_location_entry.insert(tk.END, delivery_location)
        
    def update_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Update Order", "No order selected.")
            return

        order_id = self.order_id_entry.get()
        customer_id = self.customer_id_entry.get()
        package_id = self.package_id_entry.get()
        transacted_date = self.transacted_date_entry.get()
        delivery_location = self.delivery_location_entry.get()

        # Check if customer ID exists
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id = ?", (customer_id,))
        result_customer = cursor.fetchone()

        # Check if package ID exists
        cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
        result_package = cursor.fetchone()

        if result_customer is None or result_package is None:
            messagebox.showerror("Update Order", "Invalid Customer ID or Package ID.")
            return

        # Update order in the database
        cursor.execute("UPDATE orders SET order_id=?, customer_id=?, package_id=?, transacted_date=?, delivery_location=? WHERE order_id=?",
                    (order_id, customer_id, package_id, transacted_date, delivery_location, order_id))
        conn.commit()
        self.populate_treeview()
        self.clear_entries()
        messagebox.showinfo("Update Order", "Order updated successfully.")

    def display_all_orders(self):
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def search_order(self):
        search_term = self.search_entry.get()
        cursor.execute("SELECT * FROM orders WHERE order_id LIKE ? OR customer_id LIKE ? OR package_id LIKE ?",
                       (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        rows = cursor.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)


class PaymentStatus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Main Color for the Home Page
        label = tk.Label(self, text="COURSES", font=("Times New Roman", 40),bg=("darkslategray"),fg=("darkslategray"))
        label.place(x=0,y=0,width=1400,height=800)
        
        # Top Title Frame
        self.lblccode = tk.Label(self, font=("Times New Roman", 30, "bold"),bd=5,bg=("darkslategray"),fg=("white"),text="PAYMENT STATUS", padx=2, pady=4)
        self.lblccode.place(x=250,y=20,width=880)
        
        # Home Button
        home = tk.Button(self, text="HOME",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(Home))
        home.place(x=1250,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Customer Information Button
        home = tk.Button(self, text="COSTUMER INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(CustomerInfo))
        home.place(x=120,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Package Information Button
        home = tk.Button(self, text="PACKAGE INFO",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PackageInfo))
        home.place(x=320,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")
        
        # Place Order Button
        home = tk.Button(self, text="ORDERS",font=("Lucida Console",13,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=lambda: controller.show(PlaceOrder))
        home.place(x=1050,y=50, height=35, anchor="center")
        home.config(cursor= "hand2")

        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("PaymentID", "CustomerID", "PackageID", "PaymentStatus", "PaymentDate", "TotalPaid", "TotalAmount")
        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("PaymentID", anchor="w")
        self.tree.column("CustomerID", anchor="w")
        self.tree.column("PackageID", anchor="w")
        self.tree.column("PaymentStatus", anchor="w")
        self.tree.column("PaymentDate", anchor="w")
        self.tree.column("TotalPaid", anchor="w")
        self.tree.column("TotalAmount", anchor="w")
        self.tree.heading("PaymentID", text="Payment ID")
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("PackageID", text="Package ID")
        self.tree.heading("PaymentStatus", text="Payment Status")
        self.tree.heading("PaymentDate", text="Payment Date")
        self.tree.heading("TotalPaid", text="Total Paid")
        self.tree.heading("TotalAmount", text="Total Amount")
        self.tree.place(x=30, y=100, width=1300, height=225)     

        # Create a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.place(x=1330, y=100, height=225)

        # Configure the treeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.populate_treeview()

        self.payment_id_entry = tk.Entry(self)
        self.payment_id_entry.place(x=300, y=350, width=350, height=30)
        self.payment_id_label = tk.Label(self, text="Payment ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.payment_id_label.place(x=35, y=350)

        self.customer_id_entry = tk.Entry(self)
        self.customer_id_entry.place(x=300, y=400, width=350, height=30)
        self.customer_id_label = tk.Label(self, text="Customer ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.customer_id_label.place(x=35, y=400)

        self.package_id_entry = tk.Entry(self)
        self.package_id_entry.place(x=300, y=450, width=350, height=30)
        self.package_id_label = tk.Label(self, text="Package ID:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.package_id_label.place(x=35, y=450)

        self.payment_status_entry = tk.Entry(self)
        self.payment_status_entry.place(x=300, y=500, width=350, height=30)
        self.payment_status_label = tk.Label(self, text="Payment Status:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.payment_status_label.place(x=35, y=500)

        self.payment_date_entry = tk.Entry(self)
        self.payment_date_entry.place(x=300, y=550, width=350, height=30)
        self.payment_date_label = tk.Label(self, text="Payment Date:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.payment_date_label.place(x=35, y=550)

        self.total_paid_entry = tk.Entry(self)
        self.total_paid_entry.place(x=300, y=600, width=350, height=30)
        self.total_paid_label = tk.Label(self, text="Total Paid:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.total_paid_label.place(x=35, y=600)

        self.total_amount_entry = tk.Entry(self)
        self.total_amount_entry.place(x=300, y=650, width=350, height=30)
        self.total_amount_label = tk.Label(self, text="Total Amount:", font=("Sans-serif",15,"bold"), bg="darkslategray", fg="white")
        self.total_amount_label.place(x=35, y=650)

        self.add_payment_button = tk.Button(self, text="Add Payment", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.add_payment)
        self.add_payment_button.place(x=700, y=450, width=300, height=70)
        
        self.delete_payment_button = tk.Button(self, text="Delete Payment", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.delete_payment)
        self.delete_payment_button.place(x=1025, y=450, width=300, height=70)

        self.edit_payment_button = tk.Button(self, text="Edit Payment", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.edit_payment)
        self.edit_payment_button.place(x=700, y=540, width=300, height=70)

        self.update_payment_button = tk.Button(self, text="Update Payment", font=("Lucida Console",12,"bold"),bd=6, width = 16, bg="lightslategray", fg="white", command=self.update_payment)
        self.update_payment_button.place(x=1025, y=540, width=300, height=70)

        self.display_all_button = tk.Button(self, text="Display All", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.populate_treeview)
        self.display_all_button.place(x=1090, y=350, width=120, height=40)

        self.clear_button = tk.Button(self, text="Clear", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.clear_entries)
        self.clear_button.place(x=1220, y=350, width=100, height=40)

        self.search_entry = tk.Entry(self)
        self.search_entry.place(x=810, y=350, width=270, height=40)

        self.search_button = tk.Button(self, text="Search", font=("Lucida Console",11,"bold"),bd=4, width = 16, bg="lightslategray", fg="white", command=self.search_payment)
        self.search_button.place(x=700, y=350, width=100, height=40)

    def populate_treeview(self):
        self.tree.delete(*self.tree.get_children())
        cursor.execute("SELECT * FROM payments")
        payments = cursor.fetchall()

        for payment in payments:
            self.tree.insert("", "end", values=payment)

    def add_payment(self):
        payment_id = self.payment_id_entry.get()
        customer_id = self.customer_id_entry.get()
        package_id = self.package_id_entry.get()
        payment_status = self.payment_status_entry.get()
        payment_date = self.payment_date_entry.get()
        total_paid = self.total_paid_entry.get()
        total_amount = self.total_amount_entry.get()

        # Check if payment ID already exists
        cursor.execute("SELECT payment_id FROM payments WHERE payment_id = ?", (payment_id,))
        result_payment = cursor.fetchone()

        if result_payment is not None:
            messagebox.showerror("Add Payment", "Payment ID already exists.")
        else:
            # Validate if customer ID exists
            cursor.execute("SELECT customer_id FROM customers WHERE customer_id = ?", (customer_id,))
            result_customer = cursor.fetchone()

            # Validate if package ID exists
            cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
            result_package = cursor.fetchone()

            if result_customer is not None and result_package is not None:
                cursor.execute("INSERT INTO payments (payment_id, customer_id, package_id, payment_status, payment_date, total_paid, total_amount) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (payment_id, customer_id, package_id, payment_status, payment_date, total_paid, total_amount))
                conn.commit()
                self.populate_treeview()
                self.clear_entries()
                messagebox.showinfo("Add Payment", "Payment added successfully.")
            else:
                messagebox.showerror("Add Payment", "Invalid Customer ID or Package ID.")

    def delete_payment(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Delete Payment", "No payment selected.")
            return

        confirmation = messagebox.askyesno("Delete Payment", "Are you sure you want to delete the selected payment?")
        if confirmation:
            payment_id = self.tree.item(selected_item, "values")[0]
            cursor.execute("DELETE FROM payments WHERE payment_id = ?", (payment_id,))
            conn.commit()
            self.populate_treeview()
            messagebox.showinfo("Delete Payment", "Payment deleted successfully.")

    def edit_payment(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Edit Payment", "No payment selected.")
            return

        payment_values = self.tree.item(selected_item, "values")
        self.payment_id_entry.delete(0, tk.END)
        self.payment_id_entry.insert(tk.END, payment_values[0])
        self.customer_id_entry.delete(0, tk.END)
        self.customer_id_entry.insert(tk.END, payment_values[1])
        self.package_id_entry.delete(0, tk.END)
        self.package_id_entry.insert(tk.END, payment_values[2])
        self.payment_status_entry.delete(0, tk.END)
        self.payment_status_entry.insert(tk.END, payment_values[3])
        self.payment_date_entry.delete(0, tk.END)
        self.payment_date_entry.insert(tk.END, payment_values[4])
        self.total_paid_entry.delete(0, tk.END)
        self.total_paid_entry.insert(tk.END, payment_values[5])
        self.total_amount_entry.delete(0, tk.END)
        self.total_amount_entry.insert(tk.END, payment_values[6])

    def update_payment(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Update Payment", "No payment selected.")
            return

        payment_id = self.tree.item(selected_item, "values")[0]
        customer_id = self.customer_id_entry.get()
        package_id = self.package_id_entry.get()
        payment_status = self.payment_status_entry.get()
        payment_date = self.payment_date_entry.get()
        total_paid = self.total_paid_entry.get()
        total_amount = self.total_amount_entry.get()

        # Validate if customer ID exists
        cursor.execute("SELECT customer_id FROM customers WHERE customer_id = ?", (customer_id,))
        result_customer = cursor.fetchone()

        # Validate if package ID exists
        cursor.execute("SELECT package_id FROM packages WHERE package_id = ?", (package_id,))
        result_package = cursor.fetchone()

        if result_customer is not None and result_package is not None:
            cursor.execute("UPDATE payments SET customer_id = ?, package_id = ?, payment_status = ?, payment_date = ?, total_paid = ?, total_amount = ? WHERE payment_id = ?",
                           (customer_id, package_id, payment_status, payment_date, total_paid, total_amount, payment_id))
            conn.commit()
            self.populate_treeview()
            self.clear_entries()
            messagebox.showinfo("Update Payment", "Payment updated successfully.")
        else:
            messagebox.showerror("Update Payment", "Invalid Customer ID or Package ID.")

    def search_payment(self):
        search_term = self.search_entry.get()

        cursor.execute("SELECT * FROM paymentS WHERE payment_id LIKE ? OR customer_id LIKE ? OR package_id LIKE ? OR payment_status LIKE ? OR payment_date LIKE ?",
                    (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        payments = cursor.fetchall()

        self.tree.delete(*self.tree.get_children())

        for payment in payments:
            self.tree.insert("", "end", values=payment)

    def clear_entries(self):
        self.payment_id_entry.delete(0, tk.END)
        self.customer_id_entry.delete(0, tk.END)
        self.package_id_entry.delete(0, tk.END)
        self.payment_status_entry.delete(0, tk.END)
        self.payment_date_entry.delete(0, tk.END)
        self.total_paid_entry.delete(0, tk.END)
        self.total_amount_entry.delete(0, tk.END)


def iExit():
    iExit = messagebox.askyesno("CaterMate", "Confirm if you want to exit")
    if iExit > 0:
        app.destroy()

if __name__ == "__main__":
    app = Catermate()
    app.mainloop()

conn.close()
