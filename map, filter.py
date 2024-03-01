import math
import statistics

# MAP
def area_of_cirlce(circle_radius):
    return math.pi * (circle_radius ** 2)


radii = [5, 3.5, 10, 7, 0.3]
maped_list = list(map(area_of_cirlce, radii))

# FILTER
data = [3.5, 7.1, 9.0, -3.0, 4.7, 0.4]
average = statistics.mean(data)
filtered_data = list(filter(lambda x: x > average, data))

countries = ["Ukraine", "Spain", "Italy", "", "", "Germany", "", "Montenegro"]
filtered_countries = list(filter(None, countries))

numbers = [1, 2, 3, 4, 5, 6, 7]
filtered_numbers = list(filter(lambda x: x % 2, numbers))
