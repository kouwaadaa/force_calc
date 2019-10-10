
def para_calc(file_name,force,num):

    iteration = []
    data_num = []
    with open(file_name) as f:
        next(f)
        next(f)
        next(f)

        for line in f:
            data = line.split(' ')
            iteration.append(int(data[0]))
            data_num.append(float(data[1]))

    ave = sum(data_num[-num:])/num
    print('%s:%f' % (force,ave))

    return ave