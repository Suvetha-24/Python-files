class student:
    dept="ECE"
    def self_dim(self,name,marks):
        self.name=name
        self.marks=marks
        
    def per(self):
        self.p=sum(self.marks)//3
    def display(self):
        self.per()
        print("1.Name:",self.name)
        print("2.Score:",self.p)
        print("3.Dept",student.dept)
    
Suvetha=student()
Nivetha=student()
Suvetha.self_dim("Suvetha",[20,30,50])
Nivetha.self_dim("Nivetha",[30,40,50])

Suvetha.display()
Nivetha.display()
