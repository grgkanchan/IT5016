class Whitecliffe():
    def __init__(self,studentid, lname,program):
        self.studentid = studentid
        self.lname = lname
        self.program = program
        self.membershipid = 400001
    def member(self):
        self.membershipid+=1
        return self.membershipid

    def display(self):
        print(f"Student ID : {self.studentid} \n Last Name : {self.lname} \n Student Program : {self.program} \n Membership ID : {self.membershipid}")

info = Whitecliffe(20240699,"Kanchan","Bachelor")
info.member()
info.display()