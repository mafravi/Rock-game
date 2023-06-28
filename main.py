from confige import GAME_CHOICES, RULES
import random
def get_user_choice():
   user_input = input("Enter your choice plz ( r , p , s ):")
   if user_input not in GAME_CHOICES:
      print("oops wrong choice")
      return get_user_choice()
   return user_input

def get_sys_choice():
   return random.choice(GAME_CHOICES)

def find_winner(user, system):
   match = {user,system}

   if len(match) == 1:
      return None

   return RULES[tuple(sorted(match))]


def play():
   result = {'user': 0, 'system': 0}
   while result['user'] < 3 and result['system'] < 3:
      user_choice = get_user_choice()
      sys_choice = get_sys_choice()
      winner = find_winner(user_choice,sys_choice)
      if winner == user_choice:
          msg = 'you win'
          result['user'] += 1
      elif winner == sys_choice:
          msg = 'you lost'
          result['system'] += 1
      else:
          msg = 'draw'
      print(f"user: {user_choice}\t system:{sys_choice}\t result: {msg}")
      print(result)




if __name__ == '__main__':
   play()