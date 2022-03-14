import newspaper
import nltk
from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.1'
DESCRIPTION = 'A smart Chatbot'

# Setting up
setup(
    name="Good-Bot",
    version=VERSION,
    author="Ruthless-Raven (Isaac Kim)",
    author_email="<ihkim2@uw.edu>",
    description=DESCRIPTION,
    url="https://github.com/Ruthless-Raven/Good-Bot",
    license="MIT",
    packages=find_packages(),
    install_requires=['nltk', 'newspaper'],
    keywords=['python', 'chatbot', 'bot', 'webscrape'],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "OPERATING System :: Unix",
        "OPERATING System :: MacOS :: MacOS X",
        "OPERATING System :: Microsoft :: Windows",
    ],


)
