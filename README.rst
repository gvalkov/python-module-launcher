Python module launcher
----------------------

This module tries to improve the start-up time of Python scripts. It
does so by doing two things:

 - Eliminating the time it takes to spawn a new Python process.
 - Loading modules ahead of time.

Eliminating interpreter start-up time is done by maintaining a pool of
Python processes. Reducing module load times is done by importing
modules immediately after a worker is spawned. Python is smart about
not re-importing modules that are already in ``sys.modules``.

I ended up writing this module because of a few small Qt programs that
weren't launching as fast as I would like them too. The results were a
~100ms reduction in startup time, which can be attributed to PySide
being a hefty package to import.

There are plenty of bugs and todos left - handling return code and
proper process shutdown seem to be on top of the list.

Usage
=====

::

    Usage: python-module-launcher-3.3 [-hvdpws] socket [mod, ...]

    Options:
      -h, --help           show this help message and exit
      -v, --version        show version and exit
      -d, --daemonize      run in background (default: no)
      -p, --pidfile        pid file to use if running as a daemon
      -w, --workers <num>  worker processes to start (default: 5)
      -s, --spare <num>    spare worker processes to maintain (default: 3)

    Arguments:
      socket               path to AF_UNIX socket
      mod*                 modules to pre-import in workers

    Examples:
      python-module-launcher-3.3 launcher.sock numpy PySide.QtCore

      echo -n "module path.to.module" | nc -U launcher.sock
      echo -n "file path/to/script.py arg1 arg2 | nc -U launcher.sock
      echo -n  "entrypoint name==0.1.0 console_scripts name arg1 arg2"

You can send the following commands to the unix socket::

    file path/to/script.py arg1 arg2 ...
    module path.to.module arg1 arg2 ...
    entrypoint name==0.1.0 console_scripts name arg1 arg2 ...


License
=======

This module is released under the terms of the `Revised BSD License`_.
