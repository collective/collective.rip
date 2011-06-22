from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='collective.rip',
      version=version,
      description="Edit CSS and JavaScript in Plone control panel",
      long_description=open("README.txt").read() +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Developer tools, Theming',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='http://svn.plone.org/svn/collective/collective.rip',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
