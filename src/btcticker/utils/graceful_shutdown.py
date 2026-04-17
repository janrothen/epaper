#!/usr/bin/env python3

import signal
from types import FrameType


class GracefulShutdown:
    """Cooperative shutdown via SIGINT/SIGTERM handlers.

    Flips an internal flag when signaled. Consumers poll `should_stop` from
    the main loop to exit cleanly:

        shutdown = GracefulShutdown()
        while not shutdown.should_stop:
            do_work()
    """

    def __init__(self) -> None:
        self._should_stop = False
        signal.signal(signal.SIGINT, self._exit)
        signal.signal(signal.SIGTERM, self._exit)

    @property
    def should_stop(self) -> bool:
        return self._should_stop

    def _exit(self, signum: int, frame: FrameType | None) -> None:
        """Mark should_stop on SIGINT/SIGTERM.

        Uses print rather than logging because the logging module is not fully
        reentrant and can deadlock when called from a signal handler.
        """
        print(f"Received signal {signum}, shutting down...")
        self._should_stop = True
