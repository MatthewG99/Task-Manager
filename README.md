# Capstone-Project-3
## Task Manager

## Project Details:

### Description
The Task Manager Project is a program written in the Python language that was created to fulfill the level 1 task requirements for the Hyperion Development Software Engineering Bootcamp that I am enrolled in.
The program was designed to assist a small business in managing tasks assigned to each member of a team. This includes creating, storing, displaying and editing tasks and related information to and from text files.

### Functionality
* When reading the code, the viewer will first see six functions that have been written to perform certain actions based on options that users will choose from a displayed menu.
These 'functions' are basically blocks of code that take in certain information (e.g. a menu choice) and then output various results based on the actions defined in the function.

* After the six main functions, lists and dictionary variables (as used in the Python language) are set to store user and task information within the program. 
For now, each external text file ('user.txt' and 'tasks.txt') is opened and the existing information is stored in the appropriate lists and dictionaries in the Python program.

* Thereafter, the main program is executed which involves allowing the user to login with their username and password details.
The program checks whether their details are correct by ensuring that their 'username' and 'password' entered match the corresponding information in the appropriate 'usernames' and 'passwords' lists.
If either input (i.e. username or password) is entered incorrectly, appropriate error messages are displayed (e.g. "Your username or password are incorrect.") and the user will repeatedly be prompted to enter their details until
they match the username and password details stored in the related 'usernames' and 'passwords' lists.

* Once the user has entered their details correctly, a successful login message is displayed and a menu with the options to register users, add tasks, view all tasks, view tasks assigned to the user specifically,
generate reports, or exit the program. The 'admin' user gets an extra option in their specific menu wich allows them to 'display statistics'. This option is not available on the menu for other users.
There are certain letters displayed with each menu choice that the user can type in to select an option from the menu (e.g. to register a user, they can type in 'r'). 

* The menu is displayed for users within a 'while' loop and this is done so that after each menu option chosen, the user will return to the main menu, which allows them to make another menu choice if they wish to
or to exit the program. For the first four options in the menu, the associated functions (listed in the beginning of the program) are called (brought in to perform certain actions)
when the user types in the related letter corresponding to that menu choice. For example, if they type in 'r' to register a user, the first function listed 'reg_user()' is executed.
This function prompts the user for input information relating to the new user they want to register, for example they are asked to enter a new username, and then new password. 
Once the new user information is correct (and doesn't already exist; if they try to register an existing user, an error message is displayed) it is stored in the corresponding 'usernames' and 'passwords' lists within the program.
The information is then also written to the appropriate external 'user.txt' text file. A similar process is followed if the user chooses 'a' to add a task from the main menu, except that they are then 
prompted to enter information related to the task with a series of questions (e.g. "Please enter the task description.") and this information is first added to the appropriate 'tasks' dictionary
and then written from the dictionary to the external 'tasks.txt' text file.

* For the third option in the menu, 'va' to view all tasks, the user is not prompted to enter any information but all of the tasks stored in the external 'tasks.txt' file are displayed 
to the user in an easy-to-read, clearly numbered format. If they choose the fourth menu option, 'vm' to view tasks assigned to them, only the tasks assigned to their username are numbered and displayed from the 'tasks.txt' file
and they are also given an extra option to edit one of their tasks displayed by typing in its listed number or type '-1' to return to the main menu. If they choose to edit a task, various prompt questions are displayed to get user input.

* If the user chooses the fifth option from their main menu, 'gr' to generate reports, the sixth function defined above the main program is executed. This function generates two external text files,
namely; the 'task_overview.txt' and the 'user_overview.txt'. So basically, when this program is run on a computer, two new text files will be created in the folder with the 'task manager' Python program and the existing 'user.txt' and 'tasks.txt'
text files. These text files store information relating to statistics of tasks and user information. The user only view a successful message to inform them that their reports have been generated.

* The 'admin' user can then select 'ds' from their menu options to view the reports that have been generated in the previous menu option. If the previous menu option has not been chosen yet,
the text files are firstly created and thereafter the reports with all the related statistics are displayed to the user in a clear, easy-to-read format.

### How can I use it?
* Firstly, you need to clone this repository with the Task Manager program and related text files to a local repository on your computer, so that you can access and run the program.
If you need help, follow the instructions as set out github help webpage: 

  * https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
  
* You will also need to download the Python interpreter program onto your computer's operating system (OS) so that you can view and run the Task Manager code. 
The existing and generated text files can be viewed with a simple Notepad app which comes with Windows OS or you can download an appropriate Notepad app.

  * https://www.python.org/downloads/   - Navigate here to download the appropriate Python interpreter for your OS (i.e. Windows, Mac, Linux)
  
  * https://notepad-plus-plus.org/downloads/   - Navigate here to download Notepad for the text files if you don't already have it.
  
* Once you have the Task Manager files on your computer and you have succesfully downloaded Python and/or Notepad, you need to open the IDLE file within the Python programs on your pc
that was downloaded automatically with Python. This is an Integrated Development Environment which allows you to view and run Python programs. When you open the IDLE file, a Python 'shell'
window will appear. You can then click on the 'file' and 'open' tabs on the top toolbar to navigate to the 'taskmanager.py' python program file to open it. It will be displayed in another window separate to the shell window.

* To run the program, select 'run' from the top toolbar and you can then interact with the task manager program in the shell window. Remember, if you choose to generate reports, 
the text files will be generated in the same folder as the local repository of files for this project and you can view them in Notepad if you wish to.

### Contributors
* This program was worked on individually by myself to fulfill the sofware engineering bootcamp requirements. However, the helpful Hyperion Development mentors also reviewed and 
commented on the program!


