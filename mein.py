from school import School
from classroom import Classroom
from person import Student,Teacher
from subject import Subject


school=School('SPI',"Sylhet")

eight=Classroom('Eight')
nine=Classroom('Nine')
ten=Classroom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#adding stuydent
tanin=Student('Tanim',eight)
sanim=Student('Sanim',nine)
fahim=Student('fahim',nine)
hamim=Student('hamim',ten)

school.student_admission(tanin)
school.student_admission(sanim)
school.student_admission(fahim)
school.student_admission(hamim)

#adding teacher
abul=Teacher('Abul')
babul=Teacher('babul')
kabul=Teacher('kabul')


#adding sub
eng=Subject('English',abul)
bang=Subject('Bangla',babul)
math=Subject('Math Metice',kabul)
phy=Subject('physics',kabul)


eight.add_subject(bang)
eight.add_subject(math)
eight.add_subject(eng)
nine.add_subject(phy)
nine.add_subject(math)
nine.add_subject(bang)
ten.add_subject(bang)
ten.add_subject(math)
ten.add_subject(phy)

eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()
print(school)