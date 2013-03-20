#!/usr/bin/env python
# -*- coding: utf8 -*-

from pyfacter.pyfacter import fact_writer
import rpiutils.rpi_detect_model
from sh import tvservice


def get_rpidata():
    m = rpiutils.rpi_detect_model.ModelInfo()
    return m.as_json()


def write_rpidata(data):
    for fact in data.keys():
        fact_data = ['raspi_' + fact, data[fact]]
        fact_writer(fact_data[0], fact_data[1])


if __name__ == "__main__":
    rpidata = get_rpidata()

    try:
        monitor = tvservice('-n').split('=')[1]
    except:
        monitor = False

    if monitor:
        rpidata['monitor'] = monitor

    write_rpidata(rpidata)
