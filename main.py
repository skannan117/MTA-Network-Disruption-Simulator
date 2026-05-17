from station import Station
from network import Network

# variables
city = "New York City"

connections = {
    "Times Square": ["Grand Central", "Herald Square"],
    "Grand Central": ["Times Square", "Fulton Street"],
    "Herald Square": ["Times Square", "Union Square"],
    "Union Square": ["Herald Square", "Fulton Street"],
    "Fulton Street": ["Grand Central", "Union Square"]
}

stations = [
    Station("Times Square", "A", True, 4),
    Station("Grand Central", "B", True, 2),
    Station("Herald Square", "C", False, 2),
    Station("Union Square", "D", True, 4),
    Station("Fulton Street", "E", False, 4)
]


network = Network(city, stations, connections)
# network.describe()
# network.show_connections()

network.trigger_incident("Times Square")
network.describe()
network.incident_report()