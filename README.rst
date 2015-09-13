.. _Recalbox: http://recalbox.com
.. _recalbox-manager: https://github.com/sveetch/recalbox-manager
.. _virtualenv: http://www.virtualenv.org/

Recalbox Manifesto
==================

This is a simple command line script to build rom systems and bios readme files 
from a template and using the `Recalbox`_ manifest file to retrieve datas.

Install
*******

::

    pip install recalbox-manifesto

This package have some dependancies, if you don't want to install them on your system, install it through virtualenv: ::

    mkdir manifesto
    cd manifesto
    virtualenv --no-site-packages --setuptools .
    bin/pip install recalbox-manifesto
    source bin/activate

Usage
*****

The command require a path to XML manifest file, for testing purpose you can get the one currently shipped into `recalbox-manager`_ :

    https://raw.githubusercontent.com/sveetch/recalbox-manager/master/project/MANIFEST.xml

Then you can invoke the builder like that: ::

    recalbox-manifesto -m MANIFEST.xml --roms /home/foo/roms --bios /home/foo/bios

You can see that you have to specify a directory path for bios and roms where the readme files will be created. If you don't give a path for bios or roms, they won't be builded.

These paths have to exists. Note that rom systems files are created into a directory named from their system key, this will so create a structure like that: ::

    ├── atari2600
    │   └── readme.txt
    ├── mame
    │   └── readme.txt
    ├── mastersystem
    │   └── readme.txt
    ├── megadrive
    │   └── readme.txt
    ├── n64
    │   └── readme.txt
    ├── neogeo
    │   └── readme.txt
    ├── nes
    │   └── readme.txt
    ├── pcengine
    │   └── readme.txt
    ├── snes
    │   └── readme.txt
    ├── virtualboy
    │   └── readme.txt
    └── wswan
        └── readme.txt

Use the help command action to see command options details : ::

    recalbox-manifesto --help
