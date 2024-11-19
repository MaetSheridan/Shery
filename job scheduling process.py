def job_scheduling(processing_times):
    # Sort jobs by processing time
    processing_times.sort()
    
    # Calculate completion times and total completion time
    completion_time = 0
    total_completion_time = 0
    
    for time in processing_times:
        completion_time += time
        total_completion_time += completion_time
    
    return total_completion_time

# Example processing times
processing_times = [3, 1, 4, 2, 5]

print("Minimum Total Completion Time:", job_scheduling(processing_times))
