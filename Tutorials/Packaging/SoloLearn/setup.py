# The next step in packaging is to write the setup.py file.
# This contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip (name, version, etc.).
# Example of a setup.py file:
from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)
# After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
# To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
# Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution.
# Use python setup.py register, followed by python setup.py sdist upload to upload a package.
# Finally, install a package with python setup.py install.