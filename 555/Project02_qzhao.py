""" This is my simple docstring for the new spring semester """

def get_file():
    ""
    path = input("please type your file wtih the file path: ")
    my_file = open(path, "r")
    rules = {'INDI':'0',
            'FAM':'0',
            'NAME':'1',
            'SEX':'1',
            'BIRT':'1',
            'DEAT':'1',
            'FAMC':'1',
            'FAMS':'1',
            'MARR':'1',
            'HUSB':'1',
            'WIFE':'1',
            'CHIL':'1',
            'DIV':'1',
            'DATE':'2',
            'HEAD':'0',
            'TRLR':'0',
            'NOTE':'0'
        }
    with my_file:
        lines = my_file.readlines()
        striped_lines = []
        result_lines = []
        answer = ''
        for index, each_line in enumerate(lines):
            result = each_line.split()
            if len(result) == 3 and result[0] == '0' and (result[2] == 'INDI' or result[2] == 'FAM'):
                answer = 'Y'
            elif result[1] in rules:
                if rules[result[1]] == result[0]:
                    answer = 'Y'
            else:
                answer = 'N'
            result_lines.append( result[0] + '|' + result[1] + '|' + answer + '|' + ' '.join(result[2:]))
            striped_lines.append(each_line.strip("\n"))
    return striped_lines, result_lines

def main():
    list_1, list_2 = get_file()
    for i, nothing in enumerate(list_1):
        print("--> " + list_1[i])
        print("<-- " + list_2[i])

if __name__ == '__main__':
    main()    