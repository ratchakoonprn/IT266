airline_tuple = ("Thai Airways", "Air Asia", "Nok Air", "Scoot")
airline_list = list(airline_tuple)
print(airline_list)
airline_list.remove("Scoot")
print(airline_list)
airline_list.append("Bangkok Airways")
print(airline_list)
new_airline_tuple = tuple(airline_list)
print(airline_tuple)
print(new_airline_tuple)
