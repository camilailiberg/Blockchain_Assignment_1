import hashlib

def q1():
    find = '69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7'

    path = '/Users/camilailigaray/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Blockchain_CIS4731/Assignment_1/words.txt'

    with open ("words.txt",'r') as  opened_file:
        # words = opened_file.read()
        for word in opened_file:
            
            if hashlib.sha256(word.strip().encode("ascii")).hexdigest() == find:
                print(word)

if __name__ == "__main__":
    q1()


