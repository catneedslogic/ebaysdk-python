from setuptools import setup, find_packages
import re
import os

PKG = 'ebaysdk'

version = __import__(PKG).get_version()

long_desc = """This SDK is a programatic inteface into the eBay
APIs. It simplifies development and cuts development time by standerizing
calls, response processing, error handling, debugging across the Finding,
Shopping, Merchandising, & Trading APIs. """


setup(
    name=PKG,
    version=version,
    description="eBay SDK for Python",
    author="Tim Keefer",
    author_email="tkeefer@gmail.com",
    url="https://github.com/timotheus/ebaysdk-python",
    license="COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL) Version 1.0",
    packages=find_packages(include=['ebaysdk', 'ebaysdk.*']),
    provides=[PKG],
    install_requires=['lxml', 'requests'],
    test_suite='tests',
    long_description=long_desc,
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
