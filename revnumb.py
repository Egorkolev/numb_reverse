nums1 = int(input("Введите число:"))
nums2 = 0
while nums1 > 0:
    nums3 = nums1 % 10
    print(nums3)
    nums1 = nums1 // 10
    print(nums1)
    nums2 = nums2 * 10
    print(nums2)
    nums2 = nums2 + nums3
    print(nums2)
print("Перевернутое число:", nums2)



