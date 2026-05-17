class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        i = len(digits) - 1
        carry = 0
        while i >= 0:
            value = digits[i]
            if i == len(digits) - 1:
                value += 1
            else:
                value += carry
            carry = value // 10
            value = value % 10
            res.append(value)
            if i == 0 and carry:
                res.append(carry)
            i -= 1
        return res[::-1]
            
        