import os , sys
from pathlib import Path

project_name = "Experiment"

list_of_directories = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/configs/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/utilities/__init__.py",
    "app.py",
    "main.py",
    "setup.py",
    "logs.py",
    "exception.py",
    "schema.yaml",
    f"configs/config.yaml",
    
]

for filepath in list_of_directories:
    filepath = Path(filepath)
    filedir , filename  = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            pass
    else:
        print(f"file is already present  at : {filepath}")