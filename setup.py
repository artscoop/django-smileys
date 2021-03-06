#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import emojis


setup(
    name='django-emojis',
    version=emojis.version(),
    description="Easily add, use and manage smileys on your Django-powered site.",
    long_description=open('README.rst', 'r').read(),
    keywords='django, image, smiley, emoji',
    author='Artscoop',
    author_email='artscoop93@gmail.com',
    url='http://github.com/artscoop/django-smileys/',
    license='BSD',
    package_dir={'emojis': 'emojis'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Artistic Software',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics'
    ],
    zip_safe=False,
    install_requires=['easy_thumbnails>=1.1', ]
)
