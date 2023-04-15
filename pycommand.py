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
def choice_block():
    print("请选择方块")
    data = {"1":"stone","2":"grass","3":"dirt","4":"cobblestone","5":"planks","6":"sapling","7":"bedrock"}
    print("1.石头 2.草方块 3.泥土 4.圆石 5.木板 6.树苗 7.基岩")
    choice_input = input(">>>")
    if choice_input in data:
        pycommand(data[choice_input])
    else:
        print("中途退出生成")
        exit()
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
    print("1.命令方块 2.结构方块 3.结构空位 4.自行输入方块id(tips:推荐去查Minecraft Wiki)")
    input_3 = input(">>>")
    if input_3 == "1":
        pycommand(" command_block")
        print("已生成'command_block'")
    elif input_3 == "2":
        pycommand(" structure_block")
        print("已生成'structure_block'")
    elif input_3 == "3":
        pycommand(" structure_void")
        print("已生成'structure_void'")
    elif input_3 == "4":
        pycommand(" " + input(">>>"))
        print("已生成")
    else:
        print("中途退出生成")
        exit()
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