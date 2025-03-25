### Task 1: Function with Default Parameters

# Write a function `mix` that:

# - Takes parameters `a`, `b=5`, and `c=False`
# - Returns a tuple: `(a + b, "yes" if c else "no")`
# - Test it with:
#   - `print(mix(3)[1])` (expected: `"no"`)
#   - `print(mix(2, 3, True)[0])` (expected: `5`)

# def mix(a, b=5, c=False):
#     first_element = a + b 
#     second_element = "yes" if c else "no"
#     return(first_element, second_element)

# print((mix(3)[1]))
# print(mix(2, 3, True)[0])

### Task 2: Recursion and List Manipulation

# Write a program that:

# - Defines a recursive function `build(n)` that:
#   - Takes a number `n`
#   - Returns a list starting with `n`, followed by the result of `build(n-2)` if `n > 0`
#   - Returns an empty list `[]` if `n <= 0`
# - Prints `build(6)`
# - Expected output: `[6, 4, 2, 0]`

def build(n):
    if n <= 0:
        return([])

    return [n] + build(n-2)
print(build(6))