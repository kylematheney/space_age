age = int(input("What is your age (in seconds)? "))  # In seconds
earth_orbital_period = 31557600  # In seconds,

print("You are ", round(age / earth_orbital_period, 2), " years old on Earth. Here's how old you are on other planets: ")

orbital_periods = {
    "Mercury: ": 0.2408467,  # Earth years,
    "Venus: ": 0.61519726,  # Earth years,
    "Mars: ": 1.8808158,  # Earth years,
    "Jupiter: ": 11.862615,  # Earth years
    "Saturn: ": 29.447498,  # Earth years
    "Uranus: ": 84.016846,  # Earth years
    "Neptune: ": 164.79132  # Earth years
}

for key, value in orbital_periods.items():
    print(key, round(age/earth_orbital_period, 2) * value, "years old.")
