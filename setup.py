import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_beaker',
    'pyramid_sqla',
    'pyramid_handlers',
    'pyramid_simpleform',
    'pyramid_mako',
    'SQLAlchemy',
    'transaction',
    'repoze.tm2',
    'zope.sqlalchemy',
    'WebError',
    'webhelpers',
    'babel',
    'pygithub',
    'feedparser',
    'docutils',
    ]


entry_points = """\
    [paste.app_factory]
    main = pylonshq:main

    [paste.app_install]
    main = paste.script.appinstall:Installer
"""

setup(name='pylonshq',
      version='1.0',
      description='pylonshq',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pylonshq",
      message_extractors={'pylonshq': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('static/**', 'ignore', None)]},
      entry_points=entry_points,
      paster_plugins=['pyramid'],
      )

