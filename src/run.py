

from scrapy.crawler import CrawlerProcess
from prettytable import PrettyTable
import getpass
import sys

import main

#init the spider instance
scanner=main.Spider()



main.Spider.user=input("What is your K number ?")
#get K number
main.Spider.passw=getpass.getpass()
#get password



#get crweler to work
process = CrawlerProcess()
process.crawl(scanner)
process.start()




# uncommont the following code to use the orginal output
# Please only use the original output when prettyTable package is unavailable
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print("Course List")
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# for i in scanner.getCourse():
#     print("\b"+"\b"+ i )
#     print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
#
# print()
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print("Course List")
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# for i in range(0,len(scanner.getGradeTitle())):
#     print("\b"+"\b"+ scanner.getGradeTitle()[i]+"\b"+"\b"+scanner.getGradeMarks()[i])
#     print("|++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
#
# print()
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



def printCourseTable():
    course_table = PrettyTable(["No.", "Courses"])
    for i in range(0, len(scanner.getCourse())):
        course_table.add_row([i, scanner.getCourse()[i]])

    print(course_table)
    pass



def printGradeTable():
    course_table = PrettyTable(["Course", "Grade"])
    for i in range(0, len(scanner.getCourse())):
        course_table.add_row([scanner.getGradeTitle()[i], scanner.getGradeMarks()[i]])

    print(course_table)
    pass


print("The Course you are doing ")
printCourseTable()
print("\n")
print("and Your Grade")
printGradeTable()








