# 6-1:person
person = {"first_name": "jasmine",
          "last_name": "lee",
          "age": 20,
          "city": "san jose"
          }

print(person)

#6-2: Favorite numbers
fav_nums = {"jasmine": 7,
            "james": 9,
            "eric" : 3,
            "justin" : 5,
            "luke" : 1
            }
print(fav_nums)
print("luke's fav num is ", fav_nums["luke"])

#6-3 :Glossary-pass

#6-4: Glossary2
glossary = { "tuple" : "A tuple is a collection which is ordered and unchangeable.",
             "dictionary" : "Each key is separated from its value by a colon (:), the items are separated by commas.",
             "list" : "List is a collection which is ordered and changeable",
             "loop" : "A for loop is used for iterating over a sequence",
             "key" : "A set is a collection which is unordered and unindexed"
             }
i= 1
for w, d in glossary.items():
    print(i,". ",w.title()," : ",d.title())
    i += 1

#6-5: Rivers

rivers = {"Han" : "Korea",
          "nile" : "egypt",
          "hudson" : "U.S.A"
          }

for r , c in rivers.items():
    print("The ",r.title()," runs through ",c.title(),".")

print("\n")
for r in rivers:
    print(r)

print("\n")
for c in rivers.values():
    print(c)

#6-6 : Polling
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

newppl = { 'jensen', 'ava', 'jennifer','phil','edward'}

for name in newppl :
    if name in favorite_languages:
        print("Hi!",name.title(),"your fav language is ",favorite_languages[name].title())
        print("We appriciate your effort! thanks!\n")
    else:
        print("Nice to meet you, ", name)
        print("What is your fav language? please let us know.\n")

# 6-7 people:

person1 = {"first_name": "jasmine",
           "last_name": "lee",
           "age": 20,
           "city": "san jose"
           }

person2 = {"first_name": "lauren",
           "last_name": "whittingham",
           "age": 19,
           "city": "LA"}

person3 = {"first_name": "tamris",
           "last_name": "alves",
           "age": 18,
           "city": "santa clara"}

people = [person1, person2, person3]

for ppl in people:
    print(ppl)

# 6-8 : Pets pass (same as the previous one)

# 6-9 : Favorite place
favorite_places = {
    "john": ['boston', 'san francisco'],
    "steve": ['park city', 'san jose'],
    "elyse": ['santaclara', 'huston', 'cupertino']
}

for name, places in favorite_places.items():
    print('\n' + name.title() + "'s favorite places are :")
    for place in places:
        print(place)

# 6-10 : Favorite numbers
fav_nums6_10 = {"jasmine": ['7', '3'],
                "james": ['9', '10'],
                "eric": ['3', '5', '8', '9'],
                "justin": ['5', '1', '2'],
                "luke": ['1', '3']
                }

for name, nums in fav_nums6_10.items():
    print('\n' + name + "'s favorite numbers are : ")
    for num in nums:
        print(num)
'''
#6-11: Cities ( version1)
cities = []

city1 = {
    "Seoul" : {
        'country': 'south korea',
        'population' : 500,
        'fact' : 'capital'
    }
}
cities.append(city1)

city2 = {
    "san francisco" : {
        'country': 'U.S.A',
        'population' : 700,
        'fact' : 'harbor'
    }
}
cities.append(city2)

city3 = {
    "taipei" : {
        'country': 'taiwan',
        'population' : 450,
        'fact' : 'island'
    }
}
cities.append(city3)

for city in cities:
    for name, infos in city.items():
        print("\n" + name.title())
        for key, value in infos.items():
            print(key.title(),":",str(value).title())

'''

#6-11: Cities ( version2)
cities = {
    "Seoul" : {
        'country': 'south korea',
        'population' : 500,
        'fact' : 'capital'
    },

    "san francisco" : {
        'country': 'U.S.A',
        'population' : 700,
        'fact' : 'harbor'
    },

    "taipei" : {
        'country': 'taiwan',
        'population' : 450,
        'fact' : 'island'
    }
}
for name, info in cities.items():
    print("\n" + name.title()+":")
    countryOftheCity = info['country']
    populationOftheCity = int(info['population'])
    factOftheCity = info['fact']
    print("The city is in "+countryOftheCity.title())
    print("The population of the city is",populationOftheCity)
    print("The fact of the city: "+factOftheCity.title())
