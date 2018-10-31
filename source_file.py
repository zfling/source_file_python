#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################################
# 解析uboot linux包含的源文件、头文件
# 用于Source Insight工程
#######################################

def my_function():
    print("函数调用")

def source_file_deal(sourceName, headName):
    fread = open(sourceName, 'r')
    fwrite = open("source_file.txt", 'w', encoding='utf-8')
    fheads = open(headName, 'r')
    # c asm source files
    for line in fread:
        #print(line)
        #print(type(line))
        listLine = line.split()
        #print(listLine)
        if listLine[0] == "CC":
            strCC = listLine[1].split('.')[0]+'.c'
            #print(strCC)
            fwrite.write(strCC+'\n')
            continue
        if listLine[0] == "AS":
            strAS = listLine[1].split('.')[0]+'.S'
            #print(strAS)
            fwrite.write(strAS+'\n')
            continue
    # h files
    for line in fheads:
        listLines = line.split()
        for listLine in listLines:
            #print(listLine)
            if listLine.find(".h") >= 0 and listLine.find("generated") < 0:
                if listLine[0]!='/':
                    #print(listLine)
                    fwrite.write(listLine + '\n')

    # close
    fread.close()
    fwrite.close()
    fheads.close()

if __name__=='__main__':
    print("!!!test!!!")
    print("")

    #my_function()
    source_file_deal("uboot_vexpress_log.txt", "autoconf.mk.dep")