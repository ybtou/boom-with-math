# 导入random模块，用于生成随机数
import random
# 导入os模块，用于调用系统命令
import os

# 定义数字炸弹游戏函数
def number_bomb_game():
    # 打印游戏欢迎信息
    print("=== 数字炸弹游戏 ===")
    print("游戏规则：")
    print("1. 系统会随机生成一个1到100之间的目标数字")
    print("2. 你需要猜测这个数字")
    print("3. 系统会提示你猜的数字是太大还是太小，并缩小范围")
    print("4. 直到你猜对为止")
    print("===================\n")
    
    # 初始化范围边界：最小值为1，最大值为100
    low = 1
    high = 100
    
    # 使用random.randint()函数生成范围内的随机整数作为目标数字
    target_number = random.randint(low, high)
    
    # 初始化猜测次数为0
    guess_count = 0
    
    # 使用while循环创建游戏循环，直到玩家猜对为止
    while True:
        # 获取用户输入的猜测数字，同时显示当前范围
        # input()函数用于获取用户输入，返回字符串类型
        # int()函数将字符串转换为整数
        try:
            # 尝试将用户输入转换为整数
            user_guess = int(input(f"请输入你猜测的数字（{low}-{high}）："))
            
            # 检查用户输入是否在有效范围内
            if user_guess < low or user_guess > high:
                # 如果输入超出范围，提示用户并重新开始循环
                print(f"请输入{low}到{high}之间的数字！\n")
                continue
                
        except ValueError:
            # 如果用户输入的不是数字，捕获ValueError异常
            print("请输入有效的数字！\n")
            # 重新开始循环，不增加猜测次数
            continue
        
        # 猜测次数加1（只有有效输入才计数）
        guess_count += 1
        
        # 判断用户猜测的数字与目标数字的关系
        if user_guess < target_number:
            # 如果猜测数字小于目标数字，更新范围下限
            # 新的下限为用户猜测的数字+1，因为目标数字一定大于猜测值
            low = user_guess + 1
            # 提示用户猜测太小，并显示新的范围
            print(f"太小了！目标数字在 {low}-{high} 之间。\n")
        elif user_guess > target_number:
            # 如果猜测数字大于目标数字，更新范围上限
            # 新的上限为用户猜测的数字-1，因为目标数字一定小于猜测值
            high = user_guess - 1
            # 提示用户猜测太大，并显示新的范围
            print(f"太大了！目标数字在 {low}-{high} 之间。\n")
        else:
            # 如果猜测数字等于目标数字，游戏结束
            # 使用f-string格式化输出，显示目标数字和猜测次数
            print(f"\n🎉 恭喜你猜对了！目标数字就是 {target_number}")
            print(f"你总共猜了 {guess_count} 次")
            # 跳出循环，结束游戏
            break

# 判断是否是直接运行该脚本
# __name__是Python的特殊变量，当脚本直接运行时，__name__的值为"__main__"
if __name__ == "__main__":
    # 调用数字炸弹游戏函数，开始游戏
    number_bomb_game()
    # 调用系统pause命令，等待用户按任意键关闭窗口
    print()
    os.system("pause")