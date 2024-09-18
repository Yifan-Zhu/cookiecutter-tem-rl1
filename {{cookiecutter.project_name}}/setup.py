from setuptools import find_packages, setup

install_requires = [
    {%- if cookiecutter.use_gymnasium == 'y' %}
    'gymnasium',
    {%- endif -%}
    {%- if cookiecutter.use_minigrid == 'y' %}
    'minigrid',
    {%- endif -%}
    {%- if cookiecutter.use_pytorch == 'y' %}
    'torch',
    {%- endif -%}
    {%- if cookiecutter.use_pytorch_lightning == 'y' %}
    'pytorch-lightning',
    {%- endif -%}
    {%- if cookiecutter.use_tensorflow == 'y' %}
    'tensorflow',
    {%- endif -%}
    {%- if cookiecutter.use_stable_baselines3 == 'y' %}
    'stable-baselines3',
    {%- endif -%}
    {%- if cookiecutter.use_ray == 'y' %}
    'ray',
    {%- endif -%}
    {%- if cookiecutter.use_wandb == 'y' %}
    'wandb',
    {%- endif %}
    # Utilities
    'notebook',
    'numpy',
    'scikit-learn',
    'matplotlib',
    'seaborn',
    'pandas',
    'tqdm',
    'hydra-core',
]

setup(
    name="{{ cookiecutter.package_name }}",
    version="0.1.0",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author_name }}",
    packages=find_packages(),
    python_requires=">= {{ cookiecutter.python_version }}",
    install_requires=install_requires,
)
