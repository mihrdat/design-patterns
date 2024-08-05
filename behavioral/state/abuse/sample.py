class Stopwatch:
    def __init__(self):
        self._is_running = False

    def click(self):
        if self._is_running:
            self._is_running = False
            print("Stopped")
        else:
            self._is_running = True
            print("Running")


watch = Stopwatch()
watch.click()
watch.click()
watch.click()

"""
from abc import ABC, abstractmethod


class Stopwatch:
    def __init__(self):
        self._current_state = StoppedState(self)

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, state):
        self._current_state = state

    def click(self):
        self._current_state.click()


class State(ABC):
    @abstractmethod
    def click(self): ...


class RunningState(State):
    def __init__(self, stopwatch):
        self._stopwatch = stopwatch

    def click(self):
        self._stopwatch.current_state = StoppedState(self._stopwatch)
        print("Stopped")


class StoppedState(State):
    def __init__(self, stopwatch):
        self._stopwatch = stopwatch

    def click(self):
        self._stopwatch.current_state = RunningState(self._stopwatch)
        print("Running")


watch = Stopwatch()
watch.click()
watch.click()
watch.click()
"""
