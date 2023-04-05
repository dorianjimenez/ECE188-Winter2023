# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password

class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
    
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)
        
        
    
    def getPassword(self):
        self.password = ""
        while(len(self.password) < 11):
            

            max = (-1, 0)
            for i in range(33, 127):
                # print(self.password)
                
                if(check_password(self.password + chr(i)) == "Correct"):
                    self.password += chr(i)
                    return self.password
                else:
                    total_time = 0

                    # check 6 times
                    for j in range(6):
                        T1 = time.perf_counter()
                        result = check_password(self.password + chr(i))
                        T2 = time.perf_counter()
                        total_time += T2 - T1
                    

                    if(total_time > max[1]):
                        max = (i, total_time)
                    
                    # print(chr(i), total_time)
            
            # print(max[0])
            self.password += chr(max[0])

        return self.password
        
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        

    
# Write Up
# Please explain your solution
"""
The main idea is that if you guess a right character, it will take the password checker longer since more memory lines need to be accessed. 

Using this knowledge, I knew that I could guess the password letter by letter. If the letter took a short time, then it is the wrong guess.
If the letter took a long time, then it is the right guess and we will add it to our password and then repeat until we have the full correct password.

So, for each letter in the password, I guessed a random ASCII character (33-127) and timed. I did each trial 6 times and just took the total time (no 
need to divide by 6 as the math is still the same either way). I had a maximum tracker variable that tracked the ASCII character that took the longest.
After testing each ASCII character, I then added the ASCII character that took the longest to the password. 

Repeat until we eventually get "Correct" from the password checker. This means we have the full correct password, so no need for more checking!
"""