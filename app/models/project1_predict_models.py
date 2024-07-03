from app.core.config import settings
from app.utils.get_model import get_model

class Project1PredictModels:
    def __init__(self):
        self.model1 = get_model(settings.PROJECT1_MODEL1_PATH)
        self.model2 = get_model(settings.PROJECT1_MODEL2_PATH)
        self.model3 = get_model(settings.PROJECT1_MODEL3_PATH)
        self.model4 = get_model(settings.PROJECT1_MODEL4_PATH)
        self.model5 = get_model(settings.PROJECT1_MODEL5_PATH)
        self.model6 = get_model(settings.PROJECT1_MODEL6_PATH)

    def predicts(self, input_data):
        prediction1 = self.model1.predict(input_data).tolist()
        prediction2 = self.model2.predict(input_data).tolist()
        prediction3 = self.model3.predict(input_data).tolist()
        prediction4 = self.model4.predict(input_data).tolist()
        prediction5 = self.model5.predict(input_data).tolist()
        prediction6 = self.model6.predict(input_data).tolist()
        
        return {
            "1": prediction1, 
            "2": prediction2, 
            "3": prediction3, 
            "4": prediction4, 
            "5": prediction5, 
            "6": prediction6
        }
        

predictModels = Project1PredictModels()