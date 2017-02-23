'''
Created on 02 Feb 2017
@author: admin
'''

from setuptools import setup

setup(name="systeminfo",
      version="1.0",
      description="Basic system information for COMP30670",
      url="",
      author="Joseph Doyle",
      author_email="joseph.doyle.1@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
                            )