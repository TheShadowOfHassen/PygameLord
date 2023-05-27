import setuptools
import os

# Taken From here: https://stackoverflow.com/questions/27829754/include-entire-directory-in-python-setup-py-data-files

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PygameLord", 
    version="2023.5.27.3",
    author="ShadowOfHassen",
    install_requires=['pygame'],
    description="PygameLibraryOfReusableDohickies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"": ["*.txt", "*.md"],"PygameLord": ["Resources/*.*"]},
    packages=['PygameLord'],
    url='https://github.com/TheShadowOfHassen/PygameLord',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

