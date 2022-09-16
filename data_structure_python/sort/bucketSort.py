
 def bucketSort(nums):
    min_num = min(nums)
    max_num = max(nums)

    #桶的大小
    bucked_range = (max_num - min_num) / len(nums)

    #桶数组
    count_list = [[] for _ in range(len(nums) + 1)]

    #向桶数组里填数
    for i in nums:
        count_list[int((i - min_num) // bucked_range)].append(i)

    nums.clear()

    for i in count_list:
        for j in sorted(i):
            nums.append(j)

    return nums