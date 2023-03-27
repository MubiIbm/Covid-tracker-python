import requests

country_name = input("Enter the Country name : ")

url = "https://disease.sh/v3/covid-19/countries/"+country_name

response = requests.get(url)
data = response.json()

print("Todays Cases => " , data['todayCases'])
print("Todays Deaths => " , data['todayDeaths'])
print("Todays Recovered => " , data['todayRecovered'])
print("Active Cases => " , data['active'])

