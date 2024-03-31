class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output=""
        while columnNumber>0:
            offset = (columnNumber-1)%26
            output+=chr(ord("A")+offset)
            columnNumber=(columnNumber-1)//26
            print(offset,output,columnNumber)
        return output[::-1]

        
