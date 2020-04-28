from locust import HttpLocust,TaskSet,task



class TestIndex(TaskSet):
    @task
    def get_baidu(self):
        self.client.get("/")
        print('baidu')

class WebSite(HttpLocust):
    task_set = TestIndex
    min_wait = 1000
    max_wait = 2000
