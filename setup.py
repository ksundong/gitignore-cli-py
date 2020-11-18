from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

setup(
    name='giigd',
    version='0.0.2',
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
    long_description=readme,
    long_description_content_type='text/markdown',
)
