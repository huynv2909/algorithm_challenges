class SearchClass:
    def BinarySearch(self, A, target):
        result = -1
        (left, right) = (0, len(A) - 1)

        while left <= right:
            mid = (left + ((right - left) >> 1))

            if A[mid] == target:
                result = mid
                break

            if target < A[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if result == -1:
            print(str(target) + " not found!")
        else:
            print(str(target) + " is at " + str(result))

