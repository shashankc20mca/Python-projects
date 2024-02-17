import os
import pickle

class ToDoList:
    def __init__(self, filename='todo_list.pkl'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def display_tasks(self):
        print("\n=== To-Do List ===")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print("==================\n")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")
        self.save_tasks()

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted from the to-do list.")
            self.save_tasks()
        else:
            print("Invalid task index. Please try again.")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            completed_task = self.tasks[index - 1]
            print(f"Task '{completed_task}' marked as completed.")
            self.tasks.pop(index - 1)
            self.save_tasks()
        else:
            print("Invalid task index. Please try again.")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '4':
            index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '5':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
