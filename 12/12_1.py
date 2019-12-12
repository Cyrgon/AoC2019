positions = [
    {"x": -8, "y": -9, "z": -7},
    {"x": -5, "y": 2, "z": -1},
    {"x": 11, "y": 8, "z": -14},
    {"x": 1, "y": -4, "z": -11}
]

velocity = [
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0}
]

for i in range(0, 1000):

    # Gravity
    for j in range(0, len(positions)):
        for k in range(j + 1, len(positions)):
            for key in positions[j].keys():
                if positions[j][key] < positions[k][key]:
                    velocity[j][key] += 1
                    velocity[k][key] -= 1
                elif positions[j][key] > positions[k][key]:
                    velocity[j][key] -= 1
                    velocity[k][key] += 1

    # Velocity
    for j in range(0, len(positions)):
        for key in positions[j].keys():
            positions[j][key] += velocity[j][key]

energy = 0
for j in range(0, len(positions)):
    pot = 0
    kin = 0
    for key in positions[j].keys():
        pot += abs(positions[j][key])
        kin += abs(velocity[j][key])
    energy += pot * kin

print(energy)
