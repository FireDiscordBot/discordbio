# I used a template for this because I haven't a clue what to do
from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import os


# Makes setup work inside of a virtualenv
use_system_lib = True
if os.environ.get("BUILD_LIB") == "1":
    use_system_lib = False


base_dir = os.path.dirname(__file__)

__author__ = "GamingGeek (Jake Ward)"
__email__ = "geek@gaminggeek.dev"

__title__ = "discordbio"
__version__ = "1.2.0"
__summary__ = "An asynchronous wrapper for the discord.bio api"
__uri__ = "https://github.com/GamingGeek/discordbio"

__requirements__ = [
    'aiohttp>=3.6.2',
    'python-dateutil>=2.8.0'
]

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    author=__author__,
    author_email=__email__,
    url=__uri__,
    zip_safe=False,
    install_requires=__requirements__,
    data_files=[
        ('', ['ReleaseNotes.md']),
    ],
    # For data inside packages can use the automatic inclusion
    # include_package_data = True,
    # or the explicit inclusion, eg:
    # package_data = { 'package_name': ['data.file1', 'data.file2' , ...] }
)
