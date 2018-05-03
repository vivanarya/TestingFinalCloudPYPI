import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open('MyPackageNameGithub/version.py').read()) # loads __version__

setup(name='MyPackageNameGithub',
      version=__version__,
      author='$AUTHOR',
    description='',
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="",
    packages= find_packages(exclude='docs'))
