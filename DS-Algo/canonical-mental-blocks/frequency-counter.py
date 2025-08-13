def frequency_counter(arr):
    """
    This function takes an array of integers and returns a dictionary with the frequency of each integer.
    It uses a pointer-like approach to traverse the array and count occurrences.
    
    :param arr: List[int] - List of integers
    :return: dict - Dictionary with integers as keys and their frequencies as values
    """
    frequency = {}
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
            
    return frequency

# Example usage:
if __name__ == "__main__":
    sample_array = [1, 2, 2, 3, 3, 3, 4]
    result = frequency_counter(sample_array)
    print(result)  # Output: {1: 1, 2: 2, 3: 3, 4: 1}














