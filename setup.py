
#prefer setup tools over disutils

from setuptools import setup

setup(name="systeminfo",
      version="1.0",
      description="Assignment 3",
      url="https://github.com/JosephJamesDoyle87/software.git",
      author="Joseph Doyle",
      author_email="joseph.doyle.1@ucdconnect.ie",
      licence="GPL3",
      packages=['Assignment 3'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
                            )