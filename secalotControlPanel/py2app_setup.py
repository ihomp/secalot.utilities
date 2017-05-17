"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['secalotControlPanel.py']
DATA_FILES = []
OPTIONS = {'iconfile': '/Users/admin/Desktop/secalotControlPanel/gui/icon.icns', 'plist': {'LSUIElement':'1'} }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
