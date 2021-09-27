from setuptools import setup
import sys


with open('README.rst') as file:
    long_description = file.read()


def get_packages():
    pkgs = ['vici']
    if sys.version_info >= (3, 6):
        pkgs.append('asyncvici')
    return pkgs


setup(
    name="vici",
    version="@EGG_VERSION@",
    description="Native Python interface for strongSwan's VICI protocol",
    long_description=long_description,
    author="strongSwan Project",
    author_email="info@strongswan.org",
    url="https://wiki.strongswan.org/projects/strongswan/wiki/Vici",
    license="MIT",
    packages=get_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
    ]
)
