
#prefer setup tools over disutils

from setuptools import setup

setup(name="Grid LightSwitching",
      version="1.0",
      description="Assignment 3 - Grid LightSwitching",
      Long description="Assignment 3 - Grid LightSwitching"
      url="https://github.com/JosephJamesDoyle87/software.git",
      author="Joseph Doyle",
      author_email="JosephDoyle.doyle.1@ucdconnect.ie",
      licence="n/a",
      platforms: ['Operating System :: OS Independent'],
      packages=['Assignment 3'],
      
      classifiers = [
          
          'Development Status :: 1 - Production/Unstable',
        'Intended Audience :: assignment',
        'Topic :: Software Engineering ::',
        'License :: Amazon Web Services - Student Package',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
                            )
    