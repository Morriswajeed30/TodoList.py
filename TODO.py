#Todo list App
#Date started: Aug 27 2025

Todos = []
def write(listing,moad):
    with open("C:\\Users\\user\\OneDrive\\Documents\\Todos.txt",moad)as file:
        for i in listing:
            file.write(i + "\n" )
def read(listings):
    try:
        with open("C:\\Users\\user\\OneDrive\\Documents\\Todos.txt","r") as file:
            print(file.read())
    except Exception:
        print("You ran into an error try again:( ")

while True:
    Menu = ["Read", "Write", "Delete"]
    print("Menu: ")
    for i in Menu:
        print(i)
    operation = input(" choose from the displayed menu: ")
    if operation == "Write":
        while True:
            write = input("input your todos,enter Quit when you are done: ")
            if write == "Quit":
                break
            write(Todos,"a")
            Todos.append(write)
    
    if operation == "Delete":
        delete = int(input("Enter the Number to the one our want to delete: "))
        try:
           with open("C:\\Users\\user\\OneDrive\\Documents\\Todos.txt","r") as file:
                items = [line.strip() for line in file if line.strip()]
        except IndexError:
            print("You can't delete from an empty list")
        removed_item = items.pop(delete)
        print(f"Removed:{removed_item}")
        write(items,"w")
        read(items)
    elif operation == "Delete All":
       open("C:\\Users\\user\\OneDrive\\Documents\\Todos.txt","w").close()
        
        
    elif operation == "Read":
        if not Todos:
            print("You don't have any Todos yet:( ")
        read(Todos)
        

    again = input("Do you want to perform any other action: ").capitalize()
    if again == "Yes":
        continue
    elif again == "No":
        print("Have a nice day, try not to forget your pending task!!!!")
        exit()