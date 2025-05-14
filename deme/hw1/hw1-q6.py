def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Step 2: Verify the candidate
    candidate_count = sum(1 for num in nums if num == candidate)
    if candidate_count > len(nums) // 2:
        return candidate
    else:
        return None
nums = [2,2,1,1,1,2,2]
print(majority_element(nums))