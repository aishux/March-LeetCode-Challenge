class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wordlist2 = [i.lower() for i in wordlist]
        wordlist3 = [re.sub(r'[aeiouAEIOU]', '1', i )for i in wordlist2]
        lst = []
        for i in queries:
            if i in wordlist:
                lst.append(i)
            elif i.lower() in wordlist2:
                lst.append(wordlist[wordlist2.index(i.lower())])
            elif re.sub(r'[aeiou]', '1', i.lower()) in wordlist3:
                lst.append(wordlist[wordlist3.index(re.sub(r'[aeiou]', '1', i.lower()))])
            else:
                lst.append("")
        return lst
