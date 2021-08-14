######################################################################
# To-Do List Script -- todo.py --
# C:\Users\Alleg\Python\UW Course\Week 6\todo.py
# Assignment 6 - Working with Classes and Functions
# RRoot,1.1.2030,Created starter script
# DJP -- 2021-08-08 -- Initial viewing & toying around with code
# DJP -- 2021-08-09 -- Finalized missing Processor class methods
# DJP -- 2021-08-10 -- Finalized missing IO class methods and tied in to main loop
# DJP -- 2021-08-11 -- Revisions and bug fixes
######################################################################

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """
        Appends the user input to the master list of ToDo records.

        :param task: (string) with name of task:
        :param priority: (string) with the text priority:
        :param list_of_rows (list) master with all ToDo data:
        :return: (list) master with updated ToDo data:
        """
        to_add = {}
        to_add["Task"] = task
        to_add["Priority"] = priority
        list_of_rows.append(to_add)
        print(list_of_rows)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """
        Removes the user-specified task from the master list of ToDo records.

        :param task: (string) with name of task:
        :param list_of_rows (list) master with all ToDo data:
        :return: (list) master with updated ToDo data:
        """
        for count, item in enumerate(list_of_rows):
            if item["Task"] == task:
                list_of_rows.pop(count)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):

        """ Writes data to a file from a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, (string) optional message:
        """
        filehandle = open(file_name, "w")
        for i in list_of_rows:
            to_write = f"{i['Task']}, {i['Priority']}\n"
            filehandle.write(to_write)
        filehandle.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("\n*******************************************")
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Get task name and priority level from user.
        Also

        :return: task, priority
        """
        print("\n****************ADD TASK*******************\n")
        task = input("Please enter the name of the task you wish to add - ").strip().title()
        print("""
        Task Priority:
        1) High
        2) Medium
        3) Low
        4) Overdue
        """)
        priority = int(input("Enter a priority level. [1 to 4] - ").strip())

        if priority == 1:
            priority = "High"
        elif priority == 2:
            priority = "Medium"
        elif priority == 3:
            priority = "Low"
        else:
            priority = "Overdue"

        return (task, priority)

    @staticmethod
    def input_task_to_remove():
        """ Remove user-specified task from master list object.

        :return: task
        """
        print("\n****************REMOVE TASK*****************\n")
        task = input("Please enter the name of the task you wish to remove - ").strip().title()

        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        addition = IO.input_new_task_and_priority()
        Processor.add_data_to_list(addition[0], addition[1], lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        removal = IO.input_task_to_remove()
        Processor.remove_data_from_list(removal, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)  # read file data
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
