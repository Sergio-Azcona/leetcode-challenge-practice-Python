# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
  # Open brackets must be closed by the same type of brackets.
  # Open brackets must be closed in the correct order.
  # Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
  def bracket_hash(self):
    return {
      "(": ")",
      "{": "}",
      "[": "]"
    }
  
  # return false if input_array.len() not / 2 # if odd return false
  def input_length(self, input_array): 
    return len(input_array) % 2 == 0
  
  def isValid(self, s):
    #split characters; hold in array
    input_array = list(s)
    if not self.input_length(input_array):
        return False
    first = input_array[0]
    second = input_array[1]
    dict_hash = self.bracket_hash()
    
    if dict_hash.get(first) == second and len(input_array) > 3:
        #continue to pop index positions while they are key:value pair
        input_array.pop(1)
        input_array.pop(0)
        #recursion(input is the updated, single string)
        return self.isValid("".join(input_array))
    elif dict_hash.get(first) == second and len(input_array) == 2:
      return True 
    
    #do not need this code b/c i account for odd number of characters in input_length function
    # elif dict_hash.get(first) == second and len(input_array) == 1:
    #   return False

    return False

    

  #if they do not match return false
#when input_array is empty: return true

        




solution = Solution()  # Create an instance of Solution
# Call the method on the instance
r1 = solution.isValid("()")
r2 = solution.isValid("()[]{}") #true
r3 =solution.isValid("(]") #false
r4 =solution.isValid("(") #false

print(r1)
print(r2)
print(r3)
print(r4)