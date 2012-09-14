Python module launcher
----------------------

*python-module-launcher* was a failed experiment in improving the
startup performance of python programs. It was concerned with two
things:

 - eliminate interpreter startup times
 - reduce module import times

Eliminating startup times is achieved by maintaining a pool of worker
processes. Reducing module load times is achieved by importing modules
immediately after a worker is spawned (python does not import modules
that are already in ``sys.modules``).

I ended up trying this approach because of a few small Qt dialogs that
weren't launching as fast as I would like them too. The results were
an 100ms reduction in startup time (PySide is a hefty package to
import). At that point I abandoned this project (there are a lot of
unresolved issues such as handling return codes and proper shutdown)


Usage
=====

::

    Usage: python-module-launcher-2.7 [-hvdpws] socket [mod, ...]

    Options:
      -h, --help           show this help message and exit
      -v, --version        show version and exit
      -d, --daemonize      run in background (default: no)
      -p, --pidfile        pid file to use if running as a daemon
      -w, --workers <num>  worker processes to start (default: 5)
      -s, --spare <num>    spare worker processes to maintain (default: 3)

    Arguments:
      socket               location of AF_UNIX socket
      mod*                 modules to pre-import in every worker

    Examples:
      python-module-launcher-2.7 -f launcher.sock numpy PySide.QtCore PySide.QtGui
      echo -n "module path.to.module" | nc -U launcher.sock


You can send the following commands to the unix socket::

    file path/to/script.py arg1 arg2 ...
    module path.to.module arg1 arg2 ...
    entrypoint name==0.1.0 console_scripts name arg1 arg2 ...


License
=======

*python-module-launcher* is released under the terms of the New BSD License.
