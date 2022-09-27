<<<<<<< HEAD
from engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_indicator_on):
        super().__init__(0, 0, warning_indicator_on)
        self.warning_indicator_on = warning_indicator_on

    def engine_needs_service(self):
        return self.warning_indicator_on
=======
from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
>>>>>>> origin
