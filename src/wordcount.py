__author__ = 'Siyuan'
import re
import os

dic = {}
mid = []

fo = open('../wc_output/med_result.txt', 'w')
fout = open('../wc_output/wc_result.txt', 'w')

files = os.listdir('../wc_input')               #include all the files in the directory
files.sort()                                    #sort the name of files
for item in files:
    if item.endswith('.txt'):

        f = open(os.path.join('../wc_input', item), 'r')
        for line in f:

            txt = re.sub(r'[^\u4e00-\u94a5\w\d\-]', ' ', line) #replace content with blank

            txt = re.sub(r' - ', '', txt) #remove '-'

            count = 0
            for word in txt.split():

                count += 1

                if word.lower() not in dic:

                    dic.setdefault(word.lower(), 0)

                dic[word.lower()] += 1
#find the median
            mid.append(count)
            mid.sort()
            length = len(mid)

            if length > 1:

                if length % 2 == 1:
                    fo.write(str(float(mid[int((length-1 )/ 2)]))+'\n')

                elif length % 2 == 0:
                    number = mid[int(length / 2) - 1] + mid[int(length / 2)]
                    fo.write(str(float(number / 2))+'\n')

            else:
                fo.write(str(float(mid[0]))+str('\n'))

        f.close()

words = sorted(dic.keys()) #sort the dic with the starting character

for item in words:

    fout.write(str(item) + str(' ') + str(dic[item]) + str('\n'))

fout.close()
fo.close()
