
#this is the code which will tell us which frameit will be 
filename == aase
               
if filename == 'requirements.txt':
               file_path = os.path.join(dirpath, filename)
               with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                         # if content == "fastapi" or "django":
                    if "fastapi" in content or "django" in content:
                         print("fastapi it is")


# our code will first get the percentage , accordig to our code we are now getting the percentage and all
               # now we want an function which will choose highest percetage language , and look for its dependancies , untill all the files completed
               # now we have dependencies , but now we have to read it and predict that which framework will be there 

               #highest percentage language , iteration
               #language found then from signature json we have to look at ---> dependacy files,
               #inside dependacy find frameworks , for safer side we have to look into the code files , and it can be related to , 
               # dependacy keyword from json

          