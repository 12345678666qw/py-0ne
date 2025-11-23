import random


def guess_number_game():
    # 1. 生成随机数字
    secret_number = random.randint(1, 100)

    # 2. 初始化猜测次数
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想了一个1到100之间的数字，请你来猜一猜。")

    # 3. 主游戏循环
    while True:
        # 4. 获取玩家输入
        try:
            guess = int(input("请输入你猜的数字（1-100）: "))
        except ValueError:
            print("请输入有效的数字！")
            continue

        # 5. 增加猜测次数
        attempts += 1

        # 6. 判断猜测结果
        if guess < secret_number:
            print("太小了！再试试看。")
        elif guess > secret_number:
            print("太大了！再试试看。")
        else:
            print(f"恭喜你！猜对了！答案是 {secret_number}。")
            print(f"你一共猜了 {attempts} 次。")
            break


# 运行游戏
if __name__ == "__main__":
    guess_number_game()