def solution(score):
    # Calculate the average scores for each student along with their index
    averages = [(sum(scores) / 2, idx) for idx, scores in enumerate(score)]
    
    # Sort the list of averages in descending order, keeping track of original indices
    sorted_averages = sorted(averages, key=lambda x: -x[0])
    
    # Create a list to store ranks
    ranks = [0] * len(score)
    
    # Initialize variables for tracking the rank and previous average
    current_rank = 1
    previous_average = sorted_averages[0][0]
    
    # Assign ranks based on the sorted averages
    for i, (average, idx) in enumerate(sorted_averages):
        # If the current average is different from the previous one, update the current rank
        if average != previous_average:
            current_rank = i + 1
        
        # Assign the current rank to the student at the original index
        ranks[idx] = current_rank
        
        # Update previous average
        previous_average = average

    return ranks