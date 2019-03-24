
def breakdown_file(filename, blocksize):
    blocks = {}
    sizes = []
    data = []
    ln = 0
    for line in open(filename, 'r').readlines():
        data.append(line)
        sizes.append(len(list(line)))
        raw_data = list()
        if len(list(line)) <= 16:
            data_str = line
            for letter in range(16-len(list(line))):
                data_str += '\x00'
            raw_data.append(data_str)
        else:
            data_str = ''
            counter = 0
            for element in list(line):
                if counter==blocksize:
                    raw_data.append(data_str)
                    data_str = ''
                    counter = 0
                data_str += element
                counter += 1
            if len(data_str) !=16:
                for element in range(16-len(data_str)):
                    data_str += ' '
                raw_data.append(data_str)

        ln += 1
        blocks[ln] = raw_data

    return blocks


