""" This program serves as a metrics converter."""
__author__ = "Henrique Baggio"

import math
import time


def calc_kg_lbs(mass_kg):
    """
This function gets the mass in Kilos and multiply by a constant to give
the mass in Pounds
    :param mass_kg: The mass in Kilos to convert.
    :return: The mass in Pounds after being converted.
    """
    return mass_kg * 2.20462


def calc_kg_oz(mass_kg):
    """
This function gets the mass in Kilos and multiply by a constant to give
the mass in Ounces.
    :param mass_kg: The mass in Kilos to convert.
    :return: The mass in Ounces after being converted.
    """
    return mass_kg * 35.274


def calc_lbs_kg(mass_lbs):
    """
This function gets the mass in Pounds and divide by a constant to give
the mass in Kilos.
    :param mass_lbs: The mass in Pounds to convert.
    :return: The mass in Kilos after being converted.
    """
    return mass_lbs / 2.20462


def calc_lbs_oz(mass_lbs):
    """
This function gets the mass in Pounds and multiply by a constant to give
the mass in Ounces.
    :param mass_lbs: The mass in Pounds to convert.
    :return: The mass in Ounces after being converted.
    """
    return mass_lbs * 16


def calc_f_c(temp_f):
    """
This function gets the temperature in Fahrenheit subtracted by a constant and
then multiplied by another constant to give the temperature in Celsius.
    :param temp_f: The temperature in Fahrenheit.
    :return: The temperature in Celsius after being converted.
    """
    return (temp_f - 32) * 0.5555555556


def calc_f_k(temp_f):
    """
This function gets the temperature in Fahrenheit subtract by a constant,
then multiply by another constant and lastly is added by another constant to
give the temperature in Kelvin.
    :param temp_f: The temperature in Fahrenheit.
    :return: The temperature in Kelvin after being converted.
    """
    return (temp_f - 32) * 0.5555555556 + 273.15


def calc_c_f(temp_c):
    """
This function gets the temperature in Celsius multiplied by a constant and
then added by another to give the temperature in Fahrenheit.
    :param temp_c: The temperature in Celsius.
    :return: The temperature in Fahrenheit after being converted.
    """
    return (temp_c * 1.8) + 32


def calc_c_k(temp_c):
    """
This function gets the temperature in Celsius added by a constant.
    :param temp_c: The temperature in Celsius.
    :return: The temperature in Kelvin after being converted.
    """
    return temp_c + 273.15


def calc_m_ft(distance_m):
    """
This function gets the distance in Meter multiplied by a constant to give
the distance in Feet
    :param distance_m: The distance in Meters.
    :return: The distance in Feet after being converted.
    """
    return distance_m * 6.07


def calc_m_mi(distance_m):
    """
This function gets the distance in Meters divided by a constant to give the
distance in Miles.
    :param distance_m: The distance in Meters.
    :return: The distance in Miles after being converted.
    """
    return distance_m / 1609


def calc_area(radius):
    """
This function gets the radius squared and then multiplied by Pi to give the
area of the circle.
    :param radius: The radius of the circle.
    :return: The Area of the circle.
    """
    return radius ** 2 * math.pi


def calc_circumference(radius):
    """
This function gets the radius multiplied by a constant and then multiplied by
Pi to give the circumference of the circle.
    :param radius: The radius of the circle.
    :return: The circumference of the circle.
    """
    return radius * 2 * math.pi


def calc_volume(radius):
    """
This function gets the radius cubed, multiplied by Pi and then multiplied by a
constant to give the Volume of the sphere.
    :param radius: The radius of the circle.
    :return: The Volume of the circle.
    """
    return (4 / 3) * math.pi * radius ** 3


def calc_remainder(dividend, divisor):
    """
This function gets the dividend and divisor and makes the calculation to
give the result as a remainder.
    :param dividend: The dividend of the division.
    :param divisor: the divisor of the division.
    :return: The remainder of the division.
    """
    return dividend % divisor


def calc_hole_num_div(dividend, divisor):
    """
This function gets the dividend and divisor and makes the calculation to
give the result as a hole number division.
        :param dividend: The dividend of the division.
        :param divisor: the divisor of the division.
        :return: The result of the division as a hole number.
        """
    return dividend // divisor


def calc_actual_division(dividend, divisor):
    """
This function gets the dividend divided by the divisor give the result of
the division.
        :param dividend: The dividend of the division.
        :param divisor: the divisor of the division.
        :return: The result of the division.
        """
    return dividend / divisor


