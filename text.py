# @Time    : 2024/5/8 21:04
# @Author  : SU_SHAN_WAN_YU
# @FileName: text.py
# @Software: PyCharm
# @Description
from matplotlib.font_manager import FontManager

fm = FontManager()
my_fonts = set(f.name for f in fm.ttflist)
print(my_fonts)
you = 1
if you == 2:
    pass
