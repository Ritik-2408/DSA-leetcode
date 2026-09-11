class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # used for storing the unique possible even numbers
        unique_even_numbers = set()
        n = len(digits) 
        # 3 nested loops for 3 positions, hundreds = digits(i), tens = digits(j), units = digits(k)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # ensure we use the distinct digit from the digits list
                    if i != j and j != k and i != k:
                        hundreds = digits[i]
                        tens = digits[j]
                        units = digits[k]

                        # Rule 1. Number should be even, units digit belogs to [0, 2, 4, 6, 8]
                        # Rule 2. Number should not have leading zero
                        if hundreds != 0 and units % 2 == 0:
                            num = hundreds * 100 + tens * 10 + units
                            unique_even_numbers.add(num)

        
        return len(unique_even_numbers)