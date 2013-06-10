from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='reduc.policy',
      version=version,
      description="Configura Sitio de RedUC",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['reduc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'python-ldap',
          'plone.app.ldap',
          'plone.app.registry',
          'Products.RichDocument',
          'Products.Faq',
          'Products.Scrawl',
          'wsapi4plone.core',
          'reduc.theme',
          'reduc.inventario',
          'reduc.usermanager',
          # El viejo usermanager
          #'reduc.usermgr',
      ],
      extras_require={
          'test' : ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