def main():
    """
This is the main function and it runs the entire program.
    """
    validation = True
    while validation:
        name = input("What is your name?: ")
        if name.isalpha():
            print("Hello ", name, "! Welcome to your Metrics ",
                  end="Buddy.\nThis "
                      "program will "
                      "help you "
                      "whenever you "
                      "need to convert "
                      "any "
                      "kind of data. \n",
                  sep="")
            validation = False
        else:
            print("Invalid name")

    # Now we are going to convert masses
    time.sleep(2)
    keep_running = 0
    while keep_running == 0:
        time.sleep(2)
        try:
            choice_of_conversion = str(input("=" * 69 + "\n\n\t\t*** Program Menu ***\n\n\n"
                                             "\t(1) - Kilogram to Pounds/Ounces \n"
                                             "\t(2) - Pounds to Kilograms/Ounces \n"
                                             "\t(3) - Fahrenheit to Celsius/Kelvin\n"
                                             "\t(4) - Celsius to Fahrenheit/Kelvin \n"
                                             "\t(5) - Meters / Foot \n"
                                             "\t(6) - Area / Circumference / Volume \n"
                                             "\t(7) - Remainder / Hole number Division / Actual Division \n"
                                             "\t(8) - Adding Calculator \n"
                                             "\t(9) - Average Calculator \n"
                                             "\t(0) - 'or, and, not \n"
                                             "\t(!) To stop the program\n"
                                             "Type the number of the correspondent  conversion you want to make: "))
        except TypeError:
            print("Invalid value. Try again.")


        if choice_of_conversion == '1':
            controller = 0
            while controller == 0:
                try:
                    choice = int(input("To convert from Kilograms to Pounds "
                                       "(1)\nTo convert from Kilograms to "
                                       "Ounces (2)\n:"))
                    if choice == 1:
                        mass_kg = float(
                            input("What is the mass in Kilograms you want to"
                                  " convert to Pounds?: "))
                        print("If it weight is {} Kilograms, then in lbs will"
                              " be: {:13.3f} lbs."
                              "".format(mass_kg, calc_kg_lbs(mass_kg)))
                    elif choice == 2:
                        mass_kg = float(
                            input("What is the mass in Kilograms you want "
                                  "to convert to Ounces?: "))
                        print("If it weight is {} Kilograms, then is Oz "
                              "will be: {:15.3f} Oz."
                              .format(mass_kg, calc_kg_oz(mass_kg)))
                    elif choice != (1, 2):
                        pass
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")
                    print()

        if choice_of_conversion == '2':
            controller = 0
            while controller == 0:
                try:
                    choice = int(input("To convert from Pounds to Kilograms"
                                       " (1)\nTo convert from "
                                       "Pounds to Ounces (2)\n:"))
                    if choice == 1:
                        mass_lbs = float(input("What is the mass in pounds"
                                               " you want to convert"
                                               " for Kilograms?: "))
                        print("If the weigh is {} lbs , then in Kilograms"
                              " will be: {:13.3f} Kg"
                              .format(mass_lbs, calc_lbs_kg(mass_lbs)))
                    elif choice == 2:
                        mass_lbs = float(input("What is the mass in Pounds "
                                               "you want to convert for "
                                               "Ounces?: "))

                        print("If the weigh is {} lbs , then in Ounces will"
                              " be: {:16.3f} Oz"
                              .format(mass_lbs, calc_lbs_oz(mass_lbs)))
                    elif choice >= 3:
                        pass
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

        # Now we are going to convert temperatures
        if choice_of_conversion == '3':
            controller = 0
            while controller == 0:
                try:
                    choice = int(input("To convert from Fahrenheit to Celsius"
                                       " (1)\nTo convert fromFahrenheit "
                                       "to Kelvin (2)\n:"))
                    if choice == 1:
                        temp_f = float(input("What is the temperature in "
                                             "fahrenheit that you want "
                                             "to convert to Celsius?: "))
                        print("If it is {} ºF, then in Celsius will be: "
                              "{:24.1f} ºC".format(temp_f, calc_f_c(temp_f)))

                    elif choice == 2:
                        temp_f = float(input("What is the temperature in "
                                             "fahrenheit that you want to "
                                             "convert to Kelvin?: "))
                        f_k = calc_f_k(temp_f)
                        print("If it is {} ºF, then in Kelvin will be: "
                              "{:25.1f} ºK".format(temp_f, f_k))
                    else:
                        pass
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

        if choice_of_conversion == '4':
            controller = 0
            while controller == 0:
                try:
                    choice = int(input("To convert from Celsius to Fahrenheit"
                                       " (1)\nTo convert from Celsius to "
                                       "Kelvin (2)\n:"))
                    if choice == 1:
                        temp_c = float(input("What is the temperature in "
                                             "Celsius that you want to "
                                             "convert to Fahrenheit?: "))
                        print("If it is {} ºC, then in Fahrenheit will be: "
                              "{:21.1f} ºC".format(temp_c, calc_c_f(temp_c)))
                    elif choice == 2:
                        temp_c = float(input("What is the temperature in "
                                             "Celsius that you want to "
                                             "convert to Kelvin?: "))
                        print("If it is {} ºC, then in Kelvin will be: "
                              "{:25.1f} ºK".format(temp_c, calc_c_k(temp_c)))
                    else:
                        pass
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

        # Now we are going to convert distances
        if choice_of_conversion == '5':
            controller = 0
            while controller == 0:
                try:
                    choice = int(input("To convert from Meters to Feet (1)"
                                       "\nTo convert from Meters to"
                                       " Miles (2)\n:"))
                    if choice == 1:
                        distance_m = float(input("What is the distance in "
                                                 "Meters that you want "
                                                 "to convert to Feet? :"))
                        print("If it is {}m, then in Feet will be: {:29.2f}Ft"
                              .format(distance_m, calc_m_ft(distance_m)))
                    elif choice == 2:
                        distance_m = float(input("What is the distance in "
                                                 "Meters that you want "
                                                 "to convert to Miles? :"))
                        print("IF it is {}m, then in Miles will be: {:29.8f}Mi"
                              .format(distance_m, calc_m_mi(distance_m)))
                    else:
                        pass
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

        # Now we are going to use radius to calculate the area,
        # the circumference  and the volume
        if choice_of_conversion == '6':
            controller = 0
            while controller == 0:
                try:
                    radius = float(input("Insert the radius and it will give"
                                         " you the area, the circumference"
                                         " and the volume of the sphere: "))

                    print("If the radius of the circle is {}, then the area"
                          " is: {:15.2f}".format(radius, calc_area(radius)))
                    print("If the radius of the circle is {}, then the "
                          "circumference is: {:6.2f}"
                          .format(radius, calc_circumference(radius)))
                    print("If the radius of the circle is {}, then the "
                          "volume is: {:13.2f}"
                          .format(radius, calc_volume(radius)))
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

    # Now we are going to divide some values to get the remainder, hole number
        # division and the actual value
        if choice_of_conversion == '7':
            controller = 0
            while controller == 0:
                try:
                    dividend = float(input("Plug the dividend and after plug"
                                           " the divisor to calculate "
                                           "the remainder: "))
                    divisor = float(input())

                    print("this is the remainder: {:46.0f}"
                          .format(calc_remainder(dividend, divisor)))
                    print("This is the division and the answer is shown as "
                          "a hole number: {:6.0f}"
                          .format(calc_hole_num_div(dividend, divisor)))
                    print("this is the actual answer for the division: "
                          "{:25.3f}"
                          .format(calc_actual_division(dividend, divisor)))
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")
        # Adding Calculator
        if choice_of_conversion == '8':
            controller = 0
            while controller == 0:
                try:
                    print("Keep adding numbers and when you are done"
                          " type '-99' and  will give you the sum of "
                          "all these numbers")
                    list_of_num = []
                    x = 0
                    while x == 0:
                        num = float(input())
                        if num != -99:
                            list_of_num.append(num)
                        else:
                            x += 1
                            print(list_of_num)
                            print(sum(list_of_num))
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

        # Average calculator
        if choice_of_conversion == '9':
            controller = 0
            while controller == 0:
                try:
                    list_avg = []
                    amount_of_num = int(input("Enter the number of numbers "
                                              "you want to calculate the "
                                              "average: "))
                    print("Now enter the numbers you want to calculate"
                          " the average")
                    for x in range(amount_of_num):
                        num = float(input())
                        list_avg.append(num)
                    print((sum(list_avg) / len(list_avg)))
                    controller += 1
                    print()
                except ValueError:
                    print("Invalid input. \nPlease enter a number")

        # now I'll explain how 'or', 'and', 'not' works
        if choice_of_conversion == '0':
            x = 10
            y = 7
            # Now i'll explain 'OR'
            print("We are going to assign X = 10 and Y = 7 to exemplify the "
                  "use of 'OR, AND, NOT' ")
            print("You will use 'OR' when you want to compare some given "
                  "data and if at least one of the information is True "
                  "the statement is True as "
                  "well, and it will only be False if both are False "
                  "\nCheck the example below.\n")
            print("If X == Y or X > Y print 'True' otherwise print 'False'")
            if x == y or x > y:
                print(True)
            else:
                print(False, "\n")
            time.sleep(4)
            print()
            print()
            # Now I'll explain 'AND'
            print("You will use 'AND' when you want to compare some given "
                  "data and if both information are True the statement is "
                  "True as "
                  "well, and it is False if at least 1 of the information"
                  " is False \nCheck the example below.\n")
            print("If X == Y and X > Y print 'True' otherwise print 'False'")
            if x == y and x > y:
                print(True)
            else:
                print(False, "\n")
            time.sleep(4)
            print()
            print()
            # Now I'll explain 'NOT'
            print("You will use 'NOT' when you want to compare some given data"
                  " and if the information is False the statement is True  "
                  "and it is False if the information is True "
                  "\nCheck the example below.\n")
            print("If not X == Y ")
            if not x == y:
                print(True)
            else:
                print(False, "\n")

        if choice_of_conversion == '!':
            print("Thank you for using the program!")
            keep_running += 1


if __name__ == "__main__":
    main()
