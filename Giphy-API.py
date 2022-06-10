import requests
import webbrowser

# signup to acquire your own api key
api_key ="LlBJZ6h6eSTsLN2nLcnuJg1W3I3kY1yg"
search = input("search=====>  ")

request = requests.get(f"https://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}")
get_giphy = request.json()
print(request)

with open("base.html") as my_file:
    data = my_file.read()

gif = ""
for i in range(16):
    img_src = get_giphy["data"][i]["images"]["original"]["url"]
    gif += f'<img src = "{img_src}">'

write = data.replace("${images}", gif)
with open("temp.html", "w") as my_file:
    my_file.write(write)


webbrowser.open("temp.html")

