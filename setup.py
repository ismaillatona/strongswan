from setuptools import setup, find_packages
import sys


with open('README.rst') as file:
    long_description = file.read()


setup(
    name="avici",
    version="1.0.0",
    description="Native Python interface for strongSwan's VICI protocol",
    long_description=long_description,
    author="strongSwan Project",
    author_email="info@strongswan.org",
    url="https://wiki.strongswan.org/projects/strongswan/wiki/Vici",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[ "vici" ],
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
