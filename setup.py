from setuptools import setup, find_packages
from setuptools import Command
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

setup(name='kotti_dkbase',
      version='0.1.0b1',
      description="Event collection for Kotti sites",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: BSD License",
        ],
      author='Christian Neumann',
      author_email='cneumann@datenkarussell.de',
      license='BSD License',
      packages=['kotti_dkbase'],
      package_data={'kotti_dkbase': [
            'static/*',
            'templates/*.pt',
          ]},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Kotti >= 0.6.0b1',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      cmdclass = {'test': PyTest},
      )
