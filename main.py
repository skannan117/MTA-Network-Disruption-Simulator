# variables
city = "New York City"

connections = {
    "Times Square": ["Grand Central", "Herald Square"],
    "Grand Central": ["Times Square", "Fulton Street"],
    "Herald Square": ["Times Square", "Union Square"],
    "Union Square": ["Herald Square", "Fulton Street"],
    "Fulton Street": ["Grand Central", "Union Square"]
}



# classes
class Station:
    def __init__(self, name, line, operational, platforms):
        self.name = name
        self.line = line
        self.operational = operational
        self.platforms = platforms

    def get_status(self):
        if self.operational:
            return "Operational"
        else:
            return "Closed"
        
    def describe(self):
            print(f"- {self.name} | Line: {self.line} | Platforms: {self.platforms} | Status: {self.get_status()}")



class Network:
     def __init__(self, city, stations, connections):
          self.city = city
          self.stations = stations
          self.connections = connections
    
     def describe(self):
        print(f"Transit network: {self.city}")
        print(f"Total stations: {len(self.stations)}")
        for n in self.stations: 
            n.describe()
     
     def show_connections(self):
          for n in self.connections:
               print(f"{n} → {", ".join(self.connections[n])}")
 






stations = [
    Station("Times Square", "A", True, 4),
    Station("Grand Central", "B", True, 2),
    Station("Herald Square", "C", False, 2),
    Station("Union Square", "D", True, 4),
    Station("Fulton Street", "E", False, 4)
]


network = Network(city, stations, connections)
network.describe()
network.show_connections()