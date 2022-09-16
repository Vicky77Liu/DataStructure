# counting sort 计数排序

def countingSort(arr):
    if not arr:
        return []
    max_num = max(arr)
    min_num = min(arr)
    n = len(arr)
    cnt = [0] * (max_num - min_num + 1)

    for num in arr:
        cnt[num - min_num] += 1
    print(cnt)
    j = 0
    for i in range(n):
        while cnt[j] == 0:
            j += 1
        arr[i] = j + min_num
        cnt[j] -= 1
    return arr



if __name__ == '__main__':
    a = countingSort([2, 9, 0, -1, -2])
    print(a)