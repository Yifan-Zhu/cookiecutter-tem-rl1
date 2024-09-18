# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation
{% if cookiecutter.environment_manager == 'conda' %}
**Using Conda:**
{% if cookiecutter.dependency_file == 'environment.yml' %}

```bash
conda env create -f environment.yml
conda activate {{ cookiecutter.package_name }}
```
{% elif cookiecutter.dependency_file == 'requirements.txt' %}
```bash
conda create -n {{ cookiecutter.package_name }} python={{ cookiecutter.python_version }}
conda activate {{ cookiecutter.package_name }}
pip install -r requirements.txt
```
{% endif %}
{% endif %}
## Usage
### Training
```bash
python scripts/train.py --config-name config
```
### Evaluation
```bash
python scripts/evaluate.py
```
## License
{% if cookiecutter.open_source_license != 'No license file' %} 
This project is licensed under the terms of the {{ cookiecutter.open_source_license }} license. 
{% else %} 
This project is not licensed. 
{% endif %}
