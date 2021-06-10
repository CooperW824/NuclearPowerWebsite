# Nuclear Power Website
 
A simple website for GT Earth Systems to talk about Nuclear Power

### Dependencies
You will need flask for this project
```pip install flask```

I recomend building a Python 3.7+ environment, but we are pretty confident it could work in most Python 3 environments.

I also recomend running this in a virtual environment during development which can be done a variety of ways:

#### Creating a venv:

Navigate to the folder of the repository using 

-       $ cd path/to/repo

Then use command:

-       $ python3 -m venv venv

#### Activating the venv:

-   Linux
    -       $ . venv/bin/activate

- Windows
    -       $ ./venv/scripts/activate

#### Running the Project:

To run the project run the following commands based on OS and terminal:

- Linux

    -       $ export FLASK_APP=server.py 
    -       $ flask run  

- Windows
    
    - Command Prompt:
        
        -       set FLASK_APP=server.py
        
        -       flask run
    
    - Powershell:
        
        -       $env:FLASK_APP="server.py" 
        -       flask run
