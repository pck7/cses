arr = input()
length = i = j = 0
 
while j<len(arr):
  
	if arr[i]!=arr[j]:
		i = j
    
	length = max(length, j-i+1)
	j+=1
  
print(length)
