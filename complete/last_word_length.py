class Solution(object):
  def lengthOfLastWord(self, s): #good speed, great on memory
    #Runtime 19 ms Beats 43.99%
    #Memory 13.5 MB Beats 85.23%
    #split the word and put into an array (skip whitespace)
    word_count = s.split()
    #count the length of the last element
    return len(word_count[-1])

  # def lengthOfLastWord(self, s): #faster as not storing array in variable; memory comperable
  #   # Runtime 15 ms Beats 74.29%
  #   # Memory 13.4 MB Beats 85.23%
  #   return len(s.split()[-1])

string1 = "Hello, world"
string2 = "   fly me   to   the moon  "
string3 = "luffy is still joyboy"

solution = Solution()  # Create an instance of Solution
# Call the method on the instance
result1 = solution.lengthOfLastWord(string1)  
result2 = solution.lengthOfLastWord(string2)  
result3 = solution.lengthOfLastWord(string3)  

# Print the result
print(result1)
print(result2)
print(result3)  
