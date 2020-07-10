class Lambdastudents: 
    def __init__(self, name, age, cohort_number, previous_job):
        self.name = name 
        self.age = age 
        self.cohort_number = cohort_number
        self.previous_job = previous_job
    
    def code(self):
        return print('Yes, I can code.')

class DataSci(Lambdastudents):
    def __init__(self, previous_job, name, age, cohort_number):
        super().__init__(name, age, cohort_number, previous_job)

    def make_prediction(self):
        return print("The weather for today is cloudy.")
    
    def code(self):
        return print('Yes, I can code: Python and do DS')