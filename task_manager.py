# =====importing libraries===========
from datetime import date  # Importing the datetime library as we need to print the current time

va_spacers = "---" * 50  # Print "---" for 50 times - Used it as a spacer

# ====Login Section====
"""
The usernames and the password are stored in a dict 
called all_users_dictionary. In this dictionary,
The KEYs are the Usernames &
The VALUES are the Passwords.

The Usernames & Passwords are written in users.txt and appended to the
dictionary right after registering
"""
all_users_dictionary = \
    {
        "Username": [],
        "Password": []
    }

with open('user.txt', 'r') as openuser:
    openuser = openuser.readlines()
    for individual_user in openuser:
        individual_user = individual_user.split(",")  # , for users not pass as adds an empty line
        all_users_dictionary["Username"].append(individual_user[0])
    for individual_password in openuser:
        individual_password = individual_password.split()
        all_users_dictionary["Password"].append(individual_password[1])

"""
# LOGIN MENU #
Here, program will take 2 inputs: 
1. Username
2. Password

Then, the program will check if the username exists in the users.txt
respectively in the all_users_dictionary as a KEY. 

If the username exists as a KEY, then it will check if the value of 
the user is the entered password. 
In other words, the program will check if the user and passwords 
are correct.
"""
login_user = input('Username: ')
login_password = input('Password: ')

"""
ADD ADMINS:
This variable is 0 by default
0 = The user is not admin
1 = The user is admin

IMPORTANT!
If changed to 1 - every user will get access to the admin menu
"""
admin_login = 0

"""
The program will ask for user and password
1. If the KEY(user) matches the VALUE(password), then a 'Welcome back' +username 
message will be displayed and the user will get access to the user's menu

2. If the KEY(user) EXISTS BUT doesn't match the VALUE(password), then a message 
'Username or password is incorrect!' will be displayed

3. If the KEY(user) DOESN'T EXIST, then the user will be informed that
the username entered is not a valid username

IMPORTANT!
This menu will LOOP forever until a valid username+password is entered
You can allow other usernames to access the admin menu by changing the line
80. An example after the statement is given there
"""
while True:

    if login_user in all_users_dictionary["Username"]:
        if login_password in all_users_dictionary["Password"]:
            print(f'Welcome back, {login_user}. ')
            if login_user == 'admin':  # or login_admin == 'other-user'
                admin_login = 1
            else:
                admin_login = 0
            break
        else:
            print('Username or password is incorrect! ')
    else:
        print(f'{login_user} is not a valid username')
    login_user = input('Username: ')
    login_password = input('Password: ')

# ====MENU Section====
"""
This is the user's menu where the user can access different sections.
If the user is ADMIN, an additional option will appear.

IMPORTANT!
The user got access for the below options BUT only the admin has 
access to the 'r' and 'ds' menu
"""
while True:
    # presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
    if admin_login == 1:  # IF THE USER IS ADMIN - show the below menu
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all task
vm - view my task
ds - Display statistics
e - Exit
: 
''').lower()

    elif admin_login != 1:  # IF THE USER IS NOT ADMIN - show the below menu
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all task
vm - view my task
e - Exit
: 
''').lower()
    """
    THIS 'ds' MENU WILL ONLY SHOW IF THE USER IS ADMIN
    The admin can see the statistics respectively:
    The number of the tasks & The number of the users
    """
    if login_user == 'admin' and menu == 'ds':
        read_statistics = open('tasks.txt', 'r')
        statistics = read_statistics.readlines()
        read_users_ = open('user.txt', 'r')
        number_of_users = read_users_.readlines()
        print(f"Number of tasks: {len(statistics)}\n"
              f"Number of users:      {len(number_of_users)}")

    # ONLY THE ADMIN HAS ACCESS HERE - REGISTERING NEW USERS
    elif menu == 'r':
        if login_user == 'admin':
            r_username = input('Username: ')
            r_password = input('Password: ')
            r_password_confirmation = input('Confirm your password: ')
            if r_password != r_password_confirmation:
                print('The passwords are not matching.')
            else:
                all_users_dictionary["Password"].append(r_password)
                all_users_dictionary["Username"].append(r_username)

            with open('user.txt', 'a') as register_user:
                register_user.write(f"\n{r_username}, {r_password}")
        else:
            print('Only the admin is allowed to register new users!\n')

    # ADDING NEW TASKS
    elif menu == 'a':
        a_username = input('Person\'s username: ')
        a_title = input('Task title: ')
        a_description = input('Description: ')
        a_due_date = input('The due date: ')
        today_date = date.today()
        task_done = 'No'
        with open('tasks.txt', 'a') as adding_task:
            adding_task.write(
                f"\n{a_username}, {a_title}, {a_description}, {today_date}, {a_due_date}, {task_done}")

    # VIEW ALL THE TASKS
    elif menu == 'va':
        read_task = open('tasks.txt', 'r')
        read = read_task.read().splitlines()
        for x in read:
            x = x.split(", ")
            print(
                f'Task:                {x[1]}\n'
                f'Assigned to:         {x[0]}\n'
                f'Date assigned:       {x[3]}\n'
                f'Due date:            {x[4]}\n'
                f'Task complete?:      {x[5]}\n'
                f'Task Description:    {x[2]}\n'
                f'{va_spacers}'
            )

    # ONLY DISPLAYING THE LOGGED USER'S TASKS
    elif menu == 'vm':
        read_task = open('tasks.txt', 'r')
        read = read_task.read().splitlines()
        vm_username = login_user
        for x in read:
            x = x.split(", ")
            if vm_username == x[0]:
                print(
                    f'Task:                {x[1]}\n'
                    f'Assigned to:         {x[0]}\n'
                    f'Date assigned:       {x[3]}\n'
                    f'Due date:            {x[4]}\n'
                    f'Task complete?:      {x[5]}\n'
                    f'Task Description:    {x[2]}\n'
                    f'{va_spacers}'
                )
                break

            elif vm_username != x[0]:
                for alternative in read:
                    alternative = alternative.split()
                    break
        else:  # IF THE USER HAS NO TASK
            print('There isn\'t a task for you\n')

    # EXIT MENU - PRINTING Good Bye
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()

    else:  # IF THE USER ENTERS A WRONG MENU OPTION
        print("\nYou have made a wrong choice, Please Try again\n")
