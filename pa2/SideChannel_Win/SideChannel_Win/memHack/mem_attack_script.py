# -*- coding: utf-8 -*-
import subprocess

class solution:
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXITED PROPERTIES
        # You can add as many properties as you need
        self.mem_ctl_exe = "./mem_ctl.exe"                      # This is the path of mem_ctl.exe file
        self.pwd_checker_exe = "./mem_password_checker.exe"     # This is the path of password_checker.exe file
        self.password = ""                                      # This is where your guessed password is store
        
    def setProtectMem(self, start_index, end_index):
        # DO NOT MODIFY THIS METHOD
        
        # This method used to set a range of memory can not be accessed starting from start_index, ending with end_index (included).
        # After set [start_index, end_index] as can not be accessed, any read or write operations will
        # If this operation successfully executed, this method will return some output from the mem_ctl.exe
        # Otherwise, this method will return -1
        if(start_index <= end_index and start_index >= 0 and start_index < 1024 and end_index >=0 and end_index < 1024):
            p1 = subprocess.Popen([self.mem_ctl_exe, str(start_index), str(end_index)],stdout=subprocess.PIPE)
            mem_ctl_exe_result = p1.communicate()[0].decode()
            return mem_ctl_exe_result
        else:
            return -1

    def checkPassword(self, password):
        # DO NOT MODIFY THIS METHOD
        
        # This method will pass your password to mem_password_checker.exe to verify the correctness
        # The return value is a string which is the output of mem_password_checker.exe
        # If password is correct, this method will return Correct
        # If password is wrong, this method will return Wrong
        # If mem_password_checker accessed an can not be accessed memory, this method will return SEG ERROR
        
        p2 = subprocess.Popen([self.pwd_checker_exe, password], stdout=subprocess.PIPE)
        pwd_checker_exe_result = p2.communicate()[0].decode()
        return pwd_checker_exe_result
    
    def example(self):
        # The following shows how to call a executable file in python and capture its output
        # You can modify it to test your ideas
        

        mem_ctl_exe_result = self.setProtectMem(100,1000)
        # You can print the output for debug or test.
        print(mem_ctl_exe_result)

        # After mem_ctl.exe executed, the memory in range [start_index, end_index] will be set to can not be accessed.
        # That means, password_check.exe will not accessible this section of memory.
        # Any read or write from password_check.exe to this range will cause an "SEG ERROR"

    
        pwd_checker_exe_result = self.checkPassword("guess")
        # You can print the output for debug or test.
        print(pwd_checker_exe_result)


        # For password_checker.exe, the password you input will be stored from the beginning of the memory.
        # Take the above parameters as input, the memory structure is shown below:

        # index:        0--------------------100----------------------------------1000----------1023
        # access type:  |-----accessible------|---------cannot be accessed----------|--accessible--|
        # value:        guess\0#####################################################################

        print(self.password)
    
    def getPassword(self):

        self.password = ""
        for i in range(1, 1001):

            mem_ctl_exe_result = self.setProtectMem(i,1000)
            print(mem_ctl_exe_result)

            for i in range(33, 127):
                pwd_checker_exe_result = self.checkPassword(self.password + chr(i))
                if(pwd_checker_exe_result == "Correct"):
                    self.password += chr(i)
                    return self.password
                elif(pwd_checker_exe_result == "SEG ERROR"):
                    self.password += chr(i)
                    break


        # Please complete this method
        # It should be the return the correct password in a string
        # You should modify the start_index, end_index and password appropriately to achieve the attack
        # GradeScope will import your class, and call this method to get the password you calculated.


# Write Up
# Please explain your solution
"""
First thing I thought of is that the password is always stored at the beginning of the memory space.

Second thing I thought of is if you block out the buffer except for the very first spot, 
one of either three things will happen:
1. You can guess the 1 character right and you will get
    a. "SEG FAULT" output if the password is LONGER than 1 character.
    b. "Correct" if the password is 1 character long.
2. "Wrong" if you guess the wrong character. 

Knowing these facts, you can iteratively solve the for the password just by looking at the output of the 
password checker. 

I start off with only 1 spot open (the rest of the 999 spots are protected).
I then check all possible ASCII characters (33-127) and check with the password checker to see what output I get.
If I get "Correct", this means that the password was this exact length and I'm done! I add my character to my guess and return.
If I get "SEG FAULT", this means that the character I chose was right for this index! BUT the password has more characters after this. Therefore, 
I add my character to my guess and repeat this process.
If I get "Wrong", I got the character wrong, and I go onto the next ASCII character.

I keep doing this until I eventually get "Correct", meaning that the character I chose matched AND the password was the correct length!
"""