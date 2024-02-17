import requests, json
apiKey="f970ffed473aa1f4fdbd9acf2e8ed5af"
baseURL="https://api.openweathermap.org/data/2.5/weather?q="
cityName=input ("Enter your City:")

completeURL =baseURL+cityName+"&appid="+apiKey

response=requests.get(completeURL)
data= response.json()
print("current Temperature",data["main"]["temp"])
print("Minimum Temperature",data["main"]["temp_min"])
print("Maximum Temperature",data["main"]["temp_max"])
print("pressure",data["main"]["pressure"])
print("humidity",data["main"]["humidity"])

