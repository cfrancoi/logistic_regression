import math

def standard_deviation(lst):
  """
  This function calculates the standard deviation of a list of numbers.

  Args:
      lst: A list of numbers.

  Returns:
      The standard deviation of the list, or None if the list is empty.

  Raises:
      TypeError: If the list contains non-numeric elements.
  """
  if not lst:
    return None
  
  # Check if all elements are numbers
  if not all(isinstance(x, (int, float)) for x in lst):
    raise TypeError("List must contain only numbers")

  mean_value = sum(lst) / len(lst)
  squared_differences = [math.pow(x - mean_value, 2) for x in lst]
  variance = sum(squared_differences) / (len(lst) - 1)  # Bessel's correction for population standard deviation
  return math.sqrt(variance)

# Example usage
my_list = [1, 2, 3, 4, 5]
result = standard_deviation(my_list)
print(result)  # Output: approximately 1.4142135623730951
