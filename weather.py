import csv
from datetime import datetime
import statistics

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    temp=input("What's the temperature in Celsius today?: ")
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    date = datetime.fromisoformat(iso_string)
    return date.strftime
print(convert_date("2021-07-05T07:00:00+08:00"))



"""Converts and ISO formatted date into a human-readable format.

   
    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #1.input ISO date string --> date =  "2021-07-05T07:00:00+08:00"
    #2. convert iso date to date, time object
    #print (type(iso_string))
    #readable_date=datetime.fromisoformat(iso_string)
    #print(type(readable_date))
    #3. convert back to string --> needs to be formatted as "weekday date month, year"
    #formatted_date=readable_date.strftime("%A, %d, %B, %Y")
    #print(formatted_date)
    #return(formatted_date)
    #iso_string = datetime.datetime.now()
    #return(readable_date)

#convert_date("2021-07-05T07:00:00+08:00")
#print(convert_date)

#expected_result = "Monday 05 July 2021"






def convert_f_to_c(temp_in_fahrenheit):
   # temp_in_fahrenheit = 90
    temp_in_c = (temp_in_fahrenheit - 32) * 5/9
    return round (temp_in_c, 1)


print(convert_f_to_c(90))    

"""Converts a temperature from Fahrenheit to Celcius.
    

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
   

def calculate_mean(weather_data):
    weather_data = [float(x) for x in weather_data]  # Convert all items to float
    return round (statistics.mean(weather_data), 1)

print(calculate_mean([49,57,56,55,53]))

"""Calculates the mean value from a list of numbers.
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """



def load_data_from_csv(csv_file):
    # Removed hardcoded assignment to allow dynamic file input
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        result = [row for row in reader if row]  # Read all non-empty rows into a list
    return result  # Return the list of rows
print (load_data_from_csv("tests/data/example_one.csv"))
print (load_data_from_csv("tests/data/example_two.csv"))
print (load_data_from_csv("tests/data/example_three.csv"))
            #row[1] = float(row[1])  # Convert temperature to float
            #row[2] = float(row[2])  # Convert humidity to float
            #yield row  # Yield each row instead of appending to a list
            #row[2] = float(row[2])  # Convert humidity to float
            #row.append(row)  # Append each row to the list
            # Return the list of rows



"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """



def find_min(weather_data):
    if not weather_data:
        return ()
    #weather_data = [49, 57, 56, 55, 53]
    min_value = min [weather_data]
    min_index = weather_data.index(min_value)
    return min_value, min_index(weather_data, min_value)
print (f"The minimum value is: {min_value}")    
print (f"The index of the minimum value is {min_index}")
    
    #result = weather.find_min(temperatures)
   
"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
   






def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass





def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass





def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
