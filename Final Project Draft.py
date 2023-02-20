import json, requests

base_url = "https://api.openwaethermap.org/data/2.5/weather"
appid = "11d8807823c229a1482b9686784e208a"


while (True):
    location = input("Please enter a zipcode or city name to begin your query or 'Q' to quit: ")
    if (location.isdigit() and len(location) == 5):
        # Its a zipcode
      zipcode = location
        # kick off weather lookup process using zip
      url = base_url + "appid=" + appid + "&q=" + zipcode
      
      response = requests.get(url)
      unformatted_data = response.json()

      temp = unformatted_data['main']['temp']
      print(f'The Current Temp is: {temp}')
      break
      
    elif (location.isalpha() and len(location) >=4):
        # Its a city name|
      city = location
        # kick off weather lookup process using a city name
      url = base_url + "appid=" + appid + "&q=" + city
      response = requests.get(url)
      unformatted_data = response.json()

      temp = unformatted_data['main']['temp']
      print(f'The Current Temp is: {temp}')
      break

      #Check whether the connection was established
      try:
        response.raise_for_status()
        print('Connection was successful')
      except:
        print('Connection was not succesful')


      
    elif (location.upper() == "Q"):
        # User wants to quit
        print("Enjoy the weather today...")
        break
    else:
        # Not sure what it is... warn the user.
        # make them try again
      print("Invalid Entry, Please enter city or zipcode")
 