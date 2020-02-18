import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

dependencies = ''

setup(
    name='collection',
    version='0.2.1',
    description='unified interface to collections',
    long_description=readme,
    author="Ken Kundert",
    author_email='collection@nurdletech.com',
    license='GPLv3+',
    zip_safe=True,
    py_modules=['collection'],
    install_requires=dependencies.split(),
    setup_requires='pytest-runner>=2.0'.split(),
    tests_require='pytest'.split(),
    python_requires='>=3.5',
    keywords='collections lists dictionaries'.split(),
    classifiers=[
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
