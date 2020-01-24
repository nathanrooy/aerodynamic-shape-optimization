
Learn more or give us feedback
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyfoil',
    version='0.0.1',
    author='Nathan A. Rooy',
    author_email='nathanrooy@gmail.com',
    url='https://github.com/nathanrooy/aerodynamic-shape-optimization',
    description='A Python library for 2D airfoil analysis and shape optimization',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['pyfoil'],
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
