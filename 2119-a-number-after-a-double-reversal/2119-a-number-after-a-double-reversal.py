class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        def reversals(old_number):
            new_num = 0
            remain = old_number
            last_digit = 0
            while remain > 0:
                last_digit = remain % 10
                remain = remain // 10
                new_num *= 10
                new_num += last_digit
            return new_num
        
        reversed1 = reversals(num)
        print(reversed1)
        print("-"*5)
        reversed2 = reversals(reversed1)
        print(reversed2)

        if reversed2 == num:
            return True
        else: 
            return False
