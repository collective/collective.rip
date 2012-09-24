from setuptools import find_packages
from setuptools import setup
import os

VERSION = '1.3.0'


setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
    ],
    description="Edit CSS and JavaScript in Plone control panel",
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    keywords='css html javascript plone theme',
    license='ZPL',
    long_description=(
        open("README.rst").read() +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    name='collective.rip',
    namespace_packages=[
        'collective'
    ],
    packages=find_packages(),
    url='http://collective.github.com/collective.rip/',
    version=VERSION,
    zip_safe=False,
)
