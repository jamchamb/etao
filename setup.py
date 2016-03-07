import os
from setuptools import setup

long_description = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='etao',
    version='0.3.0',

    description='Simple cryptanalysis library',
    long_description=long_description,

    url='https://github.com/jamchamb/etao',

    author='James Chambers',
    author_email='jameschambers2@gmail.com',

    license='GPLv3',

    keywords=[
        'cryptography',
        'cryptanalysis',
        'ciphers'
    ],

    test_suite='nose2.collector.collector',

    packages=['etao'],
    install_requires=[
        'nose2>=0.6.2',
        'six>=1.10.0'
    ],
    zip_safe=False
)
