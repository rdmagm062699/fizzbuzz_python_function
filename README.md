# Python FizzBuzz Function Kata

## Prerequisites
[Poetry](https://python-poetry.org/docs/#installation)\
[Make](https://www.gnu.org/software/make/manual/make.html)


## The Challenge
Test drive a single function named `calculate` that will apply all of the rules of the FizzBuzz problem (see [below](#fizzbuzz-rules)).  The starter
code contains a module for the production code ([app/fizzbuzz.py](app/fizzbuzz.py)) and a single test module
([tests/test_fizzbuzz.py](tests/test_fizzbuzz.py))

You must follow the basic rule of Test Driven Development where as you cannot add any new logic to the `calculate` function in
([app/fizzbuzz.py](app/fizzbuzz.py)) without first having a failing test in ([tests/test_fizzbuzz.py](tests/test_fizzbuzz.py)).


## FizzBuzz Rules
The function named `calculate` accepts a single parameter that is an integer.  The function will return the following values
based on the input parameter:
* If the input parameter is a multiple of 3 then return the string "Fizz"
* If the input parameter is a multiple of 5 then return the string "Buzz"
* If the input parameter is a multiple of 3 and 5 then return the string "FizzBuzz"
* If the input paramter does not meet any of the 3 previous scenarios then just simply return
the input paramter

To run the tests simply execute `make tests`
