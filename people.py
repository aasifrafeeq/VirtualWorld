# this maintaince the basic info about people
class people:
    def __init__(self, firstName,surname):
        self.firstName = firstName
        self.surname = surname
        self.fullname = firstName+" "+surname
        self.age = 0
        # initally apersons health will be at 100% as he gets older and catches diseases his health decreases
        self.health = 100
        self.diseases = []

    # increases age each year
    # as for how long a year in this program is you can define your own time period
    def age_inc(self):
        self.age += 1

    def catch_disease(self, disease):
        self.diseases.append(disease)
        self.health -= disease.damage

    def damage_from_disease(self, disease):
        self.health -= disease.damage

    def heal_disease(self, disease):
        self.diseases.remove(disease)
        # when the person heals only 90%of health is regained we  may change that for higher diseases
        self.health += (90 * disease.damage) / 100

    def have_child(self):
        #code here to spawn new child
# create a new person with name and last name as parent