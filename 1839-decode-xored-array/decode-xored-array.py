class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        
        for number in encoded:
            output.append(output[-1]^number)
            
        print(output)
        return output

        