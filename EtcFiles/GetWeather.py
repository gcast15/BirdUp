
# Python program to find current  
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
  
  
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']
geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
geo_data = geo_request.json()

# Enter your API key here 
api_key = "KEY"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
# city_name = input("Enter city name : ") 
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "lat=" + geo_data['latitude'] + "&lon=" + geo_data['longitude'] + "&appid=" + api_key

# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
    current_temperature = (current_temperature -273.15) * (9/5) +32
  
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
  
    # print following values 
    print(" Temperature (in F) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
  
else: 
    print(" City Not Found ") 

