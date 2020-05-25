from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
from manipulator import Manipulator

# 我的机械手
manipulator = Manipulator()


@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


# 设置机械助手位置
def set_position(x, y):
    print('debug: 设置窗口位置', x, y)
    manipulator.position = [x, y]
    manipulator.region = (manipulator.position[0], manipulator.position[1], manipulator.size[0] + manipulator.position[0], manipulator.size[1] + manipulator.position[1])


# 获取机械助手位置
def get_position():
    print('debug: 获取窗口位置')
    return {
        "position":  manipulator.position
    }


@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["setPosition"] = set_position
    dispatcher["get_position"] = get_position

    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    print('--- 项目启动 ---')
    run_simple('localhost', 4000, application)