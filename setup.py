from setuptools import setup, find_packages


setup(
    name="logkontrol",
    version="0.1.0",
    description="Custom file logging system for Python applications",
    author="voidfemme",
    author_email="rosemkatt@gmail.com",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
    ],
)
