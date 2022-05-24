import collections
import heapq

def part_shannon_fano(probs, beg, end):
    if(beg == end): return
    y = beg
    z = end
    sumLeft = 0.0
    sumRight = 0.0
    while(y<=z):
        if(sumLeft<=sumRight):
            sumLeft += probs[y][0]
            y += 1
        else:
            sumRight+=probs[z][0]
            z -= 1
    for h in range(beg, y):
        probs[h][1][1] =  probs[h][1][1] + "1"
    for h in range(y, end + 1):
        probs[h][1][1] =  probs[h][1][1] + "0"
    
    part_shannon_fano(probs, beg, y-1)
    part_shannon_fano(probs, y, end)

def partition(array, low, high):
  # Choose the rightmost element as pivot
  pivot = array[high][0]
  # Pointer for greater element
  i = low - 1
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if (array[j][0]) <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  # Return the position from where partition is done
  return i + 1
 
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
    # Recursive call on the left of pivot
    quick_sort(array, low, pi-1)
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)
      


def shannon_fano(toEncode):
    arr = toEncode
    dendograma = [[frequencia/len(arr), [simbolo, ""]] for simbolo, frequencia in collections.Counter(arr).items()]
    quick_sort(dendograma,0,len(dendograma)-1)
    part_shannon_fano(dendograma, 0, len(dendograma)-1)
    dendograma = {codigos[0] : codigos[1] for prob, codigos in dendograma}
    return dendograma