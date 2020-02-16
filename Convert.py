# Exercise 4
# def main():
#     fa = eval(input("Enter the temperature in F: "))
#     cel = (fa - 32) * 5 / 9
#     print("The temperature in C is: ", cel)
#
#
# for i in range(5):
#     main()
#
# input("Press the <Enter> key to exit.")


# Exercise 5
def main():
    print("This program calculates equivalent Celsius and Fahrenheit temperatures every 10 degrees from 0°C to 100°C:")
    for i in range(0, 101, 10):
        celsius = i
        fahrenheit = celsius * 9/5 + 32
        print(celsius, "   ", fahrenheit)
        # print(celsius, "degrees Celsius equals to", fahrenheit, "degrees Fahrenheit.")


main()


