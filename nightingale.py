# sort
def insertion_sort(arr):
   for i in range(1, len(arr)):
      temp = arr[i]
      pos = binary_search(arr, temp, 0, i) + 1
      for k in range(i, pos, -1):
         arr[k] = arr[k - 1]
      arr[pos] = temp

def judge(optionA, optionB ):
   print("Is A more important than B? ")
   print("A: ",optionA)
   print("B: ",optionB)
   return input()

def binary_search(arr, key, start, end):
   #key
   if end - start <= 1:
      if judge(arr[start],key) == 'T':
         return start - 1
      else:
         return start\

   mid = (start + end)//2
   if judge(key,arr[mid]) == 'T':
      return binary_search(arr, key, mid, end)
   else:
      return binary_search(arr, key, start, mid)

def get_issues_array():
   issues = []
   ## gh issue list -l "bug" 
   with open('issues.csv', 'r') as f:
      for line in f:
         issues.append(line.split(','))
   return issues

def array_to_csv(issues):
   with open('issues_out.csv', 'w') as f:
      for issue in issues:
         f.write(','.join(issue))


def main():
   issues = get_issues_array() 
   insertion_sort(issues)
   print("Done, look for the csvs in the same folder")
   array_to_csv(issues)


def test():
   issues = ["high", "extreamly Low",  "medium", "extreamly high","low"]
   n = len(issues)
   insertion_sort(issues)
   print("Sorted array is:")
   for i in range(n):
      print(issues[i],end=" ")

main()