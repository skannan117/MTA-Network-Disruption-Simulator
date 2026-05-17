from station import Station

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

    def trigger_incident(self, station_name):
          for n in self.stations:
               if  n.name == station_name:
                    n.disrupted = True
                    for neighbor_name in self.connections[station_name]:
                         for s in self.stations:
                              if s.name == neighbor_name:
                                   s.delayed = True

    def incident_report(self):
        disrupted = []
        delayed = []
        normal = []
        
        for n in self.stations:
               if n.disrupted:
                    disrupted.append(n)     
               elif n.delayed:
                    delayed.append(n)
               else: 
                    normal.append(n)
                    
                    
        print("=== INCIDENT REPORT ===")
        print("Disrupted stations:")
        for i in disrupted: 
            print(f"  - {i.name} (Line: {i.line})")
        print("Delayed stations:")
        for i in delayed:
            print(f"  - {i.name} (Line: {i.line})")
        print("No issues at:")
        for i in normal:
            print(f"  - {i.name} (Line: {i.line})")
        print("=======================")