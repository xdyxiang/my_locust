## **my_locust**
> 这是一个python的性能测试框架，基于协程gevent，





---- 
### 设置http断言

* http设置断言
    1. 在self.client.get("/",catch_response=True)加catch_response=True参数
    2. 接收response.status_code进行判断
        ```
        if response.status_code == 200:
            response.failure('Failed!')
        else:
            response.success()
        ```

* 自定义断言：
    1. `from locust import Locust,HttpLocust, TaskSet, task, between,events`
    2. `events.request_failure.fire(request_type="测试程序类型", name="name2", response_time=total_time, response_length=0,exception=e)`
    3. `events.request_success.fire(request_type="测试程序类型", name="name1", response_time=total_time,response_length=0)`


### 使用技巧
1. 使用fasthttplocust，提升请求的速度
2. 使用galang 版本的locust:https://github.com/myzhan/boomer
    * 使用python locust 运行master，用于展示web
    * 运行go boomer 程序，当做slaver，执行go中的task业务 
