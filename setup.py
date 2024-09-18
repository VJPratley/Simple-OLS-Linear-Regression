from setuptools import setup, find_packages

setup(
    name='Simple_OLS_regression',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    description='A simple library for OLS linear regression',
    author='Vincenzo Pratley',
    author_email='vincenzopratley@gmail.com',
    url='https://github.com/VJPratley/A-Simple-OLS-Regression',
)
