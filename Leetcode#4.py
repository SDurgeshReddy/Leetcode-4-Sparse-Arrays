def matchingStrings():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read the size of the strings array
    n = int(data[0])
    strings = data[1:n + 1]
    
    # Read the size of the queries array
    q = int(data[n + 1])
    queries = data[n + 2:n + 2 + q]
    
    # Create a dictionary to store the frequency of each string
    frequency_map = {}
    for string in strings:
        if string in frequency_map:
            frequency_map[string] += 1
        else:
            frequency_map[string] = 1
    
    # Prepare the result list by looking up the frequency map for each query
    result = []
    for query in queries:
        result.append(frequency_map.get(query, 0))
    
    # Print the result, one per line
    for res in result:
        print(res)
matchingStrings()
