from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '1.0.0'


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
        all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]


setup(
    name='download_pokemon',
    version=__version__,
    description="Python Script to download hundreds of pokemon from 'Google Images'. It is a ready-to-run code! ",
    url='https://github.com/joe-davidson1802/poke-detect',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='pokemon machine-learning ml neural-network image-search image-dataset image-scrapper image-gallery terminal command-line',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Joe Davidson',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='joe.davidson2111@hotmail.com',
    entry_points={
        'console_scripts': [
            'download_pokemon = download_pokemon:main'
        ]},

)