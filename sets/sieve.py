def triplets_with_sum(n):
    if n < 6:  # Smallest Pythagorean triplet is 3,4,5 with sum 12
        return []
    
    triplets = []
    
    # a must be less than n/3 since a < b < c and a + b + c = n
    for a in range(1, n // 3 + 1):
        # Using the derived formula: b = (n²/2 - n*a) / (n - a)
        numerator = n * n - 2 * n * a
        denominator = 2 * (n - a)
        
        if denominator > 0 and numerator % denominator == 0:
            b = numerator // denominator
            
            # Check if a < b and b results in valid c
            if a < b:
                c = n - a - b
                if b < c:  # We know a² + b² = c² from the derivation
                    triplets.append([a, b, c])
    
    return triplets