import codecs
import os
from setuptools import setup

setup(
    name="pytest-datadir-ng",
    version="1.0.0",
    description="Fixtures for pytest allowing test functions/methods to easily retrieve test "
                "resources from the local filesystem.",
    # Read the long description from our README.rst file, as UTF-8.
    long_description=codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "README.rst"
            ),
            "rb",
            "utf-8"
        ).read(),
    author="Tilman Blumenbach",
    author_email="tilman+pypi@ax86.net",
    entry_points={
        "pytest11": [
            "pytest_datadir_ng = pytest_datadir_ng"
        ]
    },
    url="https://github.com/Tblue/pytest-datadir-ng",
    download_url="https://github.com/Tblue/pytest-datadir-ng/archive/v1.0.0.tar.gz",
    py_modules=["pytest_datadir_ng"],
    install_requires=["pytest"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",

        # Copied from https://pypi.python.org/pypi/pytest
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2"
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",

        "Topic :: Software Development :: Testing"
    ],
    license="BSD 3-Clause License",
    keywords="py.test resources files data directory directories",
)
