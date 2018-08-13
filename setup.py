import os

from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

init_raw = open(os.path.join(ROOT, 'src/__init__.py')).read()

setup(
    name='celery-gevent',
    version='0.0.0',
    author='GalCohen',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
)
