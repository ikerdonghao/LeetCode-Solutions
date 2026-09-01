class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        self.max_gap = 0
        self.max_num_list = []
        for number in nums:
            self.max_digit = 0
            self.min_digit = 9
            self.cur_digit = None
            def int_num(test_number:int):
                if test_number == 0:
                    return
                self.cur_digit = test_number % 10
                if self.cur_digit > self.max_digit:
                    self.max_digit = self.cur_digit
                if self.cur_digit < self.min_digit:
                    self.min_digit = self.cur_digit
                int_num(test_number // 10)
            int_num(number)
            self.gap = self.max_digit-self.min_digit
            if self.gap > self.max_gap:
                self.max_gap = self.gap
                self.max_num_list = [number]
            elif self.gap == self.max_gap: 
                self.max_num_list.append(number)
        return sum(self.max_num_list)