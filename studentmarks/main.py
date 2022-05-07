sub1 = int(input('maths subject marks : '))
sub2 = int(input('social subject marks : '))
sub3 = int(input('science marks : '))
sub4 = int(input('enter the hindi marks : '))
sub5 = int(input('economics marks : '))
sub6 = int(input('enter physics marks : '))
final = sub1,sub2,sub3,sub4,sub5,sub6

class vn2_school:

    def student_report(self,maths,social,science,hindi,economics,physics):
        average = (maths + social + science + hindi + economics + physics)/6
        print(average)
        c=0
        c1=0
        if average >=75 and average <90:
            print('Average')
        elif average >=90:
            for x in final:
                if x>=95:
                    c+=1
            if c>=3:
                print('gold')
            else:
                print('Good')

        elif average >=65 and average <75:
            for x in final:
                if x <= 60:
                    c1 += 1
            if c1 >= 3:
                print('Fail')
            else:
                print('Give a chance')
        else:
            print('Fail')

v = vn2_school()
v.student_report(sub1,sub2,sub3,sub4,sub5,sub6)