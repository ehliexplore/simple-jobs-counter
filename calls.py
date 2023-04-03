from datetime import date


def line():
    print('=-=-' * 11)


def line2():
    print('=-=-' * 7)


def fileexist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createfile(name):
    try:
        a = open(name,'wt+')
        a.close()
    except:
        print('There was an error creating the file.')
    else:
        print(f'File {name} successfully created.')


def save(name, date, total):
    try:
        a = open(name, 'at')
    except:
        print('Error reading the file (while saving).')
    else:
        try:
            a.write(f'{date};{total}\n')
        except:
            print('Theres an error while saving the file.')
        else:
            print('Jobs saved.')


def showdata(name):
    try:
        a = open(name, 'rt')
    except:
        print('There was an error reading the file.')
    else:
        line()
        print('              SHOWING DATA')
        line()
        for d in a:
            data = d.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]}    {data[1]} jobs')
    finally:
        a.close()


file = 'file.txt'
today = date.today()

print(today)

if fileexist(file):
    pass
else:
    createfile(file)

line()
print(f'       CALL CENTER SAC JOBS COUNTER')
line()
calls = list()

for c in range(0, 6):
    try:
        calls.append(int(input(f"{f'How many calls at the hour {c+1}? ':^40}")))
    except:
        while True:
            try:
                calls.append(int(input(f"{f'How many calls at the hour {c + 1}? ':^40}")))
            except:
                pass
            else:
                break
    else:
        continue

line2()

for v, n in enumerate(calls):
    print(f'Hour {v+1}: {n:>13} Calls')

line2()
total = sum(calls)
print(f'Total: {total} calls received this day.')
line()

while True:
    try:
        answer = str(input('Save results? [Y/N]: ')).strip().upper()[0]
    except:
        print('Type of answer invalid. Insert Y or N.')
    else:
        if answer == 'Y':
            save(file, today, total)
            break
        if answer == 'N':
            break
        else:
            print('Invalid. Insert Y or N.')
            continue

while True:
    try:
        answer2 = str(input('Show saved data? [Y/N]: ')).strip().upper()[0]
    except:
        print('Invalid. Inser Y or N.')
        pass
    else:
        if answer2 == 'Y':
            showdata(file)
            break
        if answer2 == 'N':
            break
        else:
            print('Invalid. Insert Y or N.')
            continue
