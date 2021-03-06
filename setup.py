# coding=utf8

from setuptools import setup, find_packages

setup(
    name='awesome-slugify',
    version='1.3',

    author='Dmitry Voronin',
    author_email='dimka665@gmail.com',

    url='https://github.com/dimka665/awesome-slugify',
    description='Python flexible slugify module',

    packages=find_packages(),
    install_requires='Unidecode',

    license='GNU GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='slugify alternative russian slugify flexible awesome',
)



