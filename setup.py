from setuptools import setup
import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='zenpy-release-poc',
    packages=setuptools.find_packages(),
    version='0.1.3',
    description='[NOT A REAL PACKAGE - DO NOT INSTALL] PoC for GitHub Actions + PyPI Trusted Publishing release automation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    license_files=('LICENSE',),
    author='hassaku63',
    author_email='hassaku63@gmail.com',
    url='https://github.com/hassaku63/zenpy-release-poc',
    download_url='https://github.com/hassaku63/zenpy-release-poc/releases/tag/0.1.3',
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'zenpy-release-poc=zenpy_release_poc.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
