# Swift_Navigation_Arivan

In the programming language of your choice, write a program generating the first n Fibonacci numbers F(n), printing

"Buzz" when F(n) is divisible by 3.
"Fizz" when F(n) is divisible by 5.
"FizzBuzz" when F(n) is divisible by 15.
"BuzzFizz" when F(n) is prime.
the value F(n) otherwise.

# Usage

In Command Line, in directory of file type the following. Third argument is number of Fibonacci numbers (n) to be printed.

```
$ python swiftnav.py <n>
```
# Methodology

For each calculated Fibonacci number, we first check to see if the number is even, then whether it is divisible by 15 because this takes priority over 3 and 5. Then if it is divisible by 3, then 5, then whether it is prime. When checking for primality, we initially check to see if we have already checked to see if this number is prime by checking the class dictionary. Otherwise, we see if the Fibonacci number is divisible by any of the odds from 7 (we have already checked 2, 3, and 5, and all evens) to the square root of the Fibonacci number. We only have to check until the square root because for every number greater than the square root that divides the Fibonacci number evenly, we would have already checked its complement that is smaller than the square root, and thus we do not need to check the numbers greater than the square root.
