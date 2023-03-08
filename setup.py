import os

from setuptools import find_packages, setup

base_packages = ["textual>=0.13.0","radicli>=0.0.15", "srsly>=2.4.6", "parse>=1.19.0"]

test_packages = [
    "pytest>=5.4.3",
    "black>=19.10b0",
    "flake8>=3.8.3",
    "mktestdocs>=0.1.0",
    "interrogate>=1.2.0",
    "isort==5.12.0",
    "autoflake==2.0.1",
]

docs_packages = [
]

dev_packages = test_packages + docs_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tuilwindcss",
    version="0.1.0",
    author="Vincent D. Warmerdam",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["tuilwindcss", "tuilwindcss.*"]),
    install_requires=base_packages,
    extras_require={"dev": dev_packages},
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)