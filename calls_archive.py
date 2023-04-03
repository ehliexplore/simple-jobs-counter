

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
        data_list = list()
        for d in a:
            data = d.split(';')
            data[1] = data[1].replace('\n', '')

            data_list = (f'{data[0]};{data[1]}')
        return data_list
    finally:
        a.close()
