import random
mocmnl = open("nationsandcapitals.txt","r")
#Declare dictionary
capitals = {}
#Take data from list
countries = mocmnl.readlines()
#Save the list
for things in countries:
#Split the data
    divided = things.split(":")
    country = divided[0]
    capital = divided[1].strip()
    #Add to dictionary
    capitals[country] = capital
#Extract values    
cities = list(capitals.values())
anslabel = ['a','b','c','d']
score = 0
for country in capitals.keys():    
    i = 0
    #Answer header
    print(f"What is the capital of {country}?")
    #Choose correct answer
    correct_ans = capitals[country]
    #Generate wrong answer
    wrong_cities = cities.copy()
    wrong_cities.remove(correct_ans)
    saicmnr_ans = random.sample(wrong_cities, 3)
    #Generate list of 4 multiple choices
    ans_list = saicmnr_ans.copy()
    ans_list.append(correct_ans)
    #Shuffle choices
    random.shuffle(ans_list)
    #Print choices
    dict = {}
    for choice in ans_list:
        dict[anslabel[i]] = choice
        choices = anslabel[i]+"."+choice
        print(choices)
        i +=1
    print("\n")
    index = list(dict.keys())
    city = list(dict.values())
    ans = input("Enter your answer: ")
    print("\n")
    if dict[ans]==correct_ans:
        print("Yeah")
        print("\n")
        score += 1    
    else:
        print("You suck")
        print("\n")
    print(f"Score: {score}")
    print("\n")
#Close the file
mocmnl.close()
