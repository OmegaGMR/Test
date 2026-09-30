def heat_index(temp: float, humidity: float) -> float:

    ''' Compute the heat index for a temperature given the heat and humidity

    Arg:
        temp: Temperature in Celsius
        humidity: Humidity in %
    Returns:
        Heat Index: Heat Index in degrees

    '''
    return temp + 0.05 * humidity

#help(heat_index)

def hello(Name: str):

    return Name
    

