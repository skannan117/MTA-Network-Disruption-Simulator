class Station:
    def __init__(self, name, line, operational, platforms):
        self.name = name
        self.line = line
        self.operational = operational
        self.platforms = platforms
        self.disrupted = False
        self.delayed = False

    def get_status(self):
        if self.disrupted:
            return "Disrupted"
        elif self.delayed:
            return "Delayed"
        elif self.operational:
            return "Operational"
        else:
            return "Closed"
        
    def describe(self):
            print(f"- {self.name} | Line: {self.line} | Platforms: {self.platforms} | Status: {self.get_status()}")