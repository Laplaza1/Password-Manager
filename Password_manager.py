from random import *




img = "TheBIBBLE_Test1.png"
def image_pass_encode(image:str,password:str):
    with open(image,"rb") as photo:
        data = photo.read()
        print(data)
        photos = open(image,"ab")


        offset = data.index(bytes.fromhex('426082'))
        photo.seek(offset+2)
        print(photo.seek(offset+2))
        photos.write(password.encode())
        print(photo.seek(offset+2))


def clear_old_pass(image:str):
    with open(image,"rb+") as photo:
        data = photo.read()
        print(photo)
        offset =  data.index(bytes.fromhex('426082'))
        photo.seek(offset+2)
        print(photo.seek(offset+2))
        offset =  data.index(bytes.fromhex('426082'))
        photo.seek(offset+2)
        photo.truncate()

    



def Password_generator():
    special_char = ["?", "!" ,"@" ,"#" ,"$" ,"%" ,"&"]
    with open("Random speech.txt","r") as file1:
        test_word = file1.read()
        test_word= test_word.replace(",","").split()
        pass_word_frag=(test_word[randint(a=0,b=282)])
        pass_word_frag2 =(test_word[randint(a=0,b=282)])
        if randint(1,2) == 1:
            pass_word = pass_word_frag+pass_word_frag2
        else:
            pass_word= pass_word_frag2+pass_word_frag
    pass_num_frag =str(randint(a=121,b=100069))
    special_char_frag = ""
    for i in range(1,randint(1,5)):
        special_char_frag += (special_char[(randint(a=0,b=(len(special_char)-1)))])
    password =(pass_word+pass_num_frag+special_char_frag)
    return password



    
        
