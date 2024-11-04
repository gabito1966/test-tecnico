def puedeFormarSuma(nums, required_sum):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == required_sum:
                return True
    return False


#Ejemplo 1

nums1 = [1, 4, 3, 9]
required_sum1 = 8
print(puedeFormarSuma(nums1, required_sum1))  # Salida: False

#Ejemplo 2

nums2 = [1, 2, 4, 4]
required_sum2 = 8
print(puedeFormarSuma(nums2, required_sum2))  # Salida: True