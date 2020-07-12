import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

dependencies = 'inform'

setup(
    name = 'collection',
    version = '0.4.0',
    description = 'unified interface to collections',
    long_description = readme,
    author = "Ken Kundert",
    author_email = 'collection@nurdletech.com',
    license = 'GPLv3+',
    zip_safe = False,
    py_modules = ['collection'],
    install_requires = dependencies.split(),
    setup_requires = 'pytest-runner>=2.0'.split(),
    tests_require = 'pytest>=4.6 pytest-cov'.split(),
    python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
    keywords = 'collections lists dictionaries'.split(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
)
