import os
import re

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """判断一个unicode是否是半角数字"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False

def is_Qnumber(uchar):
    """判断一个unicode是否是全角数字"""
    if uchar >= u'\uff10' and uchar <= u'\uff19':
        return True
    else:
        return False

def is_alphabet(uchar):
    """判断一个unicode是否是半角英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

def is_Qalphabet(uchar):
    """判断一个unicode是否是全角英文字母"""
    if (uchar >= u'\uff21' and uchar <= u'\uff3a') or (uchar >= u'\uff41' and uchar <= u'\uff5a'):
        return True
    else:
        return False
def is_other(uchar):
    """判断是否非汉字，数字和英文字符"""
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False
def B2Q(uchar):
    """单个字符 半角转全角"""
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e: # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020: # 除了空格其他的全角半角的公式为: 半角 = 全角 - 0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return chr(inside_code)
def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e: #转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)
def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])

def stringPartQ2B(ustring):
    """把字符串中数字和字母全角转半角"""
    return "".join([Q2B(uchar) if is_Qnumber(uchar) or is_Qalphabet(uchar) else uchar for uchar in ustring])

def stringB2Q(ustring):
    """把字符串半角转全角"""
    return "".join([B2Q(uchar) for uchar in ustring])

def iterate_files(rootDir):
    for dirPath, dirNames, fileNames in os.walk(rootDir):
        for fileName in fileNames:
            filePath = os.path.join(dirPath, fileName)
            yield filePath

# Get the current working directory path
current_dir = os.getcwd()
rootDir = os.path.join(current_dir, "Classical-Modern/古文原文")
files = iterate_files(rootDir)

outPutFile = os.path.join(current_dir, "classical_articals.txt")

with open(outPutFile, 'w') as outFile:
    for file in files:
        with open(file, 'r') as f:
            for line in f.readlines():
                s = re.sub(r'<[^<>]*>', r'', line)
                s = s.replace(' ', '')
                s = stringB2Q(s)
                s = stringPartQ2B(s)
                outFile.writelines(s)

