#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a fahrenheit temperature: ")
  tempF = int(tempF)

  tempC = (tempF - 32) * (5/9)
  num = tempC
  rounded = round(num, 1)
  print(tempF, "is ", rounded, "degrees celsius.")
if __name__ == '__main__':
  main()
