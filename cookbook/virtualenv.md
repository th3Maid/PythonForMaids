## virtualenv:

Create a virtual environment:
    
    python -m venv venv_name

Activate the virtual environment (on Windows):
    
    venv_name\Scripts\activate

(on Unix or MacOS):
    
    source venv_name/bin/activate

Deactivate the virtual environment:
    
    deactivate

Install a package in the virtual environment:
    
    pip install package_name

List installed packages:
    
    pip list

Export the list of installed packages:
    
    pip freeze > requirements.txt

Install packages from requirements.txt:
    
    pip install -r requirements.txt

Remove the virtual environment:
    
    Delete the directory containing the virtual environment.

## poetry:


Create a new Python project:
    
    poetry new project_name

Add a dependency:
    
    poetry add package_name

Install dependencies:
    
    poetry install

Remove a dependency:
    
    poetry remove package_name

Run a script or command in the virtual environment:
    
    poetry run command

Update dependencies:
    
    poetry update

Show information about the project and its dependencies:
    
    poetry show

Export requirements to a requirements.txt file:
    
    poetry export -f requirements.txt --output requirements.txt

Remember, these commands assume you have virtualenv and poetry installed. If not, you can install them using pip:

    pip install virtualenv
    pip install poetry