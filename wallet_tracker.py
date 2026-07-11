class Monthly:
        def details(self):
            print("***Wallet Tracker***")
            self.name=input("Enter your name: ")
            while True:
                    income=input("Enter your monthly income: ")
                    if income.isdigit()==True:
                            self.income=int(income)
                            if self.income>0:
                                    break
                    else:
                            print("Invalid input! Enter integer based income")
            self.cost=0
            while True:
                    child=input("Do you have children?(Type 'yes' or 'no')  ").lower().strip()
                    if child=="yes":
                            while True:
                                    cost=input("Enter your children's overall monthly education cost: ")
                                    if cost.isdigit()==True:
                                            self.cost=int(cost)
                                            if self.cost>0:
                                                    break
                                    else:
                                            print("Invalid input!")
                            break
                    elif child=="no":
                            break
                    else:
                            print("Invalid input!Type 'yes' or 'no'.")
            while True:
                    groceries=input("Enter overall monthly groceries cost: ")
                    if groceries.isdigit()==True:
                            self.groceries=int(groceries)
                            if self.groceries>=0:
                                    break
                    else:
                            print("Invalid Input!")
            while True:
                  elec_water=input("Enter total electricity and water bill: ")
                  if elec_water.isdigit()==True:
                            self.elec_water=int(elec_water)
                            if self.elec_water>0:
                                    break
                            else:
                                    print("only positive input allowed")
                  else:
                            print("Invalid Input")
                    
            self.vech=0
            self.cost_off=0
            self.trans=0
            while True:
                wfh=input("Do you work from home?(Type 'yes' or 'no') ").lower().strip()
                if wfh=="no":
                    while True:
                        vechiles=input("Do you have personal vehicles?(Type 'yes' or 'no') ").lower().strip()
                        if vechiles=="yes":
                                while True:
                                        vech=input("Enter your overall vehicle maintenance: ")
                                        if vech.isdigit()==True:
                                                self.vech=int(vech)
                                                if self.vech>0:
                                                        break
                                                else:
                                                        print("Invalid input")
                                        else:
                                                print("Invalid Input")
                                break
                                                
                            
                        elif vechiles=="no":
                                while True:
                                        trans=input("Enter your overall transportation cost: ")
                                        if trans.isdigit()==True:
                                                self.trans=int(trans)
                                                if self.trans>0:
                                                        break
                                                else:
                                                        print("Cost cant be negative")
                                        else:
                                                print("Enter digits only")
                                break
                            
                        else:
                            print("Invalid input!Type 'yes' or 'no'.")
                    break
                elif wfh=="yes":
                        while True:
                                cost_off=input("Enter cost of internet and office supplies: ")
                                if cost_off.isdigit()==True:
                                        self.cost_off=int(cost_off)
                                        if self.cost_off>0:
                                                break
                                        else:
                                                print("Enter positive input")
                                else:
                                        print("Enter only integer inputs")
                        break
                else:
                    print("Invalid input!Type 'yes' or 'no'.")
            while True:
                    medical=input("How much money do you spend on healthcare and medicines? ")
                    if medical.isdigit()==True:
                            self.medical=int(medical)
                            if self.medical>0:
                                    break
                            else:
                                    print("Enter positive number")
                    
            while True:
                    shopping_ent=input("Expenses for shopping and entertainment: ")
                    if shopping_ent.isdigit()==True:
                            self.shopping_ent=int(shopping_ent)
                            if self.shopping_ent>0:
                                    break
                            else:
                                    print("Enter positive number")
                                    
            self.emi=0
            while True:
                yn=input("Do you pay any EMI?Type 'yes' or 'no'. ").lower().strip()
                if yn=="no":
                    break
                elif yn=="yes":
                    while True:
                            emi=input("Input your monthly EMI: ")
                            if emi.isdigit()==True:
                                    self.emi=int(emi)
                                    if self.emi>0:
                                            break
                                    else:
                                            print("Enter positive number")
                    break
                else:
                    print("Invalid input!Type 'yes' or 'no'.")
        def calculate(self):
            self.needs=self.income//2
            self.wants=3*self.income//10
            self.savings=self.income//5
            self.needs1=self.cost+self.groceries+self.elec_water+self.medical+self.cost_off+self.vech+self.trans
            self.wants1=self.shopping_ent
            self.savings1=self.income-(self.needs1+self.wants1+self.emi)
        def final(self):
            print("---Monthly Report---")
            print("Essentials: ",self.needs1)
            print("Wants: ",self.wants1)
            print("Savings: ",self.savings1)
            with open("project_output.txt","w") as file:
               file.write(f"Name: {self.name}\n")
               file.write(f"Monthly Income: {self.income}\n")
               file.write(f"Essentials: {self.needs1}\n")
               file.write(f"Wants: {self.wants1}\n")
               file.write(f"Savings: {self.savings1}\n")
        def advice(self):
                message=["---ADVICE---"]
                if self.savings1<self.savings:
                    if (self.needs1>self.needs):
                            if self.groceries>12*self.income//100:
                                    message.append(f"ALERT!You have crossed your groceries budget")
                            if self.elec_water>6*self.income//100:
                                    message.append(f"ALERT!You have crossed your Electric bill & water budget")
                            if self.trans>self.income//10:
                                    message.append(f"ALERT!You have crossed your monthly transportation budget")
                            if self.vech>6*self.income//100:
                                    message.append(f"ALERT!You have crossed your monthly vehicle maintenance budget")
                            if self.medical>8*self.income//100:
                                    message.append(f"ALERT! You have crossed your healthcare budget")
                            if self.cost>12*self.income//100:
                                    message.append(f"ALERT! You have crossed your children's education budget")

                    if (self.wants1>self.wants):
                            message.append(f"ALERT! You have crossed your shopping budget")
                    if self.emi>self.income//4:
                            message.append(f"ALERT! Your EMI has crossed your monthly budget plan")  
                else:
                        message.append(f"Since you are saving atleast 20% of your monthly income. It is fine")
                        message.append(f"Remainder, your essentials are already {self.needs1*100//self.needs} % of your essentails budget")
                        message.append(f"Remainder, your wants and desires are already {self.wants1*100//self.wants} % of your wants budget")
                for mssg in message:
                        print(mssg+'\n')
                with open("project_output.txt","a") as file:
                        for mssg in message:
                                file.write(mssg+'\n')
obj=Monthly()
obj.details()
obj.calculate()
obj.final()
obj.advice()
                

    
