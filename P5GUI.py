import tkinter as tk
from tkinter import messagebox, simpledialog


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return "Queue Overflow! Queue is Full."
        self.queue.append(item)
        return f"'{item}' inserted successfully."

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow! Queue is Empty."
        return f"Removed Item : {self.queue.pop(0)}"

    def peek(self):
        if self.is_empty():
            return "Queue is Empty."
        return f"Front Item : {self.queue[0]}"

    def traverse(self):
        if self.is_empty():
            return "Queue is Empty."

        text = "Front "

        for item in self.queue:
            text += f"[ {item} ] -> "

        text += "Rear"
        return text

    def display(self):
        if self.is_empty():
            return "Queue is Empty."

        text = "Current Queue\n\n"

        for i, item in enumerate(self.queue, start=1):
            text += f"{i}. {item}\n"

        text += f"\nQueue Size : {len(self.queue)}/{self.max_size}"

        return text


class QueueGUI:

    def __init__(self, root):

        self.root = root
        self.root.title(" KRISH Queue Implementation")
        self.root.geometry("700x550")
        self.root.configure(bg="#EAF4FC")

        size = simpledialog.askinteger(
            "Queue Size",
            "Enter Maximum Queue Size",
            minvalue=1
        )

        self.q = Queue(size)

        title = tk.Label(
            root,
            text="QUEUE IMPLEMENTATION USING PYTHON",
            font=("Arial", 18, "bold"),
            bg="#EAF4FC",
            fg="navy"
        )

        title.pack(pady=10)

        name = tk.Label(
            root,
            text="Developed By : Krish Gupta",
            font=("Arial", 12, "bold"),
            bg="#EAF4FC",
            fg="green"
        )

        name.pack()

        frame = tk.Frame(root, bg="#EAF4FC")
        frame.pack(pady=15)

        self.entry = tk.Entry(frame, width=25, font=("Arial", 12))
        self.entry.grid(row=0, column=0, padx=10)

        tk.Button(frame, text="Enqueue", width=12, command=self.enqueue).grid(row=0, column=1)

        tk.Button(frame, text="Dequeue", width=12, command=self.dequeue).grid(row=0, column=2)

        tk.Button(frame, text="Peek", width=12, command=self.peek).grid(row=1, column=0, pady=8)

        tk.Button(frame, text="Traverse", width=12, command=self.traverse).grid(row=1, column=1)

        tk.Button(frame, text="Display", width=12, command=self.display).grid(row=1, column=2)

        tk.Button(frame, text="Check Empty", width=12, command=self.empty).grid(row=2, column=0)

        tk.Button(frame, text="Check Full", width=12, command=self.full).grid(row=2, column=1)

        tk.Button(frame, text="Exit", width=12, command=root.destroy).grid(row=2, column=2)

        self.output = tk.Text(
            root,
            width=75,
            height=15,
            font=("Consolas", 11)
        )

        self.output.pack(pady=15)

    def show(self, text):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, text)

    def enqueue(self):
        item = self.entry.get()

        if item == "":
            messagebox.showwarning("Warning", "Enter an Item")
            return

        self.show(self.q.enqueue(item))
        self.entry.delete(0, tk.END)

    def dequeue(self):
        self.show(self.q.dequeue())

    def peek(self):
        self.show(self.q.peek())

    def traverse(self):
        self.show(self.q.traverse())

    def display(self):
        self.show(self.q.display())

    def empty(self):
        if self.q.is_empty():
            self.show("Queue is Empty.")
        else:
            self.show("Queue is Not Empty.")

    def full(self):
        if self.q.is_full():
            self.show("Queue is Full.")
        else:
            self.show("Queue is Not Full.")


root = tk.Tk()
QueueGUI(root)
root.mainloop()
