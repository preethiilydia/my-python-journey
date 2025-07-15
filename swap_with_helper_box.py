# Initial values
a = 5
b = 10

# Step 1: Assume Tmp (temporary variable) is an empty box, and put the value of a; and now a becomes empty.
tmp = a      # tmp now holds the value of a; tmp = 5 

# Step 2: Assign the value of b to a; now a = 10 
a = b        # a now has the value of b

# Step 3: Assign the value from the empty box (tmp) to b ; 
b = tmp      # b now has the original value of a (which was stored in tmp)

# Final output after swapping
print("a is now:", a)  # Output: a is now: 10
print("b is now:", b)  # Output: b is now: 5
