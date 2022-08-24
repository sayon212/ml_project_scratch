''' We will use this setup file to install all libraries '''

from setuptools import setup , find_packages
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Sayon"
DESCRIPTION = "This is a test project"
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:     # Returns list of string type
    
    ''' This function will read requirements.txt file 
    and return a list of libraries written inside it '''
    
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME ,
    version=VERSION ,
    author=AUTHOR ,
    description=DESCRIPTION ,
    packages=find_packages() ,                  # install our own created packages by finding __init__.py
    install_requires = get_requirements_list()  # install other external packages
)

# use python setup.py install to install the libraries from setup file