class Student:

    def __init__(self, StudentId, FirstName, LastName, Major,GPA,FacultyAdvisor,IsDeleted):
        self.StudentId = StudentId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Major = Major
        self.GPA = GPA
        self.FacultyAdvisor = FacultyAdvisor
        self.IsDeleted = IsDeleted

    def getStudentId(self):
        return self.StudentId

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getMajor(self):
        return self.Major

    def getGPA(self):
        return self.GPA

    def getFacultyAdvisor(self):
        return self.FacultyAdvisor

    def getIsDeleted(self):
        return self.IsDeleted

### returns tuple of student

    def getStudent(self):
        return (self.getStudentId(),self.getFirstName(),self.getLastName(),self.getMajor(),self.getGPA(),self.getFacultyAdvisor(),self.getIsDeleted())



