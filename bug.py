def function_with_uncommon_error(data):
    try:
        result = data['key']  # Accessing a potentially missing key
        return result
    except KeyError:
        return None  # Basic handling of missing key

# Example Usage
data1 = {'key': 'value'}
data2 = {}

print(function_with_uncommon_error(data1))  # Output: value
print(function_with_uncommon_error(data2))  # Output: None