import requests

def get_population(year):
    if int(year) < 1968 or int(year) > 2023:
        raise ValueError; 'The year must be between 1968 and 2023'    

    fraga = {"query": [{"code": "ContentsCode","selection": {"filter": "item","values": ["BE0101N1"]}},{"code": "Tid","selection": {"filter": "item","values": [year]}}],"response": {"format": "json"}}
    url = 'https://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0101/BE0101A/BefolkningNy'

    response = requests.post(url, json=fraga)
    content = response.json()
    
    x = content['data']
    y = x[0]
    z = y['values']
    q = z[0]
    w = int(q)
    
    return w


if __name__ == '__main__':
    
    year_from = int(input('Enter year from:'))
    year_to = int(input('Enter year to: '))
    pop1 = get_population(year_from)
    pop2 = get_population(year_to)

    print(abs(int(pop1)-int(pop2)))



# This lab contains two tasks that must be solved via a single python program.

# TASK 1 - RETRIEVE DATA VIA AN API

# Swedish National Statistical Bureau (SCB) provides access to a vast volume of statistical data. For example, it is possible to obtain size of the population of Sweden for a given year via URL:

# https://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0101/BE0101A/BefolkningNyLinks

# ...by sending a POST request with following JSON document specifying that the year in question is 2015:

# {"query": [{"code": "ContentsCode","selection": {"filter": "item","values": ["BE0101N1"]}},{"code": "Tid","selection": {"filter": "item","values": ["2015"]}}],"response": {"format": "json"}}

# ...see https://www.scb.se/vara-tjanster/oppna-data/api-for-statistikdatabasen/ for more details

#  To make a POST request use requests.post(url, data). The data parameter of the post method holds parameters that are passed to the API, which in our case is the JSON document describing, among other things, the year for which the population data should be retrieved. Just like with a GET request, the response is a JSON document containing data from the server.

# Write a function called get_population that takes a string describing year, e.g. '1981', and returns an integer containing population of Sweden for that year using the SCB API described above.

# The SCB database behind the API covers the population data only between 1968 and 2023. The function must raise ValueError with message "The year must be between 1968 and 2023" if the argument is outside of this range.

# TASK 2 - MAIN PROGRAM
    
# In the same python file that you created in Task 1 write the main program that prompts the user to enter two years and outputs change in the size of population of Sweden by using the get_population function.

# Use these examples to test your code:

# pytnon3 population_change.py
# Enter year from: 1984
# Enter year to: 1992
# 349392

# pytnon3 population_change.py
# Enter year from: 1968
# Enter year to: 2023
# 2620514
