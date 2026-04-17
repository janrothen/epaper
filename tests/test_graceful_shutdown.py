import signal
import unittest
from unittest.mock import patch

from btcticker.utils.graceful_shutdown import GracefulShutdown


def _make():
    """Return a GracefulShutdown with signal registration suppressed."""
    with patch("signal.signal"):
        return GracefulShutdown()


class TestGracefulShutdownInit(unittest.TestCase):
    def test_should_stop_is_false_on_init(self):
        gs = _make()
        self.assertFalse(gs.should_stop)

    def test_registers_sigint_handler(self):
        with patch("signal.signal") as mock_signal:
            GracefulShutdown()
        registered = {c.args[0] for c in mock_signal.call_args_list}
        self.assertIn(signal.SIGINT, registered)

    def test_registers_sigterm_handler(self):
        with patch("signal.signal") as mock_signal:
            GracefulShutdown()
        registered = {c.args[0] for c in mock_signal.call_args_list}
        self.assertIn(signal.SIGTERM, registered)


class TestGracefulShutdownExit(unittest.TestCase):
    def test_sets_should_stop_true(self):
        gs = _make()
        gs._exit(signal.SIGTERM, None)
        self.assertTrue(gs.should_stop)

    def test_works_for_sigint(self):
        gs = _make()
        gs._exit(signal.SIGINT, None)
        self.assertTrue(gs.should_stop)

    def test_prints_received_signal_number(self):
        gs = _make()
        with patch("builtins.print") as mock_print:
            gs._exit(15, None)
        printed = mock_print.call_args[0][0]
        self.assertIn("15", printed)


class TestGracefulShutdownReadOnly(unittest.TestCase):
    def test_should_stop_cannot_be_set_externally(self):
        gs = _make()
        with self.assertRaises(AttributeError):
            gs.should_stop = True


if __name__ == "__main__":
    unittest.main()
