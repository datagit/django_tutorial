# https://www.w3schools.com/python/python_functions.asp
def outer_func():
  def inner_func():
    print('Hello world!')
  inner_func()

outer_func()

def factorial(number):
  # Validate input
  if not isinstance(number, int):
    raise TypeError("Sorry, 'number' must be an integer.")
  if number < 0:
    raise ValueError("sorry, 'number' must be zero or positive.")
  def inner_factorial(number):
    if number <= 1:
      return 1
    return number * inner_factorial(number - 1)
  return inner_factorial(number)

result = factorial(4)
print (result)