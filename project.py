class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self):
        super().__init__(50)

    def fare(self):
        total_fare = super().fare()
        return total_fare * 1.10  


bus = Bus()
print("The total fare for the bus ride is INR", bus.fare())
