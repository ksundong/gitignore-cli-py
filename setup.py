from setuptools import setup, find_packages

setup(
    name='giigd',
    version='0.0.1',
    author='Dion',
    author_email='idion@idion.dev',
    url='https://github.com/ksundong/gitignore-cli-py',
    install_requires=[
        'click',
        'fuzzywuzzy',
        'python-Levenshtein',
    ],
    keywords=[
        'gitignore'
    ],
    python_requires='>=3',
    description='gitignore cli',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "giig = giig.main:cli"
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
