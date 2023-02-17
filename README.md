I made a basic todo app here 
The first thing to do is to clone the repository:

    $ git clone https://github.com/shahank-attentive/todoproject.git


Create a virtual environment to install dependencies in and activate it:

     $ pip install virtualenv
     $ virtalenv env_name
     $ source path/bin/activate  like source /home/your_name/Environments/env_name/bin/activate


Then install the dependencies:

    (env)$ pip install -r requirements.txt
  
Once pip has finished downloading the dependencies:

    (env)$ python manage.py runserver
  
And navigate to http://127.0.0.1:8000/todoapp/
