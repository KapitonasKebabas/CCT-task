from typing import List


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    # TODO: Replace this with real implementation:

    #List of cities with and without train station || -1 = city with train station and -2 = no train station
    cityList = []
    for i in range(number_of_cities):
        if i in cities_with_train_station:
            cityList.append(-1)
        else:
            cityList.append(-2)

    #Check distance to right
    for i in range(0, len(cityList)):
        if cityList[i] != -1:
            count = 0
            for ii in range(i,len(cityList)):
                if cityList[ii] != -1:
                    count += 1
                else:
                    cityList[i] = count
                    break
    #Check distance to left
    for i in range(0, len(cityList)):
        if cityList[i] != -1:
            count = 0
            for ii in range(i,-1, -1):
                if cityList[ii] != -1:
                    count += 1
                else:
                    if(cityList[i] > count or cityList[i] == -2):
                        cityList[i] = count
                    break
    
    print(cityList)
    maxDistance = max(cityList)
    if maxDistance == -2 or maxDistance == -1:
        maxDistance = 0
    return maxDistance


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    print("ALL TESTS PASSED")