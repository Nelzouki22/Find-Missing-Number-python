def find_missing_number(nums):
    n = len(nums)
    total = (n + 1) * (n + 2) // 2  # Sum of first n+1 natural numbers

    for num in nums:
        total -= num

    return total

# مثال على مصفوفة بها رقم مفقود
nums = [1, 2, 4, 5, 6]
missing_number = find_missing_number(nums)

print(f"The missing number is: {missing_number}")

