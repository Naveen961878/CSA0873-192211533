def find_mth_max_and_nth_min(array, m, n):
    sorted_array = sorted(array)
    mth_max = sorted_array[-m]
    nth_min = sorted_array[n - 1]
    return mth_max, nth_min
array = [14, 16, 87, 36, 25, 89, 34]
m = 1
n = 3
mth_max, nth_min = find_mth_max_and_nth_min(array, m, n)
sum_result = mth_max + nth_min
diff_result = mth_max - nth_min
print(f"{m}st Maximum Number:", mth_max)
print(f"{n}rd Minimum Number:", nth_min)
print("Sum =", sum_result)
print("Difference =", diff_result)
