from locust import HttpLocust, TaskSet, task, between
import os


class UserBehavior1(TaskSet):
    print("task2222222222222222222222222222222")
    def setup(self):
        print(" TaskSet1 setup*****************************")
    def teardown(self):
        print(" TaskSet1 teardown*****************************")
    # 每个用户都会执行
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        print("login1------")

    def logout(self):
        print("logout1------")

    @task(2)
    def index(self):
        response = self.client.get("/sf/vsearch?pd=video&tn=vsearch&lid=8f89de91000b9d89&ie=utf-8&wd=python&rsv_spt=7&rsv_bp=1&f=8&oq=python&rsv_pq=8f89de91000b9d89&rsv_t=217dX3VKXtv8DzRnhYKiVmk4FzY0o6iwW0SPVwDksiMj1ioSETkkpPM13D0",catch_response=True)
        if response.status_code == 200:
            response.failure('Failed!')
        else:
            response.success()

class UserBehavior(TaskSet):
    print("task1111111111111111111111111111111111")
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
        print("login------")

    def logout(self):
        print("logout------")

    @task(2)
    def index(self):
        print("doing something++++++++++")
        response = self.client.get("/",catch_response=True)
        if response.status_code == 200:
            response.failure('Failed!')
        else:
            response.success()

    @task(1)
    def search(self):
        print("doing something++++++++++")
        response = self.client.get("/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&oq=python&rsv_pq=8e97241c0009b0de&rsv_t=6c70bHxhSH17yBt6zo77rs1SqGvmLNGno9vcR0e%2Fmf0y86OZpURFXPzOPdo&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug4=2630&rsv_sug=2",catch_response=True)
        if response.status_code == 200:
            response.failure('Failed!')
        else:
            response.success()
# class allTaskSet(TaskSet):
#     tasks = {UserBehavior:2,UserBehavior1:1}
#
# class AllWebsiteUser(HttpLocust):
#     weight = 3
#     print("WebsiteUser")
#     host = 'http://www.baidu.com'
#     def setup(self):
#         print("all HttpLocust  setup*****************************")
#     def teardown(self):
#         print("all HttpLocust  teardown*****************************")
#     task_set = allTaskSet
#     wait_time = between(2, 5) # 等待5-9秒


class WebsiteUser1(HttpLocust):
    weight = 1
    print("WebsiteUser1")
    host = 'http://www.baidu.com'
    def setup(self):
        print("HttpLocust1  setup*****************************")
    def teardown(self):
        print("HttpLocust1  teardown*****************************")
    task_set = UserBehavior1
    wait_time = between(2, 5) # 等待5-9秒

class WebsiteUser(HttpLocust):
    weight = 1
    print("WebsiteUser")
    host = 'http://www.baidu.com'
    def setup(self):
        print("HttpLocust  setup*****************************")
    def teardown(self):
        print("HttpLocust  teardown*****************************")
    task_set = UserBehavior
    wait_time = between(2, 5) # 等待5-9秒

# if __name__ == "__main__":
#     print(os.getcwd())
#     os.system("locust -f {}/example.py".format(os.getcwd()))


# WEB页面参数
# 1.Number of total users to simulate总并发用户
# 1.Hatch rate (users spawned/second) 每秒产生用户数
# 1.Host 压测的网站

# locust -f locustfiles/example.py   ---------------------------执行所有locust
# locust -f locustfiles/example.py WebsiteUser WebsiteUser1   --------------------------执行指定的locust


# 分布式：
# 1.本机分布式：
# locust -f locustfiles/example.py --master
# locust -f locustfiles/example.py --salve

# 2.多机器分布式
# locust -f locustfiles/example.py --master  --master-bind-host=X.X.X.X    --master-bind-port=5557
# locust -f locustfiles/example.py --slave  --master-host=X.X.X.X    --master-port=5557
