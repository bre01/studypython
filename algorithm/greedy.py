stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_statsion=set()
best_station=None
states_covered=set()
for station,states_for_station in stations.itme():
    covered=states_needed&states_for_station  