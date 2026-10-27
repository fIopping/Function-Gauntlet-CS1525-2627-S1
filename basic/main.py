def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: numBer to check
    :return: True if number is even and False if it is odd
    """

    return number % 2 ==0
    


def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text: text to count
    :return: number of vowels
    """
    count = 0

    for letter in text.lower():
        if letter in "aeiou":
            count += 1

    return count
    


def celsius_to_fahrenheit(celsius:float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: temp in celsius
    :return: temp in fahrenheit
    """
    return (celsius * 9 / 5) + 32
    


def reverse_text(text:str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: text to reverse
    :return: text in reverse order
    """
    return text[::-1]
    


def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a: first number
    :param b: second number
    :return: larger number
    """
    if a > b:
        return a
    else:
        return b
    


def average_two(a:int, b:int) -> float:
    """Calculate and return the average of two integers.

    :param a: first number
    :param b: second number
    :return: average
    """
    return (a+b) / 2
    


def can_afford(balance: float, cost:float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: money you got
    :param cost: the price
    :return: true if you can afford, false if not
    """
    return balance >= cost
    


def repeat_text(text: str, times: int) -> str:
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text: text to repat
    :param times: how many times to repeat
    :return: the repeated text
    """
    return text * times
    


def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence: sentence to check
    :param word: word to look for
    :return: True if the word shows, false if not
    """
    return word in sentence
    


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost: cost of meal
    :param percent: tip percentage
    :return: tip amount
    """
    return cost * percent / 100
    


def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    Example:
        "Ada" and "Lovelace" returns "AL".

    :param first_name: persons first name
    :param last_name: persons last name
    :return: Uppercase initials
    """
    return (first_name[0] + last_name[0]).upper()
    

def percent_score(points: float, possible: float) -> float | None:
    """Calculate what percentage of the possible points
    were earned. Return None if possible is less than 1.

    Example:
        18 out of 20 returns 90.0.

    :param points: points earned
    :param possible: total points
    :return: percentage, or none if possible is less than 1.
    """
    if possible < 1:
        return None
    return (points / possible) * 100
    


def is_between(number: float, minimum: float, maximum: float) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.

    :param number: number to check
    :param minimum: smallest number
    :param maximum: large number
    :return: true if the number is in the list, false if not
    """
    return minimum <= number <= maximum
    


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise,return False.

    :param a: The first string
    :param b: The second string
    :param c: The third string
    :return: true if all strings are different, false if not.
    """
    return a != b and b != c and c != a
    


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.

    :param a: The first number
    :param b: The second number
    :param c: The third number
    :return: The average of the 3 numbers
    """
    return (a + b + c) / 3
    


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature: temp to check
    :param cold_limit:temperature below cold_limit
    :param hot_limit: temperature above hot_limit
    :return: cold or hot or comfortable
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"
    

if __name__ == "__main__":
    """
    If you want to test any of your code manually
    you can place function calls down here.
    Additionally, there is a test file loaded into
    this folder that you can run a test on your code.
    """
    

