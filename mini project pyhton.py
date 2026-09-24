import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_FILE = "krish_chaat_corner_300_records.csv"
MENU_FILE = "menu.csv"

ADMIN_PASSWORD = "085"

DEFAULT_MENU = {
    "Sev Puri": 60,
    "Bhel Puri": 50,
    "Ragada Patties": 70,
    "Dahi Ragada Patties": 80,
    "Dahi Puri": 65,
    "Coke": 40,
    "Water Bottle": 20
}

cart = []


def load_menu():

    if not os.path.exists(MENU_FILE):

        menu_df = pd.DataFrame(
            list(DEFAULT_MENU.items()),
            columns=["Item", "Price"]
        )

        menu_df.to_csv(
            MENU_FILE,
            index=False
        )

    menu_df = pd.read_csv(
        MENU_FILE
    )

    menu_df["Price"] = pd.to_numeric(
        menu_df["Price"],
        errors="coerce"
    )

    menu_df = menu_df.dropna()

    return dict(
        zip(
            menu_df["Item"],
            menu_df["Price"].astype(int)
        )
    )


menu = load_menu()


if os.path.exists(DATA_FILE):

    df = pd.read_csv(
        DATA_FILE
    )

    df.columns = df.columns.str.strip()

    df = df.drop_duplicates()

    if "Total" in df.columns:

        df["Total"] = pd.to_numeric(
            df["Total"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["Total"]
        )

else:

    df = pd.DataFrame(
        columns=[
            "No.",
            "Name",
            "Order",
            "Total"
        ]
    )


def save_menu():

    menu_df = pd.DataFrame(
        list(menu.items()),
        columns=["Item", "Price"]
    )

    menu_df.to_csv(
        MENU_FILE,
        index=False
    )


def get_items(order):

    items = []

    for part in str(order).split(","):

        item = part.strip()

        if " x" in item:

            item = item.rsplit(
                " x",
                1
            )[0]

        items.append(
            item
        )

    return items


def clear_content():

    for widget in content_frame.winfo_children():

        widget.destroy()


def create_title(
    parent,
    title,
    subtitle=""
):

    tk.Label(
        parent,
        text=title,
        font=("Arial", 28, "bold"),
        bg="#17120f",
        fg="white"
    ).pack(
        pady=(20, 5)
    )

    if subtitle:

        tk.Label(
            parent,
            text=subtitle,
            font=("Arial", 12),
            bg="#17120f",
            fg="#cccccc"
        ).pack(
            pady=(0, 15)
        )


def show_home():

    clear_content()

    frame = tk.Frame(
        content_frame,
        bg="#17120f"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    tk.Label(
        frame,
        text="INDIAN STREET FOOD",
        font=("Arial", 16),
        bg="#17120f",
        fg="#e8b43c"
    ).place(
        relx=0.08,
        rely=0.38
    )

    tk.Label(
        frame,
        text="KRISH CHAAT CORNER",
        font=("Arial", 40, "bold"),
        bg="#17120f",
        fg="white"
    ).place(
        relx=0.08,
        rely=0.44
    )

    tk.Label(
        frame,
        text="Fresh. Spicy. Delicious.",
        font=("Arial", 19),
        bg="#17120f",
        fg="white"
    ).place(
        relx=0.08,
        rely=0.54
    )

    tk.Button(
        frame,
        text="VIEW MENU",
        font=("Arial", 11, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        padx=25,
        pady=10,
        command=show_menu
    ).place(
        relx=0.08,
        rely=0.63
    )

    tk.Button(
        frame,
        text="ORDER NOW",
        font=("Arial", 11, "bold"),
        bg="#30251f",
        fg="white",
        relief="flat",
        padx=25,
        pady=10,
        command=show_order
    ).place(
        relx=0.19,
        rely=0.63
    )


def show_menu():

    clear_content()

    frame = tk.Frame(
        content_frame,
        bg="#17120f"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    create_title(
        frame,
        "OUR MENU",
        "Fresh and tasty Indian street food"
    )

    cards = tk.Frame(
        frame,
        bg="#17120f"
    )

    cards.pack()

    for i, (item, price) in enumerate(menu.items()):

        card = tk.Frame(
            cards,
            bg="#241c17",
            width=250,
            height=125
        )

        card.grid(
            row=i // 3,
            column=i % 3,
            padx=10,
            pady=8
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=item,
            font=("Arial", 14, "bold"),
            bg="#241c17",
            fg="white"
        ).pack(
            pady=(15, 5)
        )

        tk.Label(
            card,
            text="Indian Street Food",
            font=("Arial", 9),
            bg="#241c17",
            fg="#cccccc"
        ).pack()

        tk.Label(
            card,
            text=f"₹{price}",
            font=("Arial", 14, "bold"),
            bg="#241c17",
            fg="#e8b43c"
        ).pack(
            pady=8
        )


def show_order():

    global cart

    clear_content()

    frame = tk.Frame(
        content_frame,
        bg="#17120f"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    create_title(
        frame,
        "PLACE YOUR ORDER",
        "Add multiple items to your order"
    )

    main = tk.Frame(
        frame,
        bg="#241c17",
        padx=25,
        pady=15
    )

    main.pack()

    tk.Label(
        main,
        text="Customer Name",
        font=("Arial", 12, "bold"),
        bg="#241c17",
        fg="white"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=8
    )

    name_entry = tk.Entry(
        main,
        font=("Arial", 12),
        width=25
    )

    name_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=8
    )

    tk.Label(
        main,
        text="Select Item",
        font=("Arial", 12, "bold"),
        bg="#241c17",
        fg="white"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=8
    )

    item_var = tk.StringVar()

    item_combo = ttk.Combobox(
        main,
        textvariable=item_var,
        values=list(menu.keys()),
        state="readonly",
        width=23
    )

    item_combo.grid(
        row=1,
        column=1,
        padx=10,
        pady=8
    )

    if menu:

        item_combo.current(0)

    tk.Label(
        main,
        text="Quantity",
        font=("Arial", 12, "bold"),
        bg="#241c17",
        fg="white"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=8
    )

    quantity_var = tk.IntVar(
        value=1
    )

    quantity_box = tk.Spinbox(
        main,
        from_=1,
        to=20,
        textvariable=quantity_var,
        width=23,
        font=("Arial", 12)
    )

    quantity_box.grid(
        row=2,
        column=1,
        padx=10,
        pady=8
    )

    cart_list = tk.Listbox(
        main,
        width=55,
        height=7,
        font=("Arial", 11),
        bg="#30251f",
        fg="white",
        selectbackground="#e5b43c",
        selectforeground="black"
    )

    cart_list.grid(
        row=4,
        column=0,
        columnspan=2,
        pady=10
    )

    total_label = tk.Label(
        main,
        text="Total: ₹0",
        font=("Arial", 18, "bold"),
        bg="#241c17",
        fg="#e8b43c"
    )

    total_label.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=8
    )

    def refresh_cart():

        cart_list.delete(
            0,
            tk.END
        )

        total = 0

        for item, quantity, price in cart:

            amount = quantity * price

            total += amount

            cart_list.insert(
                tk.END,
                f"{item} x {quantity} = ₹{amount}"
            )

        total_label.config(
            text=f"Total: ₹{total}"
        )

    def add_item():

        item = item_var.get()

        if item == "":

            messagebox.showwarning(
                "Select Item",
                "Please select an item."
            )

            return

        try:

            quantity = int(
                quantity_var.get()
            )

        except:

            messagebox.showwarning(
                "Quantity",
                "Enter a valid quantity."
            )

            return

        price = menu[item]

        cart.append(
            (
                item,
                quantity,
                price
            )
        )

        refresh_cart()

    def remove_item():

        selected = cart_list.curselection()

        if not selected:

            messagebox.showwarning(
                "Remove Item",
                "Select an item from the cart."
            )

            return

        cart.pop(
            selected[0]
        )

        refresh_cart()

    def place_order():

        global df

        name = name_entry.get().strip()

        if name == "":

            messagebox.showwarning(
                "Customer Name",
                "Please enter customer name."
            )

            return

        if len(cart) == 0:

            messagebox.showwarning(
                "Empty Cart",
                "Please add at least one item."
            )

            return

        order_text = []

        total = 0

        for item, quantity, price in cart:

            order_text.append(
                f"{item} x{quantity}"
            )

            total += (
                quantity * price
            )

        order = ", ".join(
            order_text
        )

        if len(df) == 0:

            order_no = 1

        else:

            numbers = pd.to_numeric(
                df["No."],
                errors="coerce"
            )

            if numbers.dropna().empty:

                order_no = 1

            else:

                order_no = int(
                    numbers.max()
                ) + 1

        new_record = pd.DataFrame(
            [{
                "No.": order_no,
                "Name": name,
                "Order": order,
                "Total": total
            }]
        )

        df = pd.concat(
            [
                df,
                new_record
            ],
            ignore_index=True
        )

        df.to_csv(
            DATA_FILE,
            index=False
        )

        messagebox.showinfo(
            "Order Successful",
            f"Thank you {name}!\n\n"
            f"Order: {order}\n\n"
            f"Total: ₹{total}"
        )

        cart.clear()

        refresh_cart()

        name_entry.delete(
            0,
            tk.END
        )

    button_frame = tk.Frame(
        main,
        bg="#241c17"
    )

    button_frame.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=4
    )

    tk.Button(
        button_frame,
        text="ADD MORE ITEMS",
        font=("Arial", 10, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        padx=15,
        pady=7,
        command=add_item
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        button_frame,
        text="REMOVE ITEM",
        font=("Arial", 10, "bold"),
        bg="#8b3a32",
        fg="white",
        relief="flat",
        padx=15,
        pady=7,
        command=remove_item
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        main,
        text="PLACE ORDER",
        font=("Arial", 11, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        padx=25,
        pady=9,
        command=place_order
    ).grid(
        row=6,
        column=0,
        columnspan=2,
        pady=8
    )


def admin_login():

    login = tk.Toplevel(
        root
    )

    login.title(
        "Admin Login"
    )

    login.geometry(
        "400x250"
    )

    login.configure(
        bg="#17120f"
    )

    tk.Label(
        login,
        text="ADMIN LOGIN",
        font=("Arial", 22, "bold"),
        bg="#17120f",
        fg="white"
    ).pack(
        pady=25
    )

    tk.Label(
        login,
        text="Password",
        font=("Arial", 12),
        bg="#17120f",
        fg="white"
    ).pack()

    password_entry = tk.Entry(
        login,
        show="*",
        font=("Arial", 13),
        width=25
    )

    password_entry.pack(
        pady=10
    )

    def check_password():

        if password_entry.get() == ADMIN_PASSWORD:

            login.destroy()

            show_admin()

        else:

            messagebox.showerror(
                "Login Failed",
                "Incorrect admin password."
            )

    tk.Button(
        login,
        text="LOGIN",
        font=("Arial", 11, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        padx=30,
        pady=8,
        command=check_password
    ).pack(
        pady=10
    )

    password_entry.focus()


def show_admin():

    clear_content()

    frame = tk.Frame(
        content_frame,
        bg="#17120f"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    create_title(
        frame,
        "ADMIN PANEL",
        "CRUD - Menu Management"
    )

    main = tk.Frame(
        frame,
        bg="#241c17",
        padx=30,
        pady=20
    )

    main.pack()

    tk.Label(
        main,
        text="Item Name",
        font=("Arial", 12, "bold"),
        bg="#241c17",
        fg="white"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=8
    )

    item_entry = tk.Entry(
        main,
        font=("Arial", 12),
        width=25
    )

    item_entry.grid(
        row=0,
        column=1,
        padx=10,
        pady=8
    )

    tk.Label(
        main,
        text="Price",
        font=("Arial", 12, "bold"),
        bg="#241c17",
        fg="white"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=8
    )

    price_entry = tk.Entry(
        main,
        font=("Arial", 12),
        width=25
    )

    price_entry.grid(
        row=1,
        column=1,
        padx=10,
        pady=8
    )

    menu_list = tk.Listbox(
        main,
        width=50,
        height=9,
        font=("Arial", 11),
        bg="#30251f",
        fg="white",
        selectbackground="#e5b43c",
        selectforeground="black"
    )

    menu_list.grid(
        row=4,
        column=0,
        columnspan=2,
        pady=12
    )

    def read_items():

        menu_list.delete(
            0,
            tk.END
        )

        for item, price in menu.items():

            menu_list.insert(
                tk.END,
                f"{item}    ₹{price}"
            )

    def clear_fields():

        item_entry.delete(
            0,
            tk.END
        )

        price_entry.delete(
            0,
            tk.END
        )

    def create_item():

        item = item_entry.get().strip()

        price = price_entry.get().strip()

        if item == "" or price == "":

            messagebox.showwarning(
                "Missing Data",
                "Enter item name and price."
            )

            return

        try:

            price = int(price)

        except:

            messagebox.showerror(
                "Invalid Price",
                "Price must be a number."
            )

            return

        if item in menu:

            messagebox.showwarning(
                "Already Exists",
                "This item already exists."
            )

            return

        menu[item] = price

        save_menu()

        read_items()

        clear_fields()

        messagebox.showinfo(
            "CREATE",
            "New item added successfully."
        )

    def update_item():

        item = item_entry.get().strip()

        price = price_entry.get().strip()

        if item not in menu:

            messagebox.showwarning(
                "Not Found",
                "Item does not exist."
            )

            return

        try:

            price = int(price)

        except:

            messagebox.showerror(
                "Invalid Price",
                "Enter a valid price."
            )

            return

        menu[item] = price

        save_menu()

        read_items()

        clear_fields()

        messagebox.showinfo(
            "UPDATE",
            "Item updated successfully."
        )

    def delete_item():

        item = item_entry.get().strip()

        if item not in menu:

            messagebox.showwarning(
                "Not Found",
                "Item does not exist."
            )

            return

        answer = messagebox.askyesno(
            "DELETE",
            f"Are you sure you want to delete {item}?"
        )

        if answer:

            del menu[item]

            save_menu()

            read_items()

            clear_fields()

            messagebox.showinfo(
                "DELETE",
                "Item deleted successfully."
            )

    def select_item(event):

        selected = menu_list.curselection()

        if not selected:
            return

        text = menu_list.get(
            selected[0]
        )

        item = text.rsplit(
            "₹",
            1
        )[0].strip()

        price = text.rsplit(
            "₹",
            1
        )[1].strip()

        item_entry.delete(
            0,
            tk.END
        )

        item_entry.insert(
            0,
            item
        )

        price_entry.delete(
            0,
            tk.END
        )

        price_entry.insert(
            0,
            price
        )

    menu_list.bind(
        "<<ListboxSelect>>",
        select_item
    )

    buttons = tk.Frame(
        main,
        bg="#241c17"
    )

    buttons.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=5
    )

    tk.Button(
        buttons,
        text="CREATE",
        width=13,
        font=("Arial", 10, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        command=create_item
    ).pack(
        side="left",
        padx=4
    )

    tk.Button(
        buttons,
        text="READ",
        width=13,
        font=("Arial", 10, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        command=read_items
    ).pack(
        side="left",
        padx=4
    )

    tk.Button(
        buttons,
        text="UPDATE",
        width=13,
        font=("Arial", 10, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        command=update_item
    ).pack(
        side="left",
        padx=4
    )

    tk.Button(
        buttons,
        text="DELETE",
        width=13,
        font=("Arial", 10, "bold"),
        bg="#8b3a32",
        fg="white",
        relief="flat",
        command=delete_item
    ).pack(
        side="left",
        padx=4
    )

    tk.Button(
        main,
        text="CLEAR",
        width=20,
        font=("Arial", 10, "bold"),
        bg="#555555",
        fg="white",
        relief="flat",
        command=clear_fields
    ).grid(
        row=5,
        column=0,
        columnspan=2,
        pady=7
    )

    read_items()


def show_dashboard():

    clear_content()

    frame = tk.Frame(
        content_frame,
        bg="#17120f"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    create_title(
        frame,
        "DATA SCIENCE DASHBOARD",
        "Krish Chaat Corner"
    )

    if len(df) == 0:

        tk.Label(
            frame,
            text="No order data available.",
            font=("Arial", 18),
            bg="#17120f",
            fg="white"
        ).pack(
            pady=50
        )

        return

    stats = tk.Frame(
        frame,
        bg="#17120f"
    )

    stats.pack(
        pady=8
    )

    values = [
        (
            "TOTAL ORDERS",
            len(df)
        ),
        (
            "CUSTOMERS",
            df["Name"].nunique()
        ),
        (
            "REVENUE",
            f"₹{np.sum(df['Total']):,.0f}"
        ),
        (
            "AVERAGE",
            f"₹{np.mean(df['Total']):.0f}"
        ),
        (
            "MAX ORDER",
            f"₹{np.max(df['Total']):.0f}"
        )
    ]

    for i, (title, value) in enumerate(values):

        card = tk.Frame(
            stats,
            bg="#241c17",
            padx=20,
            pady=10
        )

        card.grid(
            row=0,
            column=i,
            padx=5
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 9, "bold"),
            bg="#241c17",
            fg="#aaaaaa"
        ).pack()

        tk.Label(
            card,
            text=str(value),
            font=("Arial", 16, "bold"),
            bg="#241c17",
            fg="#e8b43c"
        ).pack(
            pady=3
        )

    charts = tk.Frame(
        frame,
        bg="#17120f"
    )

    charts.pack(
        pady=10
    )

    chart_buttons = [
        (
            "ITEM ORDERS",
            item_chart
        ),
        (
            "PIE CHART",
            pie_chart
        ),
        (
            "HISTOGRAM",
            histogram
        ),
        (
            "BOX PLOT",
            box_plot
        ),
        (
            "REVENUE",
            line_chart
        )
    ]

    for i, (text, command) in enumerate(chart_buttons):

        tk.Button(
            charts,
            text=text,
            width=15,
            height=2,
            font=("Arial", 9, "bold"),
            bg="#e5b43c",
            fg="black",
            relief="flat",
            command=command
        ).grid(
            row=0,
            column=i,
            padx=4
        )

    history_frame = tk.Frame(
        frame,
        bg="#241c17",
        padx=15,
        pady=8
    )

    history_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=8
    )

    tk.Label(
        history_frame,
        text="LAST ORDER HISTORY",
        font=("Arial", 17, "bold"),
        bg="#241c17",
        fg="#e8b43c"
    ).pack(
        pady=(0, 7)
    )

    table_frame = tk.Frame(
        history_frame,
        bg="#241c17"
    )

    table_frame.pack(
        fill="both",
        expand=True
    )

    columns = (
        "No.",
        "Name",
        "Order",
        "Total"
    )

    order_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=7
    )

    order_table.heading(
        "No.",
        text="No."
    )

    order_table.heading(
        "Name",
        text="Customer Name"
    )

    order_table.heading(
        "Order",
        text="Order"
    )

    order_table.heading(
        "Total",
        text="Total"
    )

    order_table.column(
        "No.",
        width=60,
        anchor="center"
    )

    order_table.column(
        "Name",
        width=150
    )

    order_table.column(
        "Order",
        width=500
    )

    order_table.column(
        "Total",
        width=100,
        anchor="center"
    )

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=order_table.yview
    )

    order_table.configure(
        yscrollcommand=scrollbar.set
    )

    order_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    def load_history():

        order_table.delete(
            *order_table.get_children()
        )

        if not os.path.exists(DATA_FILE):

            return

        try:

            order_data = pd.read_csv(
                DATA_FILE
            )

            order_data["Total"] = pd.to_numeric(
                order_data["Total"],
                errors="coerce"
            )

            order_data = order_data.tail(
                10
            )

            for _, row in order_data.iterrows():

                order_table.insert(
                    "",
                    "end",
                    values=(
                        row["No."],
                        row["Name"],
                        row["Order"],
                        f"₹{row['Total']:.0f}"
                    )
                )

        except Exception as e:

            messagebox.showerror(
                "History Error",
                str(e)
            )

    tk.Button(
        history_frame,
        text="REFRESH ORDER HISTORY",
        font=("Arial", 9, "bold"),
        bg="#e5b43c",
        fg="black",
        relief="flat",
        padx=20,
        pady=6,
        command=load_history
    ).pack(
        pady=6
    )

    load_history()


def item_chart():

    if len(df) == 0:
        return

    item_data = []

    for _, row in df.iterrows():

        item_data.extend(
            get_items(
                row["Order"]
            )
        )

    counts = pd.Series(
        item_data
    ).value_counts()

    plt.figure(
        figsize=(10, 6)
    )

    counts.plot(
        kind="bar"
    )

    plt.title(
        "Item-wise Orders"
    )

    plt.xlabel(
        "Food Item"
    )

    plt.ylabel(
        "Number of Orders"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.show()


def pie_chart():

    if len(df) == 0:
        return

    item_data = []

    for _, row in df.iterrows():

        item_data.extend(
            get_items(
                row["Order"]
            )
        )

    counts = pd.Series(
        item_data
    ).value_counts()

    plt.figure(
        figsize=(8, 8)
    )

    plt.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%"
    )

    plt.title(
        "Orders by Food Item"
    )

    plt.show()


def histogram():

    if len(df) == 0:
        return

    plt.figure(
        figsize=(9, 6)
    )

    plt.hist(
        df["Total"],
        bins=10
    )

    plt.title(
        "Order Total Distribution"
    )

    plt.xlabel(
        "Order Total"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.show()


def box_plot():

    if len(df) == 0:
        return

    plt.figure(
        figsize=(9, 5)
    )

    sns.boxplot(
        x=df["Total"]
    )

    plt.title(
        "Order Total Box Plot"
    )

    plt.show()


def line_chart():

    if len(df) == 0:
        return

    sales = df.groupby(
        "No."
    )["Total"].sum()

    plt.figure(
        figsize=(10, 6)
    )

    plt.plot(
        sales.index,
        sales.values,
        marker="o",
        markersize=3
    )

    plt.title(
        "Order-wise Revenue"
    )

    plt.xlabel(
        "Order Number"
    )

    plt.ylabel(
        "Revenue"
    )

    plt.grid(
        True
    )

    plt.tight_layout()

    plt.show()


def show_about():

    clear_content()

    frame = tk.Frame(
        content_frame,
        bg="#17120f"
    )

    frame.pack(
        fill="both",
        expand=True
    )

    create_title(
        frame,
        "ABOUT KRISH CHAAT CORNER",
        "Data Science Mini Project"
    )

    text = """
KRISH CHAAT CORNER

Fresh Indian Street Food

Features:

Customer ordering system
Multiple items in one order
Automatic total calculation
Admin CRUD panel
Add new food items
Update item prices
Delete food items
CSV data storage
Data Science dashboard
Order history
Charts and analysis

Prepared by:

Krish Gupta
B.Sc. CS FY
"""

    tk.Label(
        frame,
        text=text,
        font=("Arial", 14),
        bg="#17120f",
        fg="white",
        justify="left"
    ).pack(
        pady=25
    )


def exit_program():

    root.destroy()


root = tk.Tk()

root.title(
    "Krish Chaat Corner"
)

root.geometry(
    "1400x800"
)

root.minsize(
    1100,
    650
)

root.configure(
    bg="#17120f"
)


content_frame = tk.Frame(
    root,
    bg="#17120f"
)

content_frame.pack(
    fill="both",
    expand=True
)


navbar = tk.Frame(
    root,
    bg="#111111"
)

navbar.place(
    relx=0.04,
    rely=0.025,
    relwidth=0.92,
    height=65
)


logo = tk.Label(
    navbar,
    text="KRISH\nCHAAT CORNER",
    font=("Arial", 14, "bold"),
    bg="#111111",
    fg="#e8b43c",
    justify="left"
)

logo.pack(
    side="left",
    padx=20
)


nav_buttons = [
    (
        "HOME",
        show_home
    ),
    (
        "MENU",
        show_menu
    ),
    (
        "ORDER",
        show_order
    ),
    (
        "DASHBOARD",
        show_dashboard
    ),
    (
        "ADMIN",
        admin_login
    ),
    (
        "ABOUT",
        show_about
    )
]


for text, command in nav_buttons:

    tk.Button(
        navbar,
        text=text,
        font=("Arial", 10, "bold"),
        bg="#111111",
        fg="white",
        activebackground="#30251f",
        activeforeground="#e8b43c",
        relief="flat",
        borderwidth=0,
        padx=12,
        command=command
    ).pack(
        side="left",
        padx=2
    )


tk.Button(
    navbar,
    text="EXIT",
    font=("Arial", 10, "bold"),
    bg="#e5b43c",
    fg="black",
    activebackground="#f2c85a",
    relief="flat",
    padx=18,
    command=exit_program
).pack(
    side="right",
    padx=20
)


show_home()

root.mainloop()
