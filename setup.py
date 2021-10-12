


import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

install_requires = [
    "pyramid",
    "SQLAlchemy",
    "GeoAlchemy2",
    "Shapely",
]

setup(
    name="c2c.sqlalchemy.rest",
    version="0.4",
    description="Add a REST interface to simple SQLAlchemy object",
    long_description=README,
    namespace_packages=["c2c"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Framework :: Buildout :: Recipe",
        "Topic :: System :: Installation/Setup",
    ],
    author="Mohamed Amanna",
    author_email="twitter.com/noriodachi",
    url="http://github.com/2ino/c2c.sqlalchemy.rest",
    keywords="sqlalchemy rest",
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
    }
)
