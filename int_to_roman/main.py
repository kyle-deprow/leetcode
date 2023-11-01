from typing import List

# Int to Roman solution involves iterating through a map
# of integer/numeral combinations.  To solve the problem
# of negative positioning of numerals (III = 3, IV=4, VI=6)
# Each negative combination is given it's own place in the mapping.
# When iterating backwards, these negative combinations will fill
# in naturally as the resultant is modulo'd repeatedly

ROM_MAP = {1000: 'M',
           900: 'CM',
           500: 'D',
           400: 'CD',
           100: 'C',
           90: 'XC',
           50: 'L',
           40: 'XL',
           10: 'X',
           9: 'IX',
           5: 'V',
           4: 'IV',
           1: 'I'}

class Solution:
  def intToRoman(self, num: int) -> str:
    ans = ''
    for int_val, rom_val in ROM_MAP.items():
      # Determine amount of times int val divides into num
      if num // int_val:
        # Replace int with multiples of rom_val
        ans += rom_val*(num//int_val)
      # Modulo with int_val to find remainder for rest of mapping
      num %= int_val
    return ans

if __name__ == '__main__':
  s = Solution()
  test_array = [5,2,0,3,1]
  print(s.findArray(test_array))