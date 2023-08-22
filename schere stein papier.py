# schere stein papier
import random

bot_win = 0
benutzer_win = 0

# 1 schere
# 2 papier
# 3 stein
list_bot = [1, 2, 3]


def bot_auswahl():
    global bot_zug
    global benutzer
    print("1 für schere, 2 für papier, 3 für stein")
    benutzer = int(input(">"))
    bot_zug = random.choice(list_bot)
    gewinner_entscheidung()


def gewinner_entscheidung():
    global benutzer_win
    global bot_win
    if benutzer == 1 and bot_zug == 1:
        print("unentschieden")
    elif benutzer == 1 and bot_zug == 2:
        print("Benutzer hat gewonnen")
        benutzer_win = benutzer_win + 1
    elif benutzer == 2 and bot_zug == 1:
        print("Bot hat gewonnen")
        bot_win = bot_win + 1
    elif benutzer == 1 and bot_zug == 3:
        print("Bot hat gewonnen")
        bot_win = bot_win + 1
    elif benutzer == 3 and bot_zug == 1:
        print("Benutzer hat gewonnen")
        benutzer_win = benutzer_win + 1
    elif benutzer == 2 and bot_zug == 2:
        print("unentschieden")
    elif benutzer == 2 and bot_zug == 3:
        print("Benutzer hat gewonnen")
        benutzer_win = benutzer_win + 1
    elif benutzer == 3 and bot_zug == 2:
        print("Bot hat gewonnen")
        bot_win = bot_win + 1
    elif benutzer == 3 and bot_zug == 3:
        print("unentschieden")
    print(f"Bot hat {bot_win} Siege")
    print(f"Benutzer hat {benutzer_win} Siege")


try:
    while True:
        bot_auswahl()
except:
    print("falsche eingabe")
