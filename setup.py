# This setup.py file is used: if we want to use our project as package like we use seaborn.

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    #This function will return list of all requirements
   requirements = []
   with open(file_path) as file_obj:
       requirements = file_obj.readlines()
       requirements = [req.replace("\n"," ") for req in requirements]

       if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
   return requirements

         
setup(
     name = 'MLproject',
    version = '0.0.1',
    author = 'Pearl',
    author_email = 'pearljotania12@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)