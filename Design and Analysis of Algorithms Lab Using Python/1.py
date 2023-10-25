# Q1

def main():
	n = int(input())
	arr = []
	for i in range(n):
		arr.append(int(input()))
	x = int(input())
  index = 0
  for i in range(len(arr)):
    if arr[i] == x:
      print(i+1)
      break
  else:
    print("item not found")
  
	    	                    	            	        
if __name__ == "__main__":
	main()
