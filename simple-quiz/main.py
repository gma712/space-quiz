from data.questions import QUESTIONS
import random
import time


def main():
  player_life = 5
  enemy_life = 5
  print("""
  ゲームスタート！！

  あなたのライフ: {0}
  敵のライフ: {1}
  """.format(player_life, enemy_life))
  time.sleep(1)
  while player_life > 0 and enemy_life > 0:
    q = random.choice(QUESTIONS)
    choices = q['CHOICES']
    print("""
    ****************************************
    問題: {0}

    1: {1}
    2: {2}
    3: {3}
    ****************************************
    
    番号を入力してください。
    """.format(q['Q'], choices[0], choices[1], choices[2]))

    ans = int(input())

    if choices[ans - 1] == q['ANSWER']:
      enemy_life -= 1
      print("""
      **********
      正解！
      **********

      あなたのライフ: {0}
      敵のライフ: {1}
      """.format(player_life, enemy_life))
    else:
      player_life -= 1
      print("""
      **********
      ざんねん！
      **********

      あなたのライフ: {0}
      敵のライフ: {1}
      """.format(player_life, enemy_life))
    time.sleep(1)
  
    if player_life == 0:
      print('あなたの負け')
    elif enemy_life == 0:
      print('あなたの勝ち')
    

if __name__ == '__main__':
  main()