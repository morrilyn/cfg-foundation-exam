# 25 marks 
"""Write  a  function  which  when  given  a  number  of  students, 
calculates and prints out a string for your proposed number of classes, and a dictionary 
showing the allocation"""

import math

def calculate_classes(num_students):
    # Define the maximum class size
    max_class_size = 30
    
    # Calculate the number of classes needed
    num_classes = max(2, (num_students + max_class_size - 1) // max_class_size)  # Add max_class_size - 1 for ceiling effect without math.ceil
    
    # Distribute the students across the classes as evenly as possible
    # First, give each class an equal number of students
    base_students_per_class = num_students // num_classes
    
    # Then, distribute any remaining students one per class until there are no more
    extra_students = num_students % num_classes
    
    # Create the allocation dictionary
    allocation = {}
    for class_number in range(1, num_classes + 1):
        # If there are extra students, add one to some classes
        if class_number <= extra_students:
            allocation[f'Class {class_number}'] = base_students_per_class + 1
        else:
            allocation[f'Class {class_number}'] = base_students_per_class
    
    # Prepare the output string
    proposed_allocation_str = f"Proposed Allocation: {num_classes} classes"
    
    # Return the results
    return proposed_allocation_str, allocation

# Let's test the function with an example
calculate_classes(31), calculate_classes(59), calculate_classes(87)

    
