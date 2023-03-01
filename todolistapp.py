import json
import pdb

# task class
class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "\u2713" if self.completed else " "
        print('Task repr method called')
        return f"{self.title} - [{status}]"

# to-do list class
class TodoList:
    def __init__(self):
        self.tasks = []
    
    # adding new task
    def add_task(self, task):
        self.tasks.append(task)

    # removing task
    def remove_task(self, task_index):
        del self.tasks[task_index]

    # editing task
    def edit_task(self, task_index, title, description):
        self.tasks[task_index].title = title
        self.tasks[task_index].description = description

    # status of task
    def complete_task(self, task_index):
        self.tasks[task_index].completed = True

    # saving a task to a file
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([t.__dict__ for t in self.tasks], f)
    
    # loading task(s) from a file
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                print(data)
                # pdb.set_trace()
                self.tasks = [Task(**t) for t in data]
        except Exception as e:
            print(f"file cannot be loaded {filename}:> {e}")

    def __repr__(self):
        return '\n'.join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])

# main method
def main():
    todo_list = TodoList()
    try:
        todo_list.load_from_file('todo.json')
    except:
        pass

    while True:
        print()
        print("Select an option:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Edit task")
        print("4. Complete task")
        print("5. Remove task")
        print("6. Save tasks to file")
        print("7. Load tasks from file")
        print("8. Quit")
        choice = input("> ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == '2':
            print(todo_list)
        elif choice == '3':
            task_index = int(input("Enter task number: ")) - 1
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            todo_list.edit_task(task_index, title, description)
        elif choice == '4':
            task_index = int(input("Enter task number: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '5':
            task_index = int(input("Enter task number: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '6':
            todo_list.save_to_file('todo.json')
        elif choice == '7':
            todo_list.load_from_file('todo.json')
        elif choice == '8':
            break

if __name__ == '__main__':
    main()

