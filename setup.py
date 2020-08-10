import versioneer
from setuptools import find_packages, setup

PACKAGE_NAME = "FAIR2"
AUTHORS = [
    ("Chris Smith", "c.j.smith1@leeds.ac.uk"),
    ("Nick Leach", "nicholas.leach@stx.ox.ac.uk"),
    ("Stuart Jenkins", "stuart.jenkins@wadham.ox.ac.uk"),
    ("John Broadbent", "johngeoffreybroadbent@gmail.com"),
    ("Tristram Walsh", "tristramwalsh@gmail.com"),
]
URL = "https://github.com/OMS-NetZero/FAIR2"

DESCRIPTION = "Finite-amplitude Impulse Response Model v2.0"
README = "README.md"

SOURCE_DIR = "fair"

REQUIREMENTS = []
REQUIREMENTS_TESTS = ["codecov", "coverage", "pytest-cov", "pytest>=4.0"]

REQUIREMENTS_DEV = [
    *["black", "flake8", "isort<5", "pylint>=2.4.4"],
    *REQUIREMENTS_TESTS,
]

REQUIREMENTS_EXTRAS = {
    "dev": REQUIREMENTS_DEV,
    "tests": REQUIREMENTS_TESTS,
}

# Get the long description from the README file
with open(README, "r") as f:
    README_LINES = ["FaIR 2.0", "==============", ""]
    for line in f:
        README_LINES.append(line.strip())


setup(
    name=PACKAGE_NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=DESCRIPTION,
    long_description="\n".join(README_LINES),
    long_description_content_type="text/x-rst",
    author=", ".join([author[0] for author in AUTHORS]),
    author_email=", ".join([author[1] for author in AUTHORS]),
    url=URL,
    classifiers=[  # full list at https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["fair", "python", "simple", "climate", "model"],
    packages=find_packages(SOURCE_DIR),
    package_dir={"": SOURCE_DIR},
    install_requires=REQUIREMENTS,
    extras_require=REQUIREMENTS_EXTRAS,
)
