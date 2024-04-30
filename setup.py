from setuptools import setup, find_packages

setup(
    name="logkontrol",
    version="0.1.0",
    author="voidfemme",
    author_email="rosemkatt@gmail.com",
    description="Custom file logging system for Python applications",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/voidfemme/logkontrol",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
)
