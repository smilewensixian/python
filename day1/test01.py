# 1.简单的 time.sleep + while
import time


def test_api():
    print("test_api_log")


while True:
    test_api()
    time.sleep(60 * 30)

# 2.时间调度模块 sched
import time, os, sched

# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    os.system(cmd)


def timming_exe(cmd, inc=60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()


if __name__ == __"main"__:
    print("show time after 10 seconds:")
    timming_exe("echo %time%", 10)

# scheduler.enter(delay,priority,func,args)
# 第一个参数是一个整数或者float，代表多少秒后执行这个任务
# 第二个参数priority是优先级，0代表优先级最高，1次之，2次次之
# 第三个参数就是你要执行的任务，可以简单的理解成你要执行的函数的函数名
# 第四个参数是你要传入的这个定时执行的action为函数名的函数的参数，最好是用"()"括号来包起来，包起来肯定是不会出错的。--
# --其次，当你只传入一个参数时，用括号包起来后，一定要记住再打上一个逗号。