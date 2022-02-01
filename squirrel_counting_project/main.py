#!/usr/bin/env python3

# Aleksandr Verevkin
# Counting squirrels by fur project
import pandas

if __name__ == "__main__":
    new_dict = {
        "Fur Color": ["grey", "red", "black"],
        "Count": [0, 0, 0]
    }
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

    furs = data["Primary Fur Color"]

    for fur in furs:
        match fur:
            case "Gray":
                new_dict["Count"][0] += 1
            case "Cinnamon":
                new_dict["Count"][1] += 1
            case "Black":
                new_dict["Count"][2] += 1

    pandas.DataFrame(new_dict).to_csv("squirrel_fur.csv")
