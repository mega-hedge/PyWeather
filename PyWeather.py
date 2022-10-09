try: # Main code

  # Import libraries
  from pyowm import OWM # import weather lib

  from colorama import init, Fore # import colorama
  init( autoreset = True ) # init colorama

  from time import sleep # import lib for sleep

  from os import system as sy # import lib for clear display
  sy('mode 55, 2') # set start win size

  city = str( input( f'{Fore.GREEN}Enter city name: {Fore.RED}' ) ) # var for city name


  def clear(): sy('cls') # func for clear display
  clear()


  # infinity while
  while True:
      # get weather
      temp = int( 
        OWM( '6d28e4bd835224c7d329def4297c2488', # this key for weather lib
        ) .weather_manager() .weather_at_place(city) .weather .temperature("celsius") ['temp'] )

      sy( f'mode { 24 + len(city) }, 2' ) # set win size

      print( f'{Fore.GREEN}Temperature in {Fore.BLUE}{ city.capitalize() } : {Fore.RED}{temp} {Fore.BLUE}°C') # print temperature

      sleep(10) # delay on 10 sec
      clear() # clear display

except: # If have errors
  input('Error! Please, reset the program or press Enter for close!')