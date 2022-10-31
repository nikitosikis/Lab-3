#Вариант 5 2x4 астма 20 ов
#Писал как можно более обощенно, но работать будет всеравно только с размерность 2х4 и максимальным размером вещи 3x1, с другим stash играться не пробовал
stash = {'в': [25, 3, 0], 'п': [15, 2, 0], 'б': [15, 2, 0], 'Ап': [20, 2, 0], 'и': [5, 1, 1], 'н': [15, 1, 0], 'т': [20, 3, 0], 'о': [25, 1, 0], 'ф': [15, 1, 0], 'Ан': [10, 1, 0], 'е': [20, 2, 0], 'Ар': [20, 2, 0]}
inv_fr_sp = 8
Surv_points = 20
inv = [[0, 0, 0, 0], [0, 0, 0, 0]]
pop_time = []
for i in stash.items():
    if i[1][2] == 1:
        pr = 0
        Surv_points += i[1][0]
        inv_fr_sp -= i[1][1]
        if i[1][1] == 1:
            for i2 in range(len(inv)):
                for j2 in range(len(inv[i2])):
                    print(inv[i2][j2])
                    if inv[i2][j2] == 0:
                        inv[i2][j2] = i[0]
                        pr = 1
                        break
                if pr == 1:
                    break
        if pr == 0:
            print('В инвентарь не влезают все нужные объекты, Том гарантированно умирает')
            raise SystemExit
        elif i[1][1] == 2:
            for i2 in range(len(inv)):
                for j2 in range(len(inv[i2])):
                    if inv[i2][j2] == 0:
                        try:
                            if inv[i2][j2+1] == 0:
                                inv[i2][j2], inv[i2][j2+1] = i[0]
                                pr = 1
                                break
                        except IndexError:
                            break
                if pr == 1:
                    break
            if pr == 0:
                if inv[0][3] == 0 and inv[1][3] == 0:
                    inv[0][3] = i[0]
                    inv[1][3] = i[0]
            else:
                print('В инвентарь не влезают все нужные объекты, Том гарантированно умирает')
                raise SystemExit
        elif i[1][1] == 3:
            for i2 in range(len(inv)):
                for j2 in range(len(inv[i2])):
                    if inv[i2][j2] == 0:
                        try:
                            if inv[i2][j2+1] == 0 and inv[i2][j2+2] == 0:
                                inv[i2][j2], inv[i2][j2+1] = i[0]
                                pr = 1
                        except IndexError:
                            break
                if pr == 1:
                    break
            if pr == 0:
                print('В инвентарь не влезают все нужные объекты, Том гарантированно умирает')
                raise SystemExit
        pop_time.append(i[0])
for i in pop_time:
    stash.pop(i)
pop_time = []
stash = dict(sorted(stash.items(), key=lambda x: [x[1][0]/x[1][1], x[1][0]], reverse=True))
print(stash)
for i in stash.items():
    print(i[0])
    pr = 0
    if inv_fr_sp > 0:
        if i[1][1] <= inv_fr_sp:
            if i[1][1] == 1:
                for i2 in range(len(inv)):
                    if pr == 1:
                        break
                    for j2 in range(len(inv[i2])):
                        if inv[i2][j2] == 0:
                            inv[i2][j2] = i[0]
                            Surv_points += i[1][0]
                            inv_fr_sp -= i[1][1]
                            pop_time.append(i[0])
                            pr = 1
                            break

            elif i[1][1] == 2:
                for i2 in range(len(inv)):
                    if pr == 1:
                        break
                    for j2 in range(len(inv[i2])):
                        if inv[i2][j2] == 0:
                            try:
                                if inv[i2][j2 + 1] == 0:
                                    inv[i2][j2] = i[0]
                                    inv[i2][j2 + 1] = i[0]
                                    Surv_points += i[1][0]
                                    inv_fr_sp -= i[1][1]
                                    pop_time.append(i[0])
                                    pr = 1
                                    break
                            except IndexError:
                                if inv[i2][j2 + 1] == 0 and inv[i2][j2 + 2] == 0:
                                    inv[i2][j2] = i[0]
                                    inv[i2][j2 + 1] = i[0]
                                    Surv_points += i[1][0]
                                    inv_fr_sp -= i[1][1]
                                    pop_time.append(i[0])
                                    pr = 1
                                break

            elif i[1][1] == 3:
                for i2 in range(len(inv)):
                    for j2 in range(len(inv[i2])):
                        if inv[i2][j2] == 0:
                            try:
                                if inv[i2][j2 + 1] == 0 and inv[i2][j2 + 2] == 0:
                                    inv[i2][j2] = i[0]
                                    inv[i2][j2 + 1] = i[0]
                                    inv[i2][j2 + 2] = 0
                                    Surv_points += i[1][0]
                                    inv_fr_sp -= i[1][1]
                                    pop_time.append(i[0])
                                    pr = 1
                                    break
                            except IndexError:
                                break
print(pop_time)
for i in pop_time:
    stash.pop(i)
print(stash)
for i in stash:
    Surv_points -= stash[i][0]
print(Surv_points)
for i in inv:
    print(i)
