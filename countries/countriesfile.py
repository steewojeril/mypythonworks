from json import *
with open("countries.json",encoding='utf-8') as f:
    data=load(f)
# print population of china
population=[country.get("population") for country in data if country["name"]=="China"]
print(population)
# currency of Ukraine
currency=[country["currencies"] for country in data if country["name"].lower()=="ukraine"]
print(currency.pop().pop().get("name"))

# ctrl+f ==>to find

# languages of india
language_country=[country["languages"] for country in data if country["name"].lower()=="india"].pop()
print(language_country)
language_name=[lan["name"] for lan in language_country]
print(language_name)

max_pop=max(data,key=lambda country:country["population"])
print(max_pop["name"])

# border sharing countries
country_borders=[country["borders"] for country in data if country["name"].lower().startswith("poland")][0]
# print(country_borders)
border_sharing_countries=[country["name"] for country in data if country["alpha3Code"] in country_borders]
print(border_sharing_countries)

# english samsaarikkana countries print
eng_count=[country["name"]for country in data for lan in country["languages"] if lan["name"].lower()=="english"]
print(eng_count)