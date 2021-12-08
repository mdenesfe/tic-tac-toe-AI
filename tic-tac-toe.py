def yazdir(map):
    print(map[1] + '|' + map[2] + '|' + map[3])
    print('-+-+-')
    print(map[4] + '|' + map[5] + '|' + map[6])
    print('-+-+-')
    print(map[7] + '|' + map[8] + '|' + map[9])
    print("\n")

def ekle(letter, position):
    if bosluk(position):
        map[position] = letter
        yazdir(map)
        if (beraberlik_kontrol()):
            print("Berabere!")
            exit()
        if kazanma_durumu():
            if letter == 'X':
                print("AI Kazandı!")
                exit()
            else:
                print("Sen Kazandın!")
                exit()

        return


    else:
        print("Burası Dolu!")
        position = int(input("Başka Bir Hamle Bul!:  "))
        ekle(letter, position)
        return


def bosluk(position):
    if map[position] == ' ':
        return True
    else:
        return False


def kazanma_durumu():
    if (map[1] == map[2] and map[1] == map[3] and map[1] != ' '):
        return True
    elif (map[4] == map[5] and map[4] == map[6] and map[4] != ' '):
        return True
    elif (map[7] == map[8] and map[7] == map[9] and map[7] != ' '):
        return True
    elif (map[1] == map[4] and map[1] == map[7] and map[1] != ' '):
        return True
    elif (map[2] == map[5] and map[2] == map[8] and map[2] != ' '):
        return True
    elif (map[3] == map[6] and map[3] == map[9] and map[3] != ' '):
        return True
    elif (map[1] == map[5] and map[1] == map[9] and map[1] != ' '):
        return True
    elif (map[7] == map[5] and map[7] == map[3] and map[7] != ' '):
        return True
    else:
        return False


def kazanma_kontrol(mark):
    if map[1] == map[2] and map[1] == map[3] and map[1] == mark:
        return True
    elif (map[4] == map[5] and map[4] == map[6] and map[4] == mark):
        return True
    elif (map[7] == map[8] and map[7] == map[9] and map[7] == mark):
        return True
    elif (map[1] == map[4] and map[1] == map[7] and map[1] == mark):
        return True
    elif (map[2] == map[5] and map[2] == map[8] and map[2] == mark):
        return True
    elif (map[3] == map[6] and map[3] == map[9] and map[3] == mark):
        return True
    elif (map[1] == map[5] and map[1] == map[9] and map[1] == mark):
        return True
    elif (map[7] == map[5] and map[7] == map[3] and map[7] == mark):
        return True
    else:
        return False


def beraberlik_kontrol():
    for key in map.keys():
        if (map[key] == ' '):
            return False
    return True


def ai_hareket():
    bestScore = -800
    bestMove = 0
    for key in map.keys():
        if (map[key] == ' '):
            map[key] = ai
            score = min_max(map, 0, False)
            map[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    ekle(ai, bestMove)
    return


def oyunucu_hareket():
    position = int(input("Hamleni Yap 'O':  "))
    ekle(oyuncu, position)
    return


def min_max(map, dip, maksimize):
    if (kazanma_kontrol(ai)):
        return 1
    elif (kazanma_kontrol(oyuncu)):
        return -1
    elif (beraberlik_kontrol()):
        return 0

    if (maksimize):
        bestScore = -800
        for key in map.keys():
            if (map[key] == ' '):
                map[key] = ai
                score = min_max(map, dip + 1, False)
                map[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in map.keys():
            if (map[key] == ' '):
                map[key] = oyuncu
                score = min_max(map, dip + 1, True)
                map[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


map = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

yazdir(map)
print("Ai Başlıyor \n AI: Tanrı merhamet etsin ben etmicem.")
print("Bu sayıları kullanarak mapte işaretleme yapabilirsin:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
oyuncu = 'O'
ai = 'X'


global ilk_ai_hamlesi
ilk_ai_hamlesi = True

while not kazanma_durumu():
    ai_hareket()
    oyunucu_hareket()