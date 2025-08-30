#To do list

Todo_List = []
while True:   
    print("\n--- ToDo Menu ---")
    print("1- Add a Task")
    print("2- Remove a Task")
    print("3- View list")
    print("5- Do nothing and Laze offf")
    print("6- Mark a Task as Done")
    print("7- Exit")

    choice = int(input("What's on your mind today: "))

    if choice == 1:
        Task = input("Let's add: ")
        Todo_List.append(Task)
        print("Done!!")

    elif choice == 2:
        if len(Todo_List) == 0:
            print("No tasks to remove!")
        else:
            print("Your list:", Todo_List)
            Task = input("Which task to remove? ")
            if Task in Todo_List:
                Todo_List.remove(Task)
                print("Removed!!")
            else:
                print("Task not found!")

    elif choice == 3:
        print("Your ToDo List:", Todo_List)

    elif choice == 5:
        print("Okay... Lazeee. So lazy you didn't even notice the 4 missing")
        break
    elif choice == 6:
        if len(Todo_List) == 0:
            print("No tasks to mark!")
        else:
            print("Your list:")
            for i in range(len(Todo_List)):
                print(str(i+1) + ". " + Todo_List[i])
            num = int(input("Enter the task number that is completed: "))
            if 0 < num <= len(Todo_List):
                Todo_List[num-1] = Todo_List[num-1] + " (Done)"
                print("Marked as Done!")
            else:
                print("Invalid task number!")

    elif choice == 7:
        print("Goodbye! ")
        break   