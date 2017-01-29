# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.



def check_MD5(doorID, int):
    import hashlib
    hash = doorID + str(int)
    md5 = hashlib.md5(hash.encode('utf-8')).hexdigest()
    if (md5[0:5] == "00000"):
        return md5[5]
    return ""

def main():
    print("Hello World")
    doorID = "reyedfim"
    password = ""
    i = 0
    
    
    while len(password) < 8:
        password += check_MD5(doorID, i)
        i += 1
        print (password)
        
        
        
if __name__ == "__main__":
    main()