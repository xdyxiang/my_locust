from locust import Locust, TaskSet, task, between,events
import time
from locust import web

from websrc.main import main


web.app.register_blueprint(main,url_prefix='/page')



class UserBehavior(TaskSet):
    def setup(self):
        print(" TaskSet setup*****************************")
    def teardown(self):
        print(" TaskSet teardown*****************************")
    # 每个用户都会执行
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        print("login1--------")

    def logout(self):
        print("logout1---------")

    @task(20)
    def index1(self):
        start_time = time.time()
        print("doing something++++++++++")
        total_time = int((time.time() - start_time) * 1000)
        events.request_success.fire(request_type="测试程序类型", name="name1", response_time=total_time,response_length=0)
    @task(1)
    def index2(self):
        start_time = time.time()
        print("doing something++++++++++")
        total_time = int((time.time() - start_time) * 1000)
        e = Exception("抛出一个异常")
        events.request_failure.fire(request_type="测试程序类型", name="name2", response_time=total_time, response_length=0,exception=e)

class WebsiteUser(Locust):
    print("WebsiteUser")
    host = 'http://www.baidu.com'
    def setup(self):
        print("HttpLocust  setup*****************************")
    def teardown(self):
        print("HttpLocust  teardown*****************************")
    task_set = UserBehavior
    wait_time = between(0.1, 0.5) # 等待5-9秒



