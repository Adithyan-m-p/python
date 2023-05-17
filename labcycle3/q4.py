import numpy as np
import pandas as pd
import pickle
import keyboard

class vehicle : 
   def __init__(self):
       self.engine_number=(input("enter the engine number of vehicle : "))
       self.model=input("enter the model of the vehicle : ")
       self.type=input("enter the  type of the vehicle : ")
       self.mileage=float(input("enter  the mileage of vehicle : "))
       self.vendor=input("enter vendor of the vehicle : ")
       self.register_number=input("enter the register number of the vehicle : ")
       self.owner_name=input("enter the name of the owner : ")
        
   def return_(self):
        return self.engine_number,self.model,self.type,self.mileage,self.vendor,self.register_number,self.owner_name
        
        
       
       
       
class details(vehicle):
    def __init__(self):
        list_=[]
        self.data=pd.DataFrame(list_,columns=["engine number","model","type","mileage","vendor","register number","owner name"])

        
    def add(self):
        detail=vehicle()
        self.data.loc[len(self.data.index)]=detail.return_()
        self.data=self.data.sort_values(by=["mileage"])
        print("\n succesfully added")
        self.store()
    
    
    def display(self):
        
        print(self.data)
        
        
    def modify(self):
        run=True
        while run==True:
            print("1.to modify engine number")
            print("2.to modify model")
            print("3.to modify type")
            print("4.to modify mileage")
            print("5.to modify vendor")
            print("6.to modify register number")
            print("7.to modify owner name")
            print("8.quit")
            
            user=int(input("what is your option"))
            if user==9:
                print("invalid")
            while(user!=9):
                if user==1:
                    self.data["engine number"].mask(self.data["engine number"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==2:
                    self.data["model"].mask(self.data["model"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==3:
                    self.data["type"].mask(self.data["type"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==4:
                    self.data["mileage"].mask(self.data["mileage"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==5:
                    self.data["vendor"].mask(self.data["vendor"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==6:
                    self.data["register number"].mask(self.data["register number"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==7:
                    self.data["owner name"].mask(self.data["owner name"]==input("enter the incorrect value"),input("enter value to update"),inplace=True)
                    print(" \n succesfully modified")
                    break
                elif user==8:
                    run=False
                    self.store()
                    break
                else:
                    print("invalid")
                    break
                
    def delete(self):
        self.data=self.data.set_index("register number")
        delete_data=input("enter the register number to delete the data")
        self.data=self.data.drop(delete_data)
        self.data=self.data.reset_index()
        print("deleted succesfully")
        self.store()
        
        
        
    def store(self):
        with open("q4","wb") as file:
            pickle.dump(self.data,file)
        
    def load(self):
        with open("q4","rb") as file:
            self.data=pickle.load(file)
        
    
    
def main():
    data = details()
    print("Welcome, press Enter to continue...")
    while True:
        if keyboard.is_pressed("enter"):
            data.load()
            print("\n1. Add value")
            print("2. Delete value")
            print("3. Modify value")
            print("4. Display data")
            print("5. Quit")
            user_choice = int(input("\nChoose any option: "))
            
            if user_choice == 1:
                data.add()
            elif user_choice == 2:
                data.delete()
            elif user_choice == 3:
                data.modify()
            elif user_choice == 4:
                data.display()
            elif user_choice == 5:
                print("Quitting program...")
                break
            else:
                print("Invalid option, please try again.")

            
        
main()
        
        


   
    
    
    
    