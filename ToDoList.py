def ToDo() :
    tasks = []
    while True :
        print("\n\n__________________________ TO DO LIST __________________________")
        print(" 1. Add Task\n 2. Show Tasks\n 3. Mark as Done\n 4. Quit")

        choice = int(input("Enter your choice : "))

        if choice==1 :
            n_task = int(input("\nEnter the number of tasks : "))

            for i in range(n_task) :
                task = input("\nEnter the task : ")
                tasks.append({"task" : task, "done" : False})
                print("Task Added")

        elif choice==2 :
            print("\nTasks : ")
            for index, task in enumerate(tasks) :
                status = "Done" if task["done"] else "Not Done"
                print(f"{index+1}.   {task["task"]} - {status}")

        elif choice==3 :
            taskindex = int(input("\nEnter the task number that is done : "))
            if taskindex > 0 and taskindex <= len(task) :
                tasks[taskindex-1]["done"] = True
            else :
                print("Task nummber is not valid ")

        elif choice==4 :
            print("\nExiting ... ")
            break
        
        else : 
            print("\nInvalid input !")

ToDo()