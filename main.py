# variables
city = "New York City"
stations = ["Times Square", "Grand Central", "Herald Square", "Union Square", "Fulton Street"]
total_stations = len(stations)

# print statements
print(f"Transit network: {city}")

print(f"Total stations: {total_stations}")

for n in stations:
    print("- " + n)
