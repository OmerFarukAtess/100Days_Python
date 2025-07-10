traverl_log = {
    "france" : ["paris","lille","dijon"]
}

print(traverl_log["france"][0])

nested_list = ["a","b",["c","d"]]

print(nested_list[2][1])


travel_log_2 = {
    "france" : {
        "cities_visited" : ["paris","lille","dijonnnn"],
        "total_visits" : 2
    },
    "germany" : {
        "cities_visited" : ["berlin","hamburg","stuttgart"],
        "total_visits" : 3
    }
}

print(travel_log_2["france"]["cities_visited"][2])

travel_log_2[1] = 1


print(type(travel_log_2[1]))
