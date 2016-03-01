from setuptools import setup
import pypandoc

long_description = pypandoc.convert('README.md', 'rst')
long_description = long_description.replace('\r', '')

setup(
    name='etao',
    version='0.1.0',

    description='Simple cryptanalysis library',
    long_description=long_description,

    url='https://github.com/jamchamb/etao',

    author='James Chambers',
    author_email='jameschambers2@gmail.com',

    license='GPLv3',

    keywords='cryptography cryptanalysis ciphers',

    packages=['etao'],
    zip_safe=False
)
