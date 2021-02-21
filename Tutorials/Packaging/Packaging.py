# standard format, so that other programmers can install and use them with ease.
# This involves use of the modules setuptools and distutils.
# The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
# This directory goes into another directory containing the readme and license, as well as an important file called setup.py.

# Example directory structure:
# SoloLearn/
#    LICENSE.txt
#    README.txt
#    setup.py
#    sololearn/
#       __init__.py
#       sololearn.py
#       sololearn2.py

# The previous lesson covered packaging modules for use by other Python programmers. However, many computer users who are not programmers do not have Python installed. Therefore, it is useful to package scripts as executable files for the relevant platform, such as the Windows or Mac operating systems. This is not necessary for Linux, as most Linux users do have Python installed, and are able to run scripts as they are.

# For Windows, many tools are available for converting scripts to executables. For example, py2exe, can be used to package a Python script, along with the libraries it requires, into a single executable.
# PyInstaller and cx_Freeze serve the same purpose.