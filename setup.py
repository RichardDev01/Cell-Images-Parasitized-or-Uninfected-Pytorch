import setuptools

install_requires = [
    'torch',
    'pillow',
    'matplotlib',
]

extras = {
    "dev": [
        'flake8',
        'flake8-blind-except',
        "flake8-builtins",
        "flake8-docstrings",
        "flake8-logging-format",
    ]
}

setuptools.setup(
    name='Pytorch CNN',
    description='Pytorch image recognition on Kaggle dataset',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    extras_require=extras,
    python_requires='>=3.8',
    keyword=['CNN', 'Kaggle', 'Cell Image', 'Pytorch'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
)