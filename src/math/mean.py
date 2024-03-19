def mean(lst):
  """
  This function calculates the mean of a list of numbers.

  Args:
      lst: A list of numbers.

  Returns:
      The mean of the list.

  Raises:
      TypeError: If the list is empty or contains non-numeric elements.
  """
  if not lst:
    raise TypeError("List cannot be empty")
  
  # Check if all elements are numbers
  if not all(isinstance(x, (int, float)) for x in lst):
    raise TypeError("List must contain only numbers")

  return sum(lst) / len(lst)

# Example usage
my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print(result)  # Output: 3.0
