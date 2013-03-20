# PuppetPi

A tool for exporting Raspberry Pi-specific data to Puppet facts.

## Installation

PuppetPi is intended to run directly on the Raspberry Pi. It relies on a few git submodules, and one Python module (sh).

    $ sudo apt-get install python-pip git-core
    $ git clone git://github.com/vpetersson/PuppetPi.git
    $ cd PuppetPi
    $ git submodule update --init --recursive
    $ sudo pip install -r requirements.txt

Once installed, all you need to do is to run the Python-script to export the facts:

    $ sudo python puppetpi.py

## Verifying the facts

To confirm that everything worked, you can test them with 'facter'. All values start with 'raspi_', for easy detection.

    $ facter | grep raspi
    raspi_model => B
    raspi_monitor => BNQ-BenQ_GL2450H
    raspi_ram => 512
    raspi_revision => 2.0
    raspi_serial => [removed]
    raspi_vendor => Sony
