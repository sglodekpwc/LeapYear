# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def isleapyear(year):
    # Use a breakpoint in the code line below to debug your script.
    checkifleap = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    print("rok ", year, "jest przystępny ", checkifleap)

    return checkifleap


def test_rok_ma_byc_przystepny():
    assert isleapyear(2020) == True


def test_rok_ma_niebyc_przystepny():
    assert isleapyear(2022) == False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rok = int(input("podaj rok: "))
    isleapyear(rok)


