<<<<<<< HEAD
from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery

class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NubbinBattery(last_service_date)

        super().__init__(rorschach_engine, rorschach_battery)

        self.engine = rorschach_engine
        self.battery = rorschach_battery
    
    def needs_service(self):
        return super().needs_service()
=======
from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
>>>>>>> origin
