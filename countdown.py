"""A basic countdown timer"""
from time import sleep


def countdown(timer):
    """counts down from specified number of seconds"""
    # timer: the user input for how long the countdown should be, in seconds
    while timer > 0:
        print(timer)
        timer -= 1
        sleep(1.0)
    print("Done!")


def main():
    """the main function"""
    while True:
        while True:
            try:
                timer = int(
                    input("\nHow many seconds do you want to count down from?\n-: "))
                break
            except ValueError:
                print("\n Invalid input! Please enter a time in seconds.")
        if timer <= 0:
            print("Please enter a number larger than 0")
        else:
            countdown(timer)
        break


if __name__ == "__main__":
    main()
