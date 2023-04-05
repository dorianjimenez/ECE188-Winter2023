from collections import Counter

class solution:
    
    # This method can be used to calculate the Index of Coincidence
    # Notice: A text written in English language has an index of coincidence of 0.0667
    def IoC(self, text):
        text_length = 0
        
        # Count the number of times each letter appears
        letterCounts = Counter(text)

        # Canculate the sum of the probability of getting the same letter for each letter
        total = 0
        for ni in letterCounts.values():
            total += ni * (ni-1)
            
            # Count the length of the text in the meanwhile
            text_length += ni
        
        if text_length == 0:
            return 0
        else:
            return total / (text_length * (text_length-1))
    
    
    def getKey(self, ciphertext) -> str:
        # Please complete this method
        # It should be the return the key used to encrypt the plaintext.
        # GradeScope will import your class, and pass the test ciphertext to this method

        # master dict
        dictionary = {}

        # attempt L = 3, 4, 5, 6
        for i in [3, 4, 5, 6]:
            dictionary[i] = ciphertext[::i]

        # get IOC for each one
        max_IoC = -1
        maxx = None

        for i in [3, 4, 5, 6]:
            temp_IoC = self.IoC(dictionary[i])
            if(max_IoC > temp_IoC):
                continue
            else:
                max_IoC = temp_IoC
                maxx = i


        key_length = maxx
 
        result = "" 
        for i in range(key_length):
            current_group = ciphertext[i::key_length]
            counts = dict(Counter(current_group))
            letter_e_transpose = max(counts, key=counts.get)
            
            diff = ord(letter_e_transpose) - ord('e')
            if(diff < 0):
                diff = diff + 26 # loops back around
            # print(f"diff: {diff}")
            # print(f"chr: {chr(diff)}")            
            result = result + chr(int(diff) + 97) 
        
        return result

        

'''
Code Explanation:

First thing I do is try to find the code length. I do this by trying out the various possible key lengths (3, 4, 5, 6) 
and try to find the one that has the highest IoC. To do this, I basically get a string that contains the characters spaced
i spaces apart, then pass that text into the IoC function provided. Whichever length has the highest IoC is what I assume to 
be the correct Key length.

Now that we know the key length, we have key_length # of regular shifted ciphertexts. So I make strings that contain the characters
spaced key_length apart, and I find the most frequent character in each of those strings. I assume that character is the 'e' character in 
real English as the 'e' character is the most frequent character used. Then, I can find the difference between the ASCII values of the 
most frequent character in the string and 'e' and that (converted back to a character) is one of the characters in our key!

Do that for each of the strings and you have the key!

'''




        