#dictionary for disease that can catch (to define how much health decrease with eah disease)
diseases={"fever":2}
#this maintaince the basic info about people
class people:
    def __init__(self,name):
        self.name=name
        self.age=0
        #initally apersons health will be at 100% as he gets older and catches diseases his health decreases
        self.health=100
        self.disease=[]



    #increases age each year 
    #as for how long a year in this program is you can define your own time period 
    def age_inc(self):
        self.age+=1

    def catch_disease(self,disease):
        self.disease.append(disease)
        self.health -= diseases[disease]
    
    def heal_disease(self,disease):
        self.disease.remove(disease)
        #when the person heals only 90%of health is regained we  may change that for higher diseases
        self.health+= (90 *diseases[disease] )/100

    def have_child():
        # create a new person with name and last name as parent

