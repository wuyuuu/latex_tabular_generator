import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='input.txt')
parser.add_argument('--output', type=str, default='output.txt')
args = parser.parse_args()

tabular = []
tabular.append('\\begin{table}')
with open(args.input, 'r') as f:
    title = f.readline().strip()
    first_column = f.readline().strip()
    first_column_elements = first_column.split(',')
    col_num = len(first_column_elements)
    tabular.append('\\begin{tabular}' + ' {' + '|p{3cm}' * col_num + '|}')
    tabular.append('\\hline')
    tabular.append('\\multicolumn{%d}' % (col_num) + '{|c|}' + '{%s}' % title + '\\\\')
    tabular.append('\\hline')
    temp = ""
    for i in range(col_num):
        if i:
            temp += '&' + first_column_elements[i]
        else:
            temp += first_column_elements[i]
    temp += '\\\\'
    tabular.append(temp)
    tabular.append('\\hline')
    line = f.readline().strip()
    while line:
        line_element = line.split(',')
        temp = ""
        for i in range(len(line_element)):
            if i:
                temp += '&'+line_element[i]
            else:
                temp += line_element[i]
        temp += '\\\\'
        tabular.append(temp)
        line = f.readline().strip()
tabular.append('\\hline')
tabular.append('\\end{tabular}')
tabular.append('\\end{table}')
with open(args.output,'w') as f:
    for ele in tabular:
        f.write(ele+'\n')
