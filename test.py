
def success():
    print("success")

def debug():
    print("debug")

def error():
    print("error")

def warning():
    print("warning")

def other():
    print("other")

def notify_result(num):
    numbers = {
        0 : success,
        1 : debug,
        2 : warning,
        3 : error
    }

    method = numbers.get(num, other)
    if method:
        method()

class Info:
    def __init__(self,Date):
        self.Date=Date

if __name__ == "__main__":
    import time
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    str=f'git commit -m "{date}"'
    print(str)
    a=1
    my_str=f"a={a}"
    print(my_str)