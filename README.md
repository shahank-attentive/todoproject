I made a basic todo app here 
The first thing to do is to clone the repository:

    $ git clone https://github.com/shahank-attentive/todoproject.git


Create a virtual environment to install dependencies in and activate it:

     $ virtualenv2 -- env
     $ source env/bin/activate


Then install the dependencies:
    (env)$ pip install -r requirements.txt
  
Once pip has finished downloading the dependencies:
    (env)$ python manage.py runserver
  
And navigate to http://127.0.0.1:8000/todoapp/
