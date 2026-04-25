import PyInstaller.__main__
import os
import sys

def build():
    # Define the arguments for PyInstaller
    args = [
        'main.py',
        '--name=Ndownloader',
        '--onefile',
        '--windowed',
        '--clean',
        '--noconfirm',
        '--add-data=ui' + os.pathsep + 'ui',
        '--add-data=engine' + os.pathsep + 'engine',
        '--add-data=utils' + os.pathsep + 'utils',
        '--add-data=bin' + os.pathsep + 'bin',
        '--add-data=assets' + os.pathsep + 'assets',
    ]
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)

if __name__ == "__main__":
    build()
