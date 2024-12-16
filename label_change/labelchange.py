import os
import json

def json_2_icdar(js_path, ic_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line)
            content = line.split('\t')
            print(content[0])
            txt_file = str(content[0].split('.')[0])+'.txt'
            dst_file = os.path.join(ic_path, txt_file)
            # write file
            file_lineinfo = open(txt_file, 'w', encoding='utf-8')
            list_dict = json.loads(content[1])
            nsize = len(list_dict)
            print(nsize)
            for i in range(nsize):
                print(list_dict[i])
                lin = list_dict[i]
                info = lin['transcription']
                points = lin['points']
                points = [int(y) for x in points for y in x]
                pts = ','.join(map(str, points))
                lineinfo = pts + ',' + info + '\n'
                file_lineinfo.write(lineinfo)
            file_lineinfo.close()


if __name__ == "__main__":
    src_path = r"C:/Users/PHB/Desktop/label_change/Label.txt"
    dst_path = r""
    json_2_icdar(src_path, dst_path)






if __name__ == "__main__":
    src_path = r"C:/Users/PHB/Desktop/label_change/Label.txt"
    dst_path = r"C:/Users/PHB/Desktop/delGrid4zData/Label.txt"
    json_2_icdar(src_path, dst_path)

