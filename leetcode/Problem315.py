# Count of Smaller Numbers After Self

from bisect import bisect_left

def solution(nums):
    count = []

    for i in range(len(nums)):
        temp = 0
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                temp += 1
        count.append(temp)
    return count

def solutionUsingBinaryTree(nums):
    sortedNums, answer = sorted(nums), []

    for num in nums:
        i = bisect_left(sortedNums, num)
        answer.append(i)
        del sortedNums[i]
    return answer

# def countSmaller(self, nums: List[int]) -> List[int]:
#
#     def binarySearch(arr, x):
#         l = 0
#         h = len(arr)
#         while (l < h):
#             mid = (l + h) // 2
#             if (arr[mid] < x):
#                 l = mid + 1
#             else:
#                 h = mid
#         return l
#
#     def merge(v1, v2):
#         i = 0
#         j = 0
#         v = []
#         while (i < len(v1) and j < len(v2)):
#             if (v1[i] <= v2[j]):
#                 v.append(v1[i])
#                 i += 1
#             else:
#                 v.append(v2[j])
#                 j += 1
#         for k in range(i, len(v1)):
#             v.append(v1[k])
#         for k in range(j, len(v2)):
#             v.append(v2[k])
#         return v
#
#     def build(ind, tree, l, h):
#         if (l == h):
#             tree[ind].append(nums[l])
#             return
#         mid = (l + h) // 2
#         build(2 * ind + 1, tree, l, mid)
#         build(2 * ind + 2, tree, mid + 1, h)
#         tree[ind] = merge(tree[2 * ind + 1], tree[2 * ind + 2])
#
#     def query(ind, tree, lo, hi, l, r, x):
#         if (lo >= l and hi <= r):
#             return binarySearch(tree[ind], x)
#
#         if (l > hi or r < lo):
#             return 0
#
#         mid = (lo + hi) // 2
#         return query(2 * ind + 1, tree, lo, mid, l, r, x) + query(2 * ind + 2, tree, mid + 1, hi, l, r, x)
#
#     N = len(nums)
#     tree = [[] for _ in range(4 * N + 1)]
#     build(0, tree, 0, N - 1)
#     ans = []
#     for i in range(N - 1):
#         x = query(0, tree, 0, N - 1, i + 1, N - 1, nums[i])
#         ans.append(x)
#     ans.append(0)
#     return ans


if __name__ == '__main__':
    nums = [5, 2, 6, 1]
    print(solution(nums))
    print(solutionUsingBinaryTree(nums))
