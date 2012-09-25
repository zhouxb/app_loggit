import os, sys
from setuptools import find_packages
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

data_files = []
app_dir = 'loggit'
for dirpath, dirnames, filenames in os.walk(app_dir):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pass
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
    name = "app_loggit",
    version = "0.1",
    author = "zhou.xingbo",
    author_email = "zhou.xingbo@gmail.com",
    description = "a Django user log app",
    long_description = open("README.md").read(),
    license = "MIT",
    url = "http://github.com/zhouxb/app_loggit",
    packages = find_packages(),
    data_files = data_files,
    install_requires = [
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
