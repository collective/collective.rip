from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.rip',
      version=version,
      description="Use a text area in the Plone control panel to edit CSS and Javascript.",
      long_description=open("README.txt").read() +
                       open(os.path.join("docs", "HISTORY.txt")).read() +
                       open(os.path.join("docs", "TODO.txt")).read(),
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
