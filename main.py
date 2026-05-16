# variables
city = "New York City"

stations = [
    {"name": "Times Square", "line": "A", "operational": True, "platforms": 4},
    {"name": "Grand Central", "line": "B", "operational": True, "platforms": 2}, 
    {"name": "Herald Square", "line": "C", "operational": False, "platforms": 2}, 
    {"name": "Union Square", "line": "D", "operational": True, "platforms": 4}, 
    {"name": "Fulton Street", "line": "E", "operational": False, "platforms": 4}
]


# function to determine if operational
def get_status(operational):
    if operational: 
        return "Operational"
    else: 
        return "Closed"

# function to print
def print_network(city, stations): 
    print(f"Transit network: {city}")

    print(f"Total stations: {len(stations)}")
    
    for n in stations:
        print(f"- {n['name']} | Line: {n['line']} | Platforms: {n['platforms']} | Status: {get_status(n['operational'])}")
          

# call function
print_network(city, stations)