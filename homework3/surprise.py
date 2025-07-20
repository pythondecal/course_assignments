# File: surprise.py

# Below is dictionary of star data. Let's perform some data analysis on it.

stars_data = {
    "name": [
        "Dubhe", "Merak", "Phecda", "Megrez", "Alioth", "Mizar", "Alkaid",
        "Betelgeuse", "Rigel", "Bellatrix", "Mintaka", "Alnilam", "Alnitak", "Saiph",
        "Schedar", "Caph", "Tsih", "Ruchbah", "Achird"
    ],
    "bayer": [
        "α UMa", "β UMa", "γ UMa", "δ UMa", "ε UMa", "ζ UMa", "η UMa",
        "α Orionis", "β Orionis", "γ Orionis", "δ Orionis", "ε Orionis", "ζ Orionis", "κ Orionis",
        "α Cas", "β Cas", "γ Cas", "δ Cas", "ε Cas"
    ],
    "constellation": [
        "Ursa Major", "Ursa Major", "Ursa Major", "Ursa Major", "Ursa Major", "Ursa Major", "Ursa Major",
        "Orion", "Orion", "Orion", "Orion", "Orion", "Orion", "Orion",
        "Cassiopeia", "Cassiopeia", "Cassiopeia", "Cassiopeia", "Cassiopeia"
    ],
    "magnitude": [
        1.8, 2.4, 2.4, 3.3, 1.8, 2.1, 1.9,
        0.50, 0.13, 1.64, 2.23, 1.69, 1.77, 2.09,
        2.2, 2.3, 2.5, 2.7, 3.4
    ],
    "distance_ly": [
        124, 79, 84, 81, 81, 78, 104,
        548, 863, 250, 1200, 1344, 1260, 650,
        228, 54.5, 610, 99, 19.4
    ]
}

# Questions:
# 1) Write a function that uses a loop to print the name of each star

# 2) Write a function that counts how many stars in the dataset belong to the "Orion" constellation.

# 3) Write a function that returns the name and magnitude of the brightest star in the dataset.
# Hint: Magnitude is reversed, smaller values indicate brighter stars.

# 4) Write a function that returns a list of star names that are closer than 100 light-years away.

# 5) What is your favorite constellation? 
