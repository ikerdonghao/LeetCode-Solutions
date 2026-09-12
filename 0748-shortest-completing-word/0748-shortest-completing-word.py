class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        parsedLicense = ""
        for char in licensePlate.lower():
            if char in "abcdefghijklmnopqrstuvwxyz":
                parsedLicense = parsedLicense + char
        print(parsedLicense)

        def wordToDict(w):
            word_dict = {}
            for char in w:
                if char in word_dict:
                    word_dict[char] += 1
                else:
                    word_dict[char] = 1
            return word_dict
        
        licenseDict = wordToDict(parsedLicense)
        print(licenseDict)
        print("-"*5)

        min_length = 16
        target = ""
        for word in words:
            
            candidate_dict = wordToDict(word)
            print(candidate_dict)
            found = 1
            for key,value in licenseDict.items():
                if key not in candidate_dict:
                    found = 0
                    break
                if licenseDict[key] > candidate_dict[key]:
                    found = 0
                    break
            if len(word) < min_length and found == 1:
                min_length = len(word)
                target =  word
            print("-"*2)
        
        return target



