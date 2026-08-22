fav_num = {"maria": [13, 23],
           "pete": [89, 56],
           "james": [67, 43],
           "chris": [6, 87],
           "guy": [2, 34],
           }

for person, numbers in fav_num.items():
    print(f"\n{person}'s favourite numbers are:")
    for number in numbers: 
        print(f"\t{number}")

