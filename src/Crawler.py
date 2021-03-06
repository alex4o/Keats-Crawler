import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor

from loginform import fill_login_form


class Spider(scrapy.Spider):
    name = 'login'

    # init url to crawl
    start_urls = ['https://login-keats.kcl.ac.uk/']


    # login infomration
    user = ""
    passw = ""


    #List for store info
    course_list = []
    grade_title_list = []
    grade_marks_list = []


    def parse(self, response):

        args, url, method = fill_login_form(response.url, response.body, self.user, self.passw)

        return scrapy.FormRequest(url, method=method, formdata=args, callback=self.after_login)



    ''' 
    this function will run as the callback of the login request, once the logging in process
    is finished, this function will be called to crawl and fetch the inforamtion about the course.
    after the course information is fetched, then another page which is the grade page will be crawled
    too
    
    '''
    def after_login(self, response):

        for tab in response.css('div[id*="course"]'):
            PATH = '.title a::text'

            self.course_list.append(tab.css(PATH).extract_first())

        return scrapy.Request("https://keats.kcl.ac.uk/grade/report/overview/index.php",
                              callback=self.parse_grade_page)



    '''
    This is function being used on fetching information of the grade
    it is also the callback function of the scrapy request from the previous function 
    
    '''

    def parse_grade_page(self, response):
        for tab2 in response.css('tr[id*="grade-report-overview"]'):
            PATH_2 = 'a::text'
            PATH_3 = 'td[id*="grade-report-overview"]::text'

            self.grade_title_list.append(tab2.css(PATH_2).extract_first())
            self.grade_marks_list.append(tab2.css(PATH_3).extract_first())


        # DEBUG
        # self.showThings()



    def getCourse(self):
        return self.course_list

    def getGradeTitle(self):
        return self.grade_title_list

    def getGradeMarks(self):
        return self.grade_marks_list


    # DEBUG
    # def getAc(self):
    #     return self.user, self.passw


    # DEBUG
    # def showThings(self):
    #
    #     print(self.grade_title_list)
    #     print(self.grade_marks_list)







    
