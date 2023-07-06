2





#Billing Software
class AGB :#Auto_Generate_Bill:
    name = input("Enter customer name : ")
    print(50 * " " ,name, ":-->PSP Restaurant Welcomes You")
    price = 0
    #price_list =[]
    total_price = 0
    item_list =[]
    quant_list =[]
    p_list =[]
    final_amount =0
   # count = 0
    def __init__(self):
        self.avil_items =""" 

        ----------------------------------------------------------------------------------------------------------------------------------------------
                                            Veg & Non_veg : Items--->Price_list For One Plate
        ----------------------------------------------------------------------------------------------------------------------------------------------
        ______________________________________________________________________________________________________________________________________________                
                Soups                |        Starters               |       Main Course                |     Rotis& Breads     |   Drinks
        ______________________________________________________________________________________________________________________________________________
        creamymushroomsoup(CR)= 60   |Chilli Paneer(CP)        = 200 | Paneer Biryani(PB)         = 220 | Roti(R)         = 30  | Cola(Co)        = 40
        VegSweetCorn(VSC)     = 60   |chicken_drum_sticks(CDS) = 250 | Mushroom Biryani(MB)       = 200 | Rumali Roti(RR) = 40  | Thumbsup(TH)    = 40
        Tomato Soup(TS)       = 50   |chicken_kebab(CK)        = 120 | Chicken DumBiryani(CDB)    = 120 | Butter roti(BR) = 50  | sprit(S)        = 40
        MushRoom Soup(MS)     = 70   |chilli_chicken(CC)       = 180 | ChickenFrypieceBiryani(CF) = 120 | Butter Naan(BN) = 40  | VirginMojito(VM)= 70
        Manchow Soup(MCS)     = 80   |Dragon_chicken(DC)       = 200 | Boneless chickenBiryani(BC)= 200 | Naan(N)         = 40  | Blue carco(BC)  = 70
        Creamy soup(CS)       = 60   |chicken_65(C65)          = 120 | Mutton kheema Biryani(MKB) = 250 | Kulcha(k)       = 50  | WaterBottle(WB) = 20
        Mutton_bonesoup(MBs)  = 90   |chicken_lollypop(CL)     = 150 | Mutton Biryani(MUB)        = 300 | ButterKulcha(BK)= 50
        Chickencornsoup(CSC)  = 90   |chicken555(CT5)          = 200 | Fish Biryani(FB)           = 250 | Aloo kulcha(AK) = 50
        Hot'n'sour soup(HS)   = 90   |chicken_majestics(CMA)   = 230 | Prawn Biryani(PRB)         = 250 | Chapathi(C)     = 30
        ChickenManchowsoup(CM)= 90   |chiken_tandoori(CT)      = 200 | MLA Biryani(MLA)           = 300 | Pulka(P)        = 20
        ______________________________________________________________________________________________________________________________________________

        """
        print(self.avil_items)
    
    def cal_bill(self):
        self.dict_items ={'CR':60 , 'VSC':60 ,'TS':50 ,'MS':70 ,'MCS':80 ,'CS':60,'MBS':90, 'CSC':90, 'HS':90, 'CM':90, 'CP':200,'CDS':250,'CK':120 ,'CC':180,
                          'DC':200, 'C65':120, 'CL':150, 'CT5':200 ,'CMA':230 ,'CT':200,'PB':220 ,'MB':200,'CDB':120,'CF':120, 'BC':200,'MKB':250 ,'MUB':300 ,
                          'FB':250,'PRB':250 ,'MLA':300 ,'R':30 ,'RR':40 ,'BR':50, 'BN':40 ,'N':40 ,'K':50,'BK':50 ,'AK':50 ,'C':30 ,'P':20,'CO':40 ,'TH':40,
                          'S':40,'VM':70 ,'BC':70 ,'WB':20}
        n= len(self.dict_items)
        self.food = input("You want take this items by Take Away / Dine-In  : ")

        for i in range(n):
            ip1 = input("please confirm you want take items from our resturant yes-->Y or No-->N :")
            #if ip1 == "Y":
              #  AGB.count += 1
                    
            if ip1 =="N":
                break
            if ip1 == "Y":
                print("select items from menu list and enter item codes below")
                self.item = input("Enter item code : ")
                print("plese select quantity as 1,2,3,.. (ex: plate of meal)")
                self.quantity = int(input("enter quantity  : "))
                if self.item in self.dict_items.keys():
                    AGB.price = self.quantity * (self.dict_items[self.item])
                    #AGB.price_list.append((self.item ,self.quantity , AGB.price))
                    AGB.item_list.append(self.item)
                    AGB.p_list.append(self.price)
                    AGB.quant_list.append(self.quantity)
                    AGB.total_price = AGB.total_price + AGB.price
                    self.gst = AGB.total_price * (0.18)
                    AGB.final_amount = AGB.total_price + self.gst
                else:
                    print("YOUR ENTERD ITEM IS NOT AVAILBLE")
            else:
                print("YOUR ENTERD WRONG ITEM/CODE")

    def billing(self):
        check = input("your want to billing the items press.. Yes -->Y / No -->N: ")
        
        if check == "Y" :
            print(100 *"-")
            print(45 * " " ,"PSP Restaurant ")
            print(35 *" " , "VISAKHAPATNAM - MADDILAPALEM BRANCH")
            print(45 *" ", "Ph-No - 9550019755 ")
            print(100 * "-")
            print(50 * " " ,self.food)
            print(100 * "-")
            print(3 *" " ,"S.No",20 *" ","Items" , 20*" ", "Quantity" , 20*" ", "Total Price")
            #print(len(AGB.price_list))
            #print(AGB.p_list)
            #print(AGB.quant_list)
            #print(AGB.item_list)
            #print("count " , AGB.count)
            self.x= len(AGB.p_list)

            for i in range(self.x):
                print(5 * " " ,i+1, 22 * " ",AGB.item_list[i],24*" ",AGB.quant_list[i],26 * " " ,AGB.p_list[i])
            print(100 *"-")
            print(f'{45* " "}No.of items = {sum(AGB.quant_list)} {15 * " "}Total_price {sum(AGB.p_list)}')
            print(f'{76 * " "} GST = {self.gst}')
            print(100 * "=")
            print(f' {10 * " "}{AGB.name} Please pay this amount ---> Rupees {AGB.final_amount} /-only ')
            print(100 * "=")
            print(50 *" " ,"Thank You")
            print(45 * " " ,"Please Visit Again")
                       
        


   
    #print(price_list)
  
obj = AGB()
obj.cal_bill()
obj.billing()

