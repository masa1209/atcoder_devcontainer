import glob
import os

print("target_dir")
current_dir = input()

dir_list = glob.glob(current_dir + "/*")

item_list = ["a","b","c","d","e","f","g","e","h","i","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ex"]

for i in dir_list:
    target_dir = i.split("/")[-1]
    print(type(target_dir))
    if target_dir in item_list:
        f = open(i+"/main.py", 'w')
        f.write('')
        f.close()
        