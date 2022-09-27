<<<<<<< HEAD
from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery

class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        glissade_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_battery = SpindlerBattery(last_service_date)

        super().__init__(glissade_engine, glissade_battery)

        self.engine = glissade_engine
        self.battery = glissade_battery
    
    def needs_service(self):
        return super().needs_service()
=======
from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
>>>>>>> origin
