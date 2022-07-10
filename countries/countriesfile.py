from json import *
with open("countries.json",encoding='utf-8') as f:
    data=load(f)

# capital of china
china_capital=[country["capital"] for country in data if country["name"].lower()=="china"]
print(china_capital)

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
# or
languages=[lan["name"] for country in data for lan in country["languages"] if country["name"].lower()=="india"]
print(languages)

# country with max population
max_pop=max(data,key=lambda country:country["population"])
print(max_pop["name"])

# ukraine borders
borders_uk=[country["borders"] for country in data if country["name"].lower().startswith("ukra")].pop() # startswith(ukra)  ukra vach start cheyyunna countries in te kittum
print(borders_uk) # uth cheythal code mathram kittullu (alphacode3)
uk_borders=[country["name"] for country in data if country["alpha3Code"] in borders_uk]
print(uk_borders)

#  print countries whose language is english
eng_countries=[country["name"] for country in data for lan in country["languages"] if lan["name"]=="English"]
print(eng_countries)