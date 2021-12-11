import time
import random

NO_OF_COMPS = 0
TYPE = 0


def algochooser(list_elts, paint, label_comparison, something, TYPE_OF_DRAW, speed):
    global NO_OF_COMPS, TYPE
    TYPE = TYPE_OF_DRAW
    if something == "Bubble Sort":
        label_comparison.configure(text="No of comparisons: 0")
        bubblesort(list_elts, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["DarkOrange1"] * len(list_elts))
        NO_OF_COMPS = 0


    elif something == "Insertion Sort":
        label_comparison.configure(text="No of comparisons: 0")
        insertionsort(list_elts, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["DarkOrange1"] * len(list_elts))
        NO_OF_COMPS = 0

    elif something == "Merge Sort":
        label_comparison.configure(text="No of comparisons: 0")
        mergesort(list_elts, 0, len(list_elts), paint, label_comparison, speed)
        if TYPE == 0:
            paint(["DarkOrange1"] * len(list_elts))
        NO_OF_COMPS = 0

    elif something == "Quick Sort":
        label_comparison.configure(text="No of comparisons: 0")
        quicksort(list_elts, 0, len(list_elts) - 1, paint, label_comparison, speed)
        if TYPE == 0:
            paint(["DarkOrange1"] * len(list_elts))
        NO_OF_COMPS = 0


def bubblesort(list_elts, paint, label_comparison, speed):
    global NO_OF_COMPS, TYPE
    is_sort = False
    colors = []
    for i in range(len(list_elts) - 1):
        is_sort = True
        for j in range(len(list_elts) - 1 - i):
            if (list_elts[j] > list_elts[j + 1]):
                is_sort = False
                list_elts[j], list_elts[j + 1] = list_elts[j + 1], list_elts[j]
                time.sleep(1 / speed)
            NO_OF_COMPS += 1
            if TYPE == 0:
                colors = ["#cc0000" if x == list_elts[j] or x == list_elts[j + 1] else "antique white" for x in list_elts]
            else:
                colors = [((int)(x * 360) / 950) for x in list_elts]
            paint(colors)
            label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))
        if is_sort:
            break
        time.sleep(1 / speed)


def insertionsort(list_elts, paint, label_comparison, speed):
    global NO_OF_COMPS, TYPE
    colors = []
    for i in range(1, len(list_elts)):
        current = list_elts[i]
        y = i - 1
        while (y >= 0 and list_elts[y] > current):
            list_elts[y + 1] = list_elts[y]
            y -= 1
            NO_OF_COMPS += 1
            if TYPE == 0:
                for gh in range(len(list_elts)):
                    if y == gh:
                        colors.append("#cc0000")
                    elif gh == i:
                        colors.append("green")
                    else:
                        colors.append("antique white")
            else:
                colors = [((int)(x * 360) / 950) for x in list_elts]
            time.sleep(1 / speed)
            paint(colors)
            colors = []
            label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))
        list_elts[y + 1] = current
        NO_OF_COMPS += 1
        label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))


def mergesort(list_elts, left, right, paint, label_comparison, speed):
    if left < right:
        middle = (left + right) // 2
        mergesort(list_elts, left, middle, paint, label_comparison, speed)
        mergesort(list_elts, middle + 1, right, paint, label_comparison, speed)
        merge(list_elts, left, middle, right, paint, label_comparison, speed)


def merge(list_elts, left, middle, right, paint, label_comparison, speed):
    global NO_OF_COMPS, TYPE
    si = fi = 0
    colors = []
    firstlist = list_elts[left:middle + 1]
    secondlist = list_elts[middle + 1:right + 1]
    for ai in range(left, right + 1):
        if (fi < len(firstlist) and si < len(secondlist)):
            if (firstlist[fi] < secondlist[si]):
                list_elts[ai] = firstlist[fi]
                fi += 1
                NO_OF_COMPS += 1
            else:
                list_elts[ai] = secondlist[si]
                si += 1
        elif (fi < len(firstlist)):
            list_elts[ai] = firstlist[fi]
            fi += 1
        elif (si < len(secondlist)):
            list_elts[ai] = secondlist[si]
            si += 1
        if TYPE == 0:
            for x in range(len(list_elts)):
                if x > middle and x <= right:
                    colors.append("yellow")
                elif x >= left and x <= middle:
                    colors.append("teal")
                else:
                    colors.append("antique white")
        else:
            colors = [((int)(x * 360) / 950) for x in list_elts]
        paint(colors)
        time.sleep(1 / speed)
        label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))


def quicksort(list_elts, left, right, paint, label_comparison, speed):
    color = []
    if (left < right):
        mid = partition(list_elts, left, right, paint, label_comparison, speed)
        quicksort(list_elts, left, mid - 1, paint, label_comparison, speed)
        quicksort(list_elts, mid + 1, right, paint, label_comparison, speed)


def partition(list_elts, low, high, paint, label_comparison, speed):
    global NO_OF_COMPS, TYPE
    tracker = low
    pivot = list_elts[high]
    color = []
    if TYPE == 0:
        for i in range(len(list_elts)):
            if i == low and i == high - 1:
                color.append("#cc0000")
            elif i == high:
                color.append("yellow")
            else:
                color.append("antique white")
    else:
        color = [((int)(x * 360) / 950) for x in list_elts]
    paint(color)
    label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))
    for i in range(low, high, 1):
        if list_elts[i] <= pivot:
            list_elts[i], list_elts[tracker] = list_elts[tracker], list_elts[i]
            tracker += 1
            color = []
        time.sleep(1 / speed)
        NO_OF_COMPS += 1
        if TYPE == 0:
            for i in range(len(list_elts)):
                if i == low or i == high - 1:
                    color.append("#cc0000")
                elif i == high:
                    color.append("yellow")
                else:
                    color.append("antique white")
        else:
            color = [((int)(x * 360) / 950) for x in list_elts]
        paint(color)
        label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))
    list_elts[tracker], list_elts[high] = list_elts[high], list_elts[tracker]
    label_comparison.configure(text="No of comparisons: " + str(NO_OF_COMPS))
    return tracker
