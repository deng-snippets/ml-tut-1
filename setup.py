from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path : str) -> List[str]:
    '''
    return the list of requirements
    '''
    with open(file_path) as f:
        req = f.read().splitlines()

    if '-e .' in req:
        req.remove('-e .')

    return req


setup(
    name = 'ml-tut-1',
    version = '1.0',
    author = 'pd',
    author_email = 'pdmisc@pm.me',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)