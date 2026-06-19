# This is a sample file with perfect code climate metrics
# It calculates the area of a circle

import math

def calculate_area(radius):
    # Ensure the radius is positive
    if radius < 0:
        return 0
    
    pi_value = math.pi
    calculated_area = pi_value * (radius ** 2)
    return calculated_area

# Execute function
final_result = calculate_area(5)
print(final_result)