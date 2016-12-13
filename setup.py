#!/usr/bin/env python
"""omf: API Library for Open Mining Format"""

from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Physics',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS',
    'Natural Language :: English',
]

with open('README.rst') as f:
    LONG_DESCRIPTION = ''.join(f.readlines())

setup(
    name='omf',
    version='0.9.0',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'numpy>=1.7',
        'properties>=0.3.0',
        'pypng',
        'six',
        'vectormath',
    ],
    author='ARANZ Geo Ltd.',
    author_email='info@3ptscience.com',
    description='API Library for Open Mining Format',
    long_description=LONG_DESCRIPTION,
    keywords='mining data interchange',
    url='http://www.aranzgeo.com/',
    download_url='http://github.com/3ptscience/omf',
    classifiers=CLASSIFIERS,
    platforms=['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    license='MIT License',
    use_2to3=False,
)