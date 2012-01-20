import os
from setuptools import setup, find_packages
version = '0.1.0'
README = os.path.join(os.path.dirname(__file__), 'README')
long_description = open(README).read()
setup(name='django-omniture',
      version=version,
      description=("Implements Omniture for use in Django Web Project"),
      long_description=long_description,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      keywords='omniture django',
      author='Llewellyn Hinkes-Jones',
      author_email='lhinkesjones@theatlantic.com',
      url='https://github.com/theatlantic/django-omniture',
      download_url='http://www.github.com/theatlantic/django-omniture/tarball/master',
      license='BSD',
      packages=find_packages(),
      )
