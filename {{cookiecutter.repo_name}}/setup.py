# -*- coding: utf-8 -*-
"""
{{cookiecutter.project_name}}
{{cookiecutter.description}}
"""
from setuptools import setup
import versioneer

DOCLINES = __doc__.split("\n")

setup(
    # Self-descriptive entries which should always be present
    name='{{cookiecutter.repo_name}}',
    author='{{cookiecutter.author_name}}',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='{{cookiecutter.open_source_license}}',

    # Which Python importable modules should be included when your package is installed
    packages=['{{cookiecutter.repo_name}}'],

    # Optional include package data to ship with your package
    # Comment out this line to prevent the files from being packaged with your software
    # Extend/modify the list to include/exclude other items as need be
    package_data={'{{cookiecutter.repo_name}}': ["data/*.dat"]
                  },

    entry_points={'console_scripts': ['{{cookiecutter.first_module_name}} = {{cookiecutter.repo_name}}.{{cookiecutter.first_module_name}}:main',
                                      ],
                  },     package_dir={'{{cookiecutter.repo_name}}': '{{cookiecutter.repo_name}}'},

    test_suite='tests',
    # Additional entries you may want simply uncomment the lines you want and fill in the data
    # author_email='me@place.org',      # Author email
    # url='http://www.my_package.com',  # Website
    install_requires=['common-wrangler', 'argparse'],              # Required packages, pulls from pip if needed; do not use for Conda deployment
    # platforms=['Linux',
    #            'Mac OS-X',
    #            'Unix',
    #            'Windows'],            # Valid platforms your code works on, adjust to your flavor
    python_requires=">=3.6",          # Python version restrictions
    tests_require=['pytest']

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    # zip_safe=False,

)
