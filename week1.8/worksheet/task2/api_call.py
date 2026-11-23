
import httpx, pandas as pd

base_url = "https://dummyjson.com/"

content = "posts/1"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)


# finding likes for post 5
content = "posts/5"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content['reactions']['likes'])


# finding products that mention apple
content = "products/search?q=apple"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data
print(content)

# converting to pandas data frame
df = pd.DataFrame(content)
print((df))


# finding products that match the word phone
content = "products/search?q=phone"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data
print(content)

# converting to pandas data frame
df = pd.DataFrame(content)
print((df))


# finding recipes which are snacks
content = "recipe/meal-type/snack"
url = base_url + content # API request

response = httpx.get(url)   # API call
print(response.status_code)   # HTTP response

content = response.json()   # JSON data
print(content)

# retrieve difficulties
for recipe in range(len(content['recipes'])):
    print(content['recipes'][recipe]['difficulty'])
