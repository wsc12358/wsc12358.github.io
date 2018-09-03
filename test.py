
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

if __name__ == "__main__":
    notify_result(0)
    notify_result(1)
    notify_result(2)
    notify_result(3)
    notify_result(4)