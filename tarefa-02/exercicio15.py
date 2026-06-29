print("Ganho de antena Yagi")  
print("-" * 40)  
print("Elementos | Ganho (dBi)")  
print("-" * 40)  

for n in range(2, 21):  
    G = 10 * (n ** 0.8)  
    print(f"{n:9d} | {G:11.2f}") 

print("-" * 40)  
print("Quanto mais elementos, maior o ganho!")
