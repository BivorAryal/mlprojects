# what is setup.py?  it is resposible for creating ML application as a package. 

# with the help of setup.py, we will be able to build entire ML application as a package and deploy in pipeline

from setuptools import find_packages,setup # 
from typing import List


HYPEN_E_DOT='-e .' # constant
def get_requirements(file_path:str)->List[str]: # input parameter -> return list[in form as str] 
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # removing \n with blanks (forloop)

        if HYPEN_E_DOT in requirements: # if -e. present in req. then removed -e. 
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlprojects',
version='0.0.1',
author='Bivor',
author_email='bivorbivor@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt') # we create function to read "requirement.txt"

)