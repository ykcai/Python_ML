the_world = {}

# with statement: we don’t have to close the file handler. The with statement creates a context manager and it will automatically close the file handler for you when you are done with it. (Better way)


def read_from_file():
    with open('/Users/michaelcai/Desktop/Personal/Python_ML/code_samples/countries.txt', 'r') as text_file:
        for each_line in text_file:
            each_line = each_line.rstrip('\n')
            country, city = each_line.split('/')
            the_world[country] = city


def write_to_file(country_name, city_name):
    with open('/Users/michaelcai/Desktop/Personal/Python_ML/code_samples/countries.txt', 'a') as text_file:
        text_file.write("\n" + country_name + '/' + city_name)


print("Ask the expert - Capital Cities of the World")
read_from_file()

while True:
    query_country = input(
        "Type the name of the country: ").lower().capitalize()
    if query_country in the_world:
        result = the_world[query_country]
        print(f"The capital city of {query_country} is {result}!")
    else:
        new_city = input(
            f"I do not know what is the capital of {query_country}, please tell me!")
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)
