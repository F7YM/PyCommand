def pycommand(command):
    f = open("pycommand.txt","a")
    f.write(command)
    f.close()
def choice(mode):
    print("请选择生效对象")
    if mode == "0":
        print("1.自己 2.最近的一个玩家 3.所有玩家 4.所有实体")
    else:
        print("1.自己 2.最近的一个玩家 3.所有玩家")
    choice_input = input(">>>")
    if choice_input == "1":
        pycommand(" @s")
    elif choice_input == "2":
        pycommand(" @p")
    elif choice_input == "3":
        pycommand(" @a")
    elif choice_input == "4":
        if mode == "0":
            pycommand(" @e")
        else:
            print("中途退出生成")
            exit()
    else:
        print("中途退出生成")
        exit()
def choice_item():
    print("请输入物品的正确名称(中英文皆可)且确保您已接入互联网/拥有requests库")
    try:
        import requests
        choice_input = input(">>>")
        url = f"https://ca.projectxero.top/idlist/search?q={choice_input}"
        response = requests.get(url, timeout=10)
        data = response.json()["data"]
        result = str(data["result"])
        a = eval(result.replace("[","").replace("]",""))
        pycommand(" " + a["key"])
    except:
        print("请检查你的互联网连接/数据库无此物品/你是否有requests库(pip install requests)")
        exit()
def choice_parameter():
    print("添加选择器参数")
file_0 = open("pycommand.txt","w")
file_0.close()
open("pycommand.txt","w").write("")
print("""  ____                                                              _ 
 |  _ \  _   _   ___  ___   _ __ ___   _ __ ___    __ _  _ __    __| |
 | |_) || | | | / __|/ _ \ | '_ ` _ \ | '_ ` _ \  / _` || '_ \  / _` |
 |  __/ | |_| || (__| (_) || | | | | || | | | | || (_| || | | || (_| |
 |_|     \__, | \___|\___/ |_| |_| |_||_| |_| |_| \__,_||_| |_| \__,_|
         |___/                                                        """)
print("tips:生成的指令在pycommand.txt里！")
print("0.关于pycommand | 1.杀死 2.给予物品 3.传送")
one = input(">>>")
if one == "0":
    print("Pycommand_0.1.0")
elif one == "1":
    #---↓kill↓---
    pycommand("/kill")
    choice("0")
    print("生成完成")
    #---↑kill↑---
elif one == "2":
    #---↓give↓---
    pycommand("/give")
    choice("1")
    print("请选择要给予的方块")
    choice_item()
    print("请输入物品数量")
    pycommand(" " + input(">>>"))
    print("生成完成")
    #---↑give↑---
elif one == "3":
    #---↓tp↓---
    pycommand("/tp")
    choice("0")
    print("请选择……")
    print("1.传送至某位玩家 2.传送至某坐标")
    input_5 = input(">>>")
    if input_5 == "1":
        print("输入要传送到的玩家的昵称")
        input_6 = input(">>>")
        if " " in input_6:
            pycommand(' "' + input_6 + '"')
        else:
            pycommand(" " + input_6)
        print("生成完成")
    elif input_5 == "2":
        print("输入x坐标")
        pycommand(" " + input(">>>"))
        print("输入y坐标")
        pycommand(" " + input(">>>"))
        print("输入z坐标")
        pycommand(" " + input(">>>"))
        print("生成完成")
    else:
        print("中途退出生成")
        exit()
    #---↑tp↑---