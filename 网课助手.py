from PIL import ImageGrab
from PIL import Image
from aip import AipOcr
import webbrowser

pic = ImageGrab.grabclipboard()

APP_ID = 'your_app_id'
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "false"
u1 = "https://www.baidu.com/s?wd=site%3A(zybang.com)%20"
u2 = "https://www.baidu.com/s?wd="
text = ""
n = 1
m = 1
co = ""
def get_file_content(imp):
    with open(imp, 'rb') as fp:
        return fp.read()
while m == 1:
    print("自动搜题器 beta 0.1 Built @By Bill Luo @Powered By Baidu")
    print("请选择模式:")
    print("1.搜题模式【适用于单纯搜题】")
    print("2.问答模式【适用于网课提问】")
    print("3.关于本软件")
    print("默认为【搜题模式】,直接按【回车】以使用")
    ask = "1"
    ask = input("请输入模式前的数字:")
    if ask == "1" or ask == "":
        while n == 1:
            co = input("按【回车】以继续，如需退出返回上级请输入【e】")
            if co == "":
                pic = "0"
                pic = ImageGrab.grabclipboard()
                if isinstance(pic, Image.Image):
                    pic.save('1.jpg')
                    imp = '1.jpg'
                    image = get_file_content(imp)
                    results = client.general(image, options)
                    for w in results['words_result']:
                        text = text + str(w['words'])
                    url = u1 + text
                    print(url)
                    webbrowser.open(url)
                    text = ""

                else:
                    print("剪贴板里不是图片哟~")
                    pass
            elif co == "e":
                break

    elif ask == "2":
        while n == 1:
            co = input("按【回车】以继续，如需退出返回上级请输入【e】")
            if co == "":
                pic = "0"
                pic = ImageGrab.grabclipboard()
                if isinstance(pic, Image.Image):
                    pic.save('1.jpg')
                    imp = '1.jpg'
                    image = get_file_content(imp)
                    results = client.general(image, options)
                    for w in results['words_result']:
                        text = text + str(w['words'])
                    url = u2 + text
                    print(url)
                    webbrowser.open(url)
                    text = ""
                else:
                    print("剪贴板里不是图片哟~")
                    pass
            elif co == "e":
                break
    elif ask == "3":
        print("*关于*")
        print("*本软件纯属一时头脑发热产品，后续版本随缘更新。")
        print("*本软件基于百度云OCR接口进行字符识别，后调用百度定向搜索作业帮数据或全网搜索完成搜题，题目数据非本人提供。")
        print("*使用方法：用截屏工具（推荐Windows10自带截屏工具Win+Shift+s）截取屏幕上要搜索的题目，选择模式，按下【回车】即可完成搜索。")
        print("*本软件仅做学习交流使用。")
        con = input("按【回车】返回上级")

    else:
        print("选择1或2或3哟~")
        pass
