# variables
city = "New York City"

stations = [
    {"name": "Times Square", "line": "A", "operational": True, "platforms": 4},
    {"name": "Grand Central", "line": "B", "operational": True, "platforms": 2}, 
    {"name": "Herald Square", "line": "C", "operational": False, "platforms": 2}, 
    {"name": "Union Square", "line": "D", "operational": True, "platforms": 4}, 
    {"name": "Fulton Street", "line": "E", "operational": False, "platforms": 4}
]


total_stations = len(stations)


# print statements
print(f"Transit network: {city}")

print(f"Total stations: {total_stations}")

for n in stations:
    if n["operational"]: 
        status = "Operational"
    else: 
        status= "Closed" 
    
    print(f"- {n['name']} | Line: {n['line']} | Platforms: {n['platforms']} | Status: {status}")
          
