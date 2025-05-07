def min_base_stations(houses):
    stations = []
    cover = -float('inf')
    for house in houses:
        if house > cover:
            stations.append(house)
            cover = house + 8  # 覆盖 [house-4, house+4]
    return len(stations), stations
#e.g
houses = [1, 5, 12, 33, 34, 35]
num, pos = min_base_stations(houses)
print(f"基站数目为 {num}，基站位置为 {pos}")