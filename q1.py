import hashlib

#hashlib.sha256(word.encode("ascii", "ignore")).hexdigest()

find = '69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7'

path = '/Users/camilailigaray/Library/CloudStorage/OneDrive-FloridaInternationalUniversity/Blockchain_CIS4731/Assignment_1/words.txt'

with open (path,'r') as  opened_file:
    words = opened_file.read()
    for word in words:
        
        if hashlib.sha256(word.encode("ascii","ignore")).hexdigest() == find:
            print(word)

# print(words)
