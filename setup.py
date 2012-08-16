import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'Kotti >= 0.7',
    'kotti_contactform >= 0.1.0',
    'pyramid_zcml',
    'zope.browserresource',
    'psycopg2',
    'pyramid >=1.3',
]

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-xdist',
    'wsgi_intercept',
    'zope.testbrowser',
]

setup(name='kotti_dkbase',
      version='0.1.0b2',
      description='Kotti setup and modifications for CMS projects of Datenkarussell.',
      long_description='\n\n'.join([README, CHANGES]),
      classifiers=[
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: BSD License',
          'Framework :: Pylons',
      ],
      author='Christian Neumann',
      author_email='cneumann@datenkarussell.de',
      url='https://github.com/chrneumann/kotti_dkbase',
      license="BSD3",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'testing': tests_require,
      },
      entry_points="""\
      [paste.app_factory]
      main = kotti_dkbase.maintenance:main

      [fanstatic.libraries]
      kotti_dkbase = kotti_dkbase:lib_dkbase
      """,
)
