import os
import platform
import shutil
import subprocess

import cookiecutter


def remove(filepath):
    print(filepath, os.path.isfile(filepath), os.path.isdir(filepath))
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        res = shutil.rmtree(filepath)
        print(res)


def create_virtual_environment():
    # Create a virtual environment using the current Python version
    subprocess.run(["python", "-m", "venv", "env"])

    # Upgrade pip version
    subprocess.run(
        ["./env/bin/python3", "-m", "pip", "install", "--upgrade", "pip"])


def install_requirements():
    # Determine the requirements file based on the environment parameter
    requirements_file = f'requirements/local.txt'

    # Execute the pip command to install the requirements
    # TODO: set correct windows venv python path
    if platform.system() == 'Windows':
        subprocess.run(["./env/bin/python3", "-m", "pip", "install", "-r",
                        requirements_file], shell=True)
    else:
        subprocess.run(["./env/bin/python3", "-m", "pip", "install", "-r",
                        requirements_file])


def add_example_api():
    if "{{ cookiecutter.add_example_api }}" == "False":
        remove(os.path.join(os.getcwd(), 'apps', 'example_api'))


# Call the initial setup functions
create_virtual_environment()
install_requirements()
add_example_api()
