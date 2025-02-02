#!/usr/bin/env python

import codecs
import os
import re
import sys

from setuptools import find_packages, setup

# When creating the sdist, make sure the django.mo file also exists:
if "sdist" in sys.argv or "develop" in sys.argv:
    os.chdir("wagtailmetadata")
    try:
        from django.core import management

        management.call_command("compilemessages", stdout=sys.stderr, verbosity=1)
    except ImportError:
        if "sdist" in sys.argv:
            raise
    finally:
        os.chdir("..")


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding="utf-8").read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


requires = [
    "django-meta>1.5,<2",
    "wagtail>1.4,<3.0",
]

setup(
    name="wagtail-metadata-mixin",
    version=find_version("wagtailmetadata", "__init__.py"),
    license="MIT License",
    description="OpenGraph, Twitter Card and Google+ snippet tags for Wagtail CMS pages",
    long_description=read("README.rst"),
    author="Basil Shubin",
    author_email="basil.shubin@gmail.com",
    url="https://github.com/bashu/wagtail-metadata-mixin",
    download_url="https://github.com/bashu/wagtail-metadata-mixin/zipball/master",
    packages=find_packages(exclude=("example*", "*.tests*")),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=requires,
)
