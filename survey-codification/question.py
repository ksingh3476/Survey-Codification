class Question:

    def __init__(self, q, m, t):
        self.question = q
        self.answers = []
        self.metric = m
        self.type = t
    
    def get_question(self):
        return self.question
    
    def get_answers(self):
        return self.answers
    
    def get_metric(self):
        return self.metric
    
    def get_type(self):
        return self.type
    
    def set_question(self, q):
        self.question = q
    
    def set_answers(self, a):
        self.answers = a
    
    def set_metric(self, m):
        self.metric = m
    
    def set_type(self, t):
        self.type = t
    
    def __str__(self):
        pass