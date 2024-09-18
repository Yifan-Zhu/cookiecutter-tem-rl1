import os
import shutil

# Get the project directory
project_directory = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    full_path = os.path.join(project_directory, filepath)
    if os.path.exists(full_path):
        os.remove(full_path)

def main():
    if '{{ cookiecutter.open_source_license }}' == 'No license file':
        remove_file('LICENSE')

    if '{{ cookiecutter.use_git }}'.lower() != 'y':
        remove_file('.gitignore')

    dependency_file = '{{ cookiecutter.dependency_file }}'
    if dependency_file == 'requirements.txt':
        remove_file('environment.yml')
    elif dependency_file == 'environment.yml':
        remove_file('requirements.txt')
    else:
        remove_file('requirements.txt')
        remove_file('environment.yml')

if __name__ == '__main__':
    main()
