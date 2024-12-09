#7 Coffee customization:
size = str(input("Enter a coffee's size:")).lower()
extra_shot = True

if extra_shot == True:
    order = size + " Coffee with extra shot"
else:
    order = size + " Coffee without extra shot"
       
print(order)     