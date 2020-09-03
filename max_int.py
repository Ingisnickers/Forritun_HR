# Forritið byður notanda um að slá inn tölu
# Forritið sannreynir að talan sé ekki mínus tala
# Forritið heldur utan um stærstu töluna sem notandi hefur slegið inn
# Ef notandi slær inn tölu minni en 0 (mínus tölu) prentar forritið
# stærstu töluna sem notandi hafði slegið inn

num_int = int(input("Input a number: "))    
max_int = 0                             # Breyta til að geyma stærstu innslegnu 
                                        # töluna                                

while num_int >= 0:                     # Lykkjan heldur áfram svo lengi sem notandi slær ekki inn mínus tölu 
    while num_int > max_int:           
        max_int = num_int
    num_int = int(input("Input a number: ")) 

print("The maximum is", max_int)