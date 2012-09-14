from setuptools import setup, find_packages

setup(
    name = "app_loggit",
    version = "0.1",
    author = "zhou.xingbo",
    author_email = "zhou.xingbo@gmail.com",
    description = "a Django user log app",
    long_description = open("README.rst").read(),
    license = "MIT",
    #url = "http://github.com/pinax/django-user-accounts",
    packages = find_packages(),
    install_requires = [
        #"django-appconf==0.5",
        #"pytz==2012d"
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
