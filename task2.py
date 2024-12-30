import requests

def fetch_planet_data():
    url = 'https://api.le-systeme-solaire.net/rest/bodies/'
    response = requests.get(url)
    
    if response.status_code == 200:
        planets = response.json()['bodies']
        
        planet_data = []
        for planet in planets:
            if planet.get('isPlanet', False):  # Only consider planets
                name = planet.get('englishName', 'Unknown')
                mass = planet.get('mass', {}).get('massValue', 0)
                orbit_period = planet.get('sideralOrbit', 0)
                planet_data.append({
                    'name': name,
                    'mass': mass,
                    'orbit_period': orbit_period
                })
        
        return planet_data
    else:
        print(f"Unable to fetch data! Status code: {response.status_code}")
        return []  

def find_heaviest_planet(planets):
    if not planets:
        return 'Unknown', 0  

    heaviest_planet = max(planets, key=lambda planet: planet['mass'], default=None)
    if heaviest_planet:
        return heaviest_planet['name'], heaviest_planet['mass']
    return 'Unknown', 0

def find_planet_with_longest_orbit(planets):
    if not planets:
        return 'Unknown', 0 
    
    longest_orbit_planet = max(planets, key=lambda planet: planet['orbit_period'], default=None)
    if longest_orbit_planet:
        return longest_orbit_planet['name'], longest_orbit_planet['orbit_period']
    return 'Unknown', 0

#test heaviest/longest orbit 
planets = fetch_planet_data()

if planets:

    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")

   
    longest_name, longest_orbit = find_planet_with_longest_orbit(planets)
    print(f"The planet with the longest orbit period is {longest_name} with an orbit period of {longest_orbit} days.")
else:
    print("No planet data available.")
