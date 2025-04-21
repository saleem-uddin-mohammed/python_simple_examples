#this method uses inbuild reverse method which will reverse array in-place
def reverseArray_usingInbuildMethod(nums):
    nums.reverse()
    return nums


def reverseArrayUsingStartEnd(nums): #Uses two pointers
    start = 0
    end = len(nums) - 1

    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
        return nums
    return None


def reverseArrayUsingSlice(nums): #uses array slice from reverse
    return nums[::-1]

print(reverseArray_usingInbuildMethod([1,2,3,4,5]))
print(reverseArrayUsingStartEnd([1,2,3,4,5]))
print(reverseArrayUsingSlice([1,2,3,4,5]))
print(slicingExamples([1,2,3,4,5]))



