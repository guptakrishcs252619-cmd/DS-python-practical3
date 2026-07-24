import os


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
            print("\nQueue Overflow! Queue is Full.")
        else:
            self.queue.append(item)
            print(f"\n'{item}' inserted successfully.")

    def dequeue(self):
        if self.is_empty():
            print("\nQueue Underflow! Queue is Empty.")
        else:
            item = self.queue.pop(0)
            print(f"\nRemoved Item : {item}")

    def peek(self):
        if self.is_empty():
            print("\nQueue is Empty.")
        else:
            print(f"\nFront Item : {self.queue[0]}")

    def traverse(self):
        if self.is_empty():
            print("\nQueue is Empty.")
        else:
            print("\nQueue Traversal")
            print("-" * 50)
            print("Front", end=" ")

            for item in self.queue:
                print(f"[ {item} ]", end=" -> ")

            print("Rear")
            print("-" * 50)

    def display(self):
        if self.is_empty():
            print("\nQueue is Empty.")
        else:
            print("\nCurrent Queue")
            print("-" * 35)
            print("| No. | Item            |")
            print("-" * 35)

            for i, item in enumerate(self.queue, start=1):
                print(f"| {i:<3} | {item:<15}|")

            print("-" * 35)
            print(f"Queue Size : {len(self.queue)}/{self.max_size}")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print("=" * 60)
print("           QUEUE IMPLEMENTATION USING PYTHON")
print("              Developed By : Krish Gupta")
print("=" * 60)

size = int(input("\nEnter Maximum Queue Size : "))
queue = Queue(size)

while True:

    print("\n" + "=" * 60)
    print("                  QUEUE MENU")
    print("=" * 60)
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Traverse Queue")
    print("5. Display Queue")
    print("6. Check Queue Empty")
    print("7. Check Queue Full")
    print("8. Clear Screen")
    print("9. Exit")
    print("=" * 60)

    choice = input("Enter Your Choice : ")

    if choice == "1":
        item = input("Enter Item : ")
        queue.enqueue(item)

    elif choice == "2":
        queue.dequeue()

    elif choice == "3":
        queue.peek()

    elif choice == "4":
        queue.traverse()

    elif choice == "5":
        queue.display()

    elif choice == "6":
        if queue.is_empty():
            print("\nQueue is Empty.")
        else:
            print("\nQueue is Not Empty.")

    elif choice == "7":
        if queue.is_full():
            print("\nQueue is Full.")
        else:
            print("\nQueue is Not Full.")

    elif choice == "8":
        clear()

    elif choice == "9":
        print("\n" + "=" * 60)
        print("Thank You!")
        print("Program Developed By : Krish Gupta")
        print("=" * 60)
        break

    else:
        print("\nInvalid Choice! Please Try Again.")

    input("\nPress Enter to Continue...")
