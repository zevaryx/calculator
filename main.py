import sys
from calculator import calculate

if __name__ == "__main__":
    MIN_PYTHON = (3, 10)

    if sys.version_info < MIN_PYTHON:
        sys.exit("Python {}.{} or later is required".format(*MIN_PYTHON))

    while True:
        try:
            text = input(">> ")
            if value := calculate(text):
                print(value)
        except Exception as e:
            print(e)
