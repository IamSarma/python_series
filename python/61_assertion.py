# Usage of assert statement
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# print(ages)
# assert ages[0] <= ages[-1]


# Simulating failure scenario
# ages.reverse()
# print(ages)
# assert ages[0] <= ages[-1]


# Traffic light simulation using assertion
market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green"}


def switchLights(stop_light):
    for key in stop_light.keys():
        if stop_light[key] == "green":
            stop_light[key] = "yellow"
        elif stop_light[key] == "yellow":
            stop_light[key] = "red"
        elif stop_light[key] == "red":
            stop_light[key] = "green"

        assert "red" in stop_light.values(), "Neither light is red!" + str(stop_light)


switchLights(market_2nd)
