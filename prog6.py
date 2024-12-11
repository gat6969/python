
country_capital = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin"
}


country_capital["Canada"] = "Ottawa"


country_capital["Germany"] = "Munich"


del country_capital["Japan"]


for country in sorted(country_capital):
    print(f"{country}: {country_capital[country]}")


search_country = input("Enter a country to search: ")
if search_country in country_capital:
    print(f"The capital of {search_country} is {country_capital[search_country]}.")
else:
    print(f"{search_country} is not found in the dictionary.")
