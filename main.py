# variables
city = "New York City"


# lists
# stations = ["Central Park", "Grand Central", "Herald Square", "Union Square", "Fulton Street"]


# for loops
# for station in stations:
#    print(station)

# for i in range (len(stations)):
#    print(stations[i])


# dictionaries
stations = [
    {"name": "Times Square", "line": "A", "operational": True, "platforms": 4},
    {"name": "Grand Central", "line": "B", "operational": True, "platforms": 2}, 
    {"name": "Herald Square", "line": "C", "operational": False, "platforms": 2}, 
    {"name": "Union Square", "line": "D", "operational": True, "platforms": 4}, 
    {"name": "Fulton Street", "line": "E", "operational": False, "platforms": 4}
]

connections = {
    "Times Square": ["Grand Central", "Herald Square"],
    "Grand Central": ["Times Square", "Fulton Street"],
    "Herald Square": ["Times Square", "Union Square"],
    "Union Square": ["Herald Square", "Fulton Street"],
    "Fulton Street": ["Grand Central", "Union Square"]
}


# function to determine if operational
def get_status(operational):
    if operational: 
        return "Operational"
    else: 
        return "Closed"

# function to print
# printf - drop variables directly inside {} without converting or joining
def print_network(city, stations): 
    print(f"Transit network: {city}")

    print(f"Total stations: {len(stations)}")
    
    for n in stations:
        print(f"- {n['name']} | Line: {n['line']} | Platforms: {n['platforms']} | Status: {get_status(n['operational'])}")
          

def print_connections(connections):
    for i in connections:
        print(f"{i} → {", ".join(connections[i])}")




# calling functions
# print_network(city, stations)
print_connections(connections)