def next_fit(block_sizes, process_sizes):
    num_blocks = len(block_sizes)
    num_processes = len(process_sizes)

    allocation = [-1] * num_processes  # Initialize all allocations as -1
    last_allocated_block = 0  # Pointer to track the last allocated block

    # Iterate through each process
    for i in range(num_processes):
        start = last_allocated_block  # Start searching from the last allocated block

        # Search for a suitable block
        while True:
            if block_sizes[last_allocated_block] >= process_sizes[i]:
                # Allocate memory
                allocation[i] = last_allocated_block
                block_sizes[last_allocated_block] -= process_sizes[i]
                break

            # Move to the next block, wrapping around if necessary
            last_allocated_block = (last_allocated_block + 1) % num_blocks

            # Stop if we've checked all blocks
            if last_allocated_block == start:
                break

    # Output results
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(num_processes):
        print(f"{i + 1}\t\t{process_sizes[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not Allocated")

# Example usage
block_sizes = [10, 15, 20, 40, 15]
process_sizes = [12, 18, 10]

next_fit(block_sizes, process_sizes)
