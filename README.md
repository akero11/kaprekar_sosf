# kaprekar_sosf

## Objective

Code [Kaprekar's routine](https://en.wikipedia.org/wiki/Kaprekar%27s_routine) for four-digit numbers.

I'm doing nothing serious, this is just for fun.

---

## Analysis

1. Input a number.
2. Add zeros to complete four digits.
3. Form the biggest and the smallest numbers possible.
4. Substract the first from the second.
5. If the result is not equal to 6174, repeat.
6. Stop.

> [1] 403  
> [2] 0403  
> [3] 4300 - 0034  
> [4] 4266  
> [5] .  
> [5] .  
> [5] .  
> [6] 6174

Note: Leading zeros are not permitted in python.

---

## Checklist

* [-] A function to add following zeros
* [-] A function to get the biggest and shortest numbers.

---
