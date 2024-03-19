def percentile(lst, perc):
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

    sorted_data = sorted(lst)
    n = len(sorted_data)

    if n == 0:
        return None
    elif percentile == 0:
        return sorted_data[0]
    elif percentile == 100:
        return sorted_data[-1]

    percentile_index = (perc * (n -1)) / 100
    
    if  isinstance((percentile_index), int):
        return sorted_data[int(percentile_index)]
    else:
        lower_index = int(percentile_index)
        upper_index = lower_index + 1
        fractional_part = percentile_index - lower_index
        return sorted_data[lower_index] * (1 - fractional_part) + sorted_data[upper_index] * fractional_part
# Example usage
data = [4, 2, 2, 1, 6]

# Calculate percentiles
p10 = percentile(data, 10)
p50 = percentile(data, 50)  # Median
p90 = percentile(data, 90)

print("10th percentile:", p10)  # Output: 10th percentile: 1.4
print("50th percentile (median):", p50)  # Output: 50th percentile (median): 2.0
print("90th percentile:", p90)  # Output: 90th percentile: 5.2