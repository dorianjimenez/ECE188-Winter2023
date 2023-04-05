import urllib.parse
from pymd5 import md5, padding

class solution:
    def getNewURL(self, url) -> str:
        # # Please complete this method
        # It should be the return the new url, ending with &command3=releaseAccess
        # GradeScope will import your class, and pass the test URL to this method

        password_length = 8
        initial_pos_of_token = url.find("token=") + 6
        hash = url[initial_pos_of_token:(initial_pos_of_token + 32)]

        initial_pos_of_user = url.find("user=")
        message_length = len(url) - initial_pos_of_user + password_length

        attack_message = "&command3=releaseAccess"

        bits = (message_length + len(padding(message_length * 8))) * 8
        
        new_padding = str(padding(message_length * 8))
        new_padding = new_padding[2:len(new_padding) - 1]
        new_padding = new_padding.replace("\\x", "%")
        new_padding = new_padding.replace("a", "A")
        new_padding = new_padding.replace("b", "B")
        new_padding = new_padding.replace("c", "C")

        h = md5(state=bytes.fromhex(hash), count= bits)
        h.update(attack_message)

        return url[:initial_pos_of_token] + h.hexdigest() + url[initial_pos_of_user-1:] + new_padding + attack_message




'''
Code Explanation:

The first thing I did was I parsed the URL to find the original hash. I also then parsed the URL to the part that makes up the hash
(besides the password), which is the latter half of the URL past "user=...". Then I found out the original length of the message that was
hashed by adding 8 (password length) + the rest of the URL.

I then found the bits using the formula provided in the spec, as well as the new_padding we put in the URL. I had to do some string 
modifications because I was getting some issues with capitalization, but overall it was OK. I then calculated the new MD5 hash with the 
attack message, and pieced together the new URL. 
'''