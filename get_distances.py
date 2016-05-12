import urllib, json, time
url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
city_string = "Amaravati|Itanagar|Dispur|Patna|Raipur|Panaji|Gandhinagar|Chandigarh|Shimla|Srinagar|Ranchi|Bengaluru|Thiruvananthapuram|Bhopal|Mumbai|Imphal|Shillong|Aizawl|Kohima|Bhubaneswar|Chandigarh|Jaipur|Gangtok|Chennai|Hyderabad|Agartala|Lucknow|Dehradun|Kolkata|Jammu|Chandigarh|Silvassa|Daman|Delhi|Pondicherry"
cities = city_string.split("|")
dist_mat = [[0 for x in range(len(cities))] for y in range(len(cities))] 
for dest, city in enumerate(cities):
	response = urllib.urlopen(url + "origins=" + city_string + "&destinations=" + city)
	data = json.loads(response.read())
	for source, row in enumerate(data["rows"]):
		dist_mat[source][dest] = (row["elements"][0])["distance"]["value"]
	time.sleep(11)	#Limitation of google maps api
print dist_mat
