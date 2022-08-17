class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        ten, five, one = ["M", "M", "C", "X"], ["M", "D", "L", "V"], ["M", "C", "X", "I"]
        ten_v, five_v, one_v = [1000, 1000, 100, 10], [1000, 500, 50, 5], [1000, 100, 10, 1]
        for i in range(4):
            local_str = ""
            num_one = num // one_v[i]
            if num_one <= 3:
                local_str += one[i] * num_one
            elif num_one == 4:
                local_str += one[i] + five[i]
            elif num_one <= 8:
                local_str += five[i] + one[i] * (num_one - 5)
            else:
                local_str += one[i] + ten[i]
                
            num %= one_v[i]
            
            out += local_str
        
        return out
        
        
        