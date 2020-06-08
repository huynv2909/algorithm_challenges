class SortClass:
    object_unsorted = []

    def __init__(self, number_arr=[4, -1, 2, 7, 6, 3, 10, -21, 44, -23, 15]):
        self.object_unsorted = number_arr

    def printResult(self):
        print(self.object_unsorted)

    def swap(self, i, j):
        temp = self.object_unsorted[i]
        self.object_unsorted[i] = self.object_unsorted[j]
        self.object_unsorted[j] = temp

    # Selection sort ~ O(n^2) Idea: Split set to 2 subsets - sorted subset and unsorted subset.
    # For each iteration, remove next element and insert to the location in sorted set
    def insertionSort(self):
        for i, num in enumerate(self.object_unsorted):
            if i == 0:
                continue

            j = i
            value = self.object_unsorted[i]
            while j > 0 and self.object_unsorted[j - 1] > value:
                self.object_unsorted[j] = self.object_unsorted[j - 1]
                j = j - 1

            self.object_unsorted[j] = value

    def selectionSort(self):
        for i, num in enumerate(self.object_unsorted):
            # find smallest element on unsorted subset
            index = i
            for j in range(i + 1, len(self.object_unsorted) - 1):
                if self.object_unsorted[index] > self.object_unsorted[j]:
                    index = j

            self.swap(i, index)

    def bubbleSort(self):
        swapped = True
        k = 0
        while swapped:
            swapped = False
            for i in range(len(self.object_unsorted) - 1 - k):
                if self.object_unsorted[i] > self.object_unsorted[i + 1]:
                    self.swap(i, i + 1)
                    swapped = True
            k += 1

    def merge(self, start, mid, end):
        temp_list = self.object_unsorted.copy()
        i = start
        j = mid + 1
        k = i
        while i <= mid and j <= end:
            if self.object_unsorted[i] < self.object_unsorted[j]:
                temp_list[k] = self.object_unsorted[i]
                i += 1
            else:
                temp_list[k] = self.object_unsorted[j]
                j += 1
            k += 1

        while i <= mid:
            temp_list[k] = self.object_unsorted[i]
            k += 1
            i += 1

        for i in range(start, end + 1):
            self.object_unsorted[i] = temp_list[i]

    def mergeSortRecursion(self, low, high):
        if high == low:
            return

        mid = (low + ((high - low) >> 1))

        self.mergeSortRecursion(low, mid)
        self.mergeSortRecursion(mid + 1, high)

        self.merge(low, mid, high)

    def mergeSort(self):
        self.mergeSortRecursion(0, len(self.object_unsorted) - 1)


x = SortClass()
x.mergeSort()
x.printResult()
