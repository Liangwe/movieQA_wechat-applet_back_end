# -*- coding:utf-8 -*-
import re

def from_str_split_out_image(ans):
    if ans:
        ans = str(ans)      # 必须str（ans）防止仅有这个二进制字符
        #image = "b'" + ''.join(re.findall(r"b'(.+)'", ans)) + "'"  #两种方法
        image = "b'RIFF" + ans.split("b'RIFF")[1]
        other = ans.split("b'RIFF")[0]
        return other, image
    else:
        pass