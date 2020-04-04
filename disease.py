#disease class can be used to create deseases
class disease:
    def __init__(self, name, infectionrate, incubationperiod, damage, cureTime):
        self.name = name
        self.infectionrate = infectionrate
        self.incubationperiod = incubationperiod
        self.damage = damage
        self.showingSymptons = False
        self.timeTillCured = cureTime