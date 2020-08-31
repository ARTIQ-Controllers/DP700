Welcome to DP700's documentation!
=================================

General Instructions
--------------------

This software provides ARTIQ support for the RIGOL DP700 series power supplies.

.. note::
    The software is configured for RS232 communication.

Installation
++++++++++++

Install the DP700 package to your environment using pip with git::

    $ python -m pip install git+https://github.com/ARTIQ-Controllers/DP700


DP700 Controller Usage Example
+++++++++++++++++++++++++++++++

First, run the DP700 controller::

    $ aqctl_AGUC8 --bind ::1 -p 3251 -s COM1

.. note::
    Anything compatible with `serial_for_url <https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.serial_for_url>`_
    can be given as a serial port in ``-s`` argument.

    For instance, if you want to specify a host IP address and its port:

    ``-s "socket://<host>:<port>"``.
    for instance:

    ``-d "socket://192.168.1.220:10001"``

Then, send commands via the ``sipyco_rpctool`` utility::

    $ sipyco_rpctool ::1 3251 list-targets
    Target(s):   DP700
    $ sipyco_rpctool ::1 3251 call apply(5.0, 1.0) # will apply 5.0V, 1.0A to channel CH1
    $ sipyco_rpctool ::1 3251 call measure_all() # will return the measured voltage, current, and power on channel CH1
    $ sipyco_rpctool ::1 3251 call channel_on_off('ON') # will turn on channel CH1
    $ sipyco_rpctool ::1 3251 call timer_parameter(1, 5.0, 0.5, 3.0) # will set timing parameters for group 1 to 5.0V, 0.5A, 3.0s
    $ sipyco_rpctool ::1 3251 call close() # close the device

API
---

.. automodule:: DP700.driver
    :members:

.. automodule:: DP700.dpPort
    :members:

ARTIQ Controller
----------------

.. argparse::
    :ref: DP700.aqctl_DP700.get_argparser
    :prog: aqctl_DP700


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
