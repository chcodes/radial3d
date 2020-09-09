import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="radial",
    version='0.0.1',
    author="Chris Huynh",
    description="Experimenting with 3D radial MRI image reconstruction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chcodes/radial3d",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
