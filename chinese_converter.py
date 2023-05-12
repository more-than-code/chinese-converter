import opencc
import os
import re

count = 0


def check_chinese(file_path):
    linecount=-1
    # UserFile = open(file_path, "r+")
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            linecount += 1
            pattern = re.compile(r'[\u4e00-\u9fa5]')
            result = pattern.findall(line)
            if result.count != 0:
            # 定义繁体中文字符范围
                converter = opencc.OpenCC("s2t")
                # 中文简体到中文繁体的转换
                text_t = converter.convert(line)
                if(text_t != line):
                    # 替换为已翻译文字
                    # lines[linecount] = text_t
                    print(f"文件中包含简体中文：\n第{linecount}行 \n{file_path}，\n内容：{line} \n对应繁体：{text_t}")
                    global count  # 声明 count 为全局变量
                    count += 1
        # 写入替换好的文件
        # with open(file_path, 'w') as file:
        #     file.writelines(lines)

def traverse_dir(dir_path):
    entities = os.listdir(dir_path)
    for entity in entities:
        entity_path = os.path.join(dir_path, entity)
        if os.path.isfile(entity_path):
            if entity_path.endswith(".dart"):
                check_chinese(entity_path)
        elif os.path.isdir(entity_path):
            if entity_path.endswith('config')==False:
                traverse_dir(entity_path)

# 文件夹路径
traverse_dir("/Users/mac/Documents/flutterProject/mohiguide-mobileapp/lib")
print(f"检测完毕，共找到：{count}处简体字")
