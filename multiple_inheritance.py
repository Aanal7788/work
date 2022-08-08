class Idea:
    def idea_display(self):
        print("welcome to Idea")

class Vodafone:
    def vodafone(self):
        print("welcome to Vodafone")

class VI(Idea,Vodafone):
    def display(self):
        self.idea_display()
        self.vodafone()
        print("welcome to VI")

vi=VI()
VI.display()
