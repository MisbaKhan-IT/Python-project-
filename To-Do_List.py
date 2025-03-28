tasks = []  

def show_tasks():
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet!")

while True:
    choice = input("\n[A]dd [R]emove [V]iew [Q]uit: ").lower()

    if choice == 'a':
        tasks.append(input("Enter task: "))
    elif choice == 'r' and tasks:
        show_tasks()
        try:
            tasks.pop(int(input("Task number: ")) - 1)
        except:
            print("Invalid!")
    elif choice == 'v':
        show_tasks()
    elif choice == 'q':
        break
    else:
        print("Invalid choice!")
