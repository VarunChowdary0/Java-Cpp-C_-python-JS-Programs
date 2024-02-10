def WindowSum(nums,a):
   min_len = float('inf') # +infinet
   start = 0 
   end = 0
   Current_sum = 0
   while end < len(nums): # itterate over the nums form 0 to its length
      Current_sum = Current_sum + nums[end]  # Update the Sum
      end+=1 # extend the window
      while start < end and  Current_sum >= a: # starts if currents sum exeeds or equals to the "value"
         Current_sum = Current_sum - nums[start] # Back Tracking.
         start+=1 # Reducing the window 

         min_len = min(min_len , end-start+1)  # compairing the min_len and length of current_sum 
   return min_len
nums = list(map(int,input("Enter nums: ").split()))
a = int(input("A: "))
x = WindowSum(nums,a)
print(x)