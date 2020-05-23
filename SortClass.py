class SortClass:
    object_unsorted = []

    def __init__(self, number_arr=[4, -1, 2, 7, 6, 3, 10, -21, 44, -23, 15]):
        self.object_unsorted = number_arr

    # Selection sort ~ O(n^2) Idea: Split set to 2 subsets - sorted subset and unsorted subset.
    # For each iteration, remove next element and insert to the location in sorted set
    def selectionSort(self):
        for i, num in enumerate(self.object_unsorted):
            if i == 0:
                continue

            j = i
            value = self.object_unsorted[i]
            while j > 0 and self.object_unsorted[j - 1] > value:
                self.object_unsorted[j] = self.object_unsorted[j - 1]
                j = j - 1

            self.object_unsorted[j] = value

        print(self.object_unsorted)


x = SortClass()
x.selectionSort()
