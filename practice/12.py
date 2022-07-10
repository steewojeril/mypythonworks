from json import *
with open("countries.json",encoding='utf-8') as f:
    data=load(f)
# print(data)
# capital of china
china_capital=[country["capital"] for country in data if country["name"].lower()=="china"]
print(china_capital)
# print population of china
china_pop=[country["population"] for country in data if country["name"].lower()=="china"][0]
print(china_pop)
# currency of Ukraine
uk_currency=[country["currencies"] for country in data if country["name"].lower()=="ukraine"]
print(uk_currency.pop().pop().get("name"))

# languages of india
ind_lang_details=[country["languages"] for country in data if country["name"].lower()=="india"].pop()
print(ind_lang_details)
ind_lang=[lan["name"] for lan in ind_lang_details]
print(ind_lang)

# country with max population
country_detail=max(data,key=lambda country:country["population"])
print(country_detail["name"])

# print(country_borders)

# english samsaarikkana countries print
eng_lan=[lan for lan in lang if lan["name"].lower()=="english"]
print(eng_lan)
eng_country=[country["name"] for country in data if country["language"] in eng_lan]
print(eng_country)