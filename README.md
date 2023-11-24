#  ㅤㅤㅤㅤㅤWeb Task Manager
Description

**This is a small web application that implements the** 
**basic concepts of management and task allocation to**
**ensure structured work in the IT team**
**Installation**


Set up the environment
```
python -m venv venv
```

for Windows:
```
source venv\Scripts\activate
```
for Mac OS
```
source venv/bin/activate
```

Using Python 3.11

Make sure requirements are installed, if not, type in terminal

```
pip install -r requirements.txt
```

To populate the database, use the json file by executing the command:

```python manage.py loaddata data.json```

(If you have problems, you can try migrations)

Next, you may need access to the admin panel to work. For this, you can use a ready-made user:

```
username: admin.user
password: 1qazcde3
```
Or you can create your own using the command:

```python manage.py createsuperuser```

It is a simple conceptual web application that allows the worker to conveniently manage work on tasks

#     Home page

![Screenshot_1.png](images%20for%20readme%2FScreenshot_1.png)

# Login form

![Screenshot_16.png](images%20for%20readme%2FScreenshot_16.png)

# All tasks list
Here, in the left column, you can see the status of the task (ready or not) and in the general task, completed ones are highlighted in green. Tasks in which the deadline has passed are red. On the right, there is a Me suffix next to tasks where I am involved

![Screenshot_2.png](images%20for%20readme%2FScreenshot_2.png)
![Screenshot_3.png](images%20for%20readme%2FScreenshot_3.png)

# Detail worker card

Here is detailed information about the user and the tasks in which he is involved

![Screenshot_6.png](images%20for%20readme%2FScreenshot_6.png)

# Detail task card

You can see more information on the task's detail page, including a list of workers working on it

![Screenshot_4.png](images%20for%20readme%2FScreenshot_4.png)

It is important to note that everyone can create and edit tasks by adding their colleagues there. However, only CTO and Project Manager can add, edit, and delete job item types, and only CTO and HR Manager can add, edit, and delete workers. All others do not have permissions for this

# Example with permissions:

![Screenshot_7.png](images%20for%20readme%2FScreenshot_7.png)

# Example with permissions:

![Screenshot_14.png](images%20for%20readme%2FScreenshot_14.png)

Other screenshots of web app:

![Screenshot_11.png](images%20for%20readme%2FScreenshot_11.png)
![Screenshot_14.png](images%20for%20readme%2FScreenshot_14.png)
![Screenshot_5.png](images%20for%20readme%2FScreenshot_5.png)
![Screenshot_8.png](images%20for%20readme%2FScreenshot_8.png)
![Screenshot_10.png](images%20for%20readme%2FScreenshot_10.png)