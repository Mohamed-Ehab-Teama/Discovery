def estimate_time( distance, items ):
    # Check if the distance is negative
    if distance < 0:
        return "Distance Cannot be Negative Number"
    
    # Calculate Delievery Time
    delievery_time = distance / 100
    
    # Calculate Preparation Time
    prep_time = items * 5
    
    # Calculate Total Time
    total_time = delievery_time + prep_time
    
    return(total_time)
    
print(estimate_time(-500, 5))