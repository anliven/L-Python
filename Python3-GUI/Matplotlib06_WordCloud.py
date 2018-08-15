# coding=utf-8
import matplotlib.pyplot as plt
import wordcloud
import jieba
import os

font_file = os.path.join(os.path.dirname("./"), "ZDroidSansFallbackFull.ttf")  # 中文字体文件路径
mask_image = plt.imread("./Zstar.jpg")  # 背景图片

stopwords = set(wordcloud.STOPWORDS)  # 设置屏蔽词
stopwords.add("不见")  # 添加屏蔽词

# contents = "这是一个Python脚本。" \
#            "这是一个关于词云的Python脚本测试。" \
#            "使用matplotlib库绘制图形、jieba库进行中文分词、wordcloud生成词云。"
# words_cut = jieba.cut(contents, cut_all=True)

file_path = open('./ZQiangJinJiu.txt').read()  # 注意txt文件的编码字符集
words_cut = jieba.cut(file_path, cut_all=True)  # 分词
words_join = " ".join(words_cut)  # 分词结果以空格隔开
word_cloud = wordcloud.WordCloud(background_color='white',  # 背景颜色，默认为黑色
                                 mask=mask_image,  # 背景图片
                                 stopwords=stopwords,  # 屏蔽词
                                 font_path=font_file,  # 字体文件
                                 max_words=300,  # 最多显示的词数，默认为200
                                 width=800,  # 宽度
                                 height=800,  # 高度
                                 margin=10,  # 边缘
                                 scale=1.1,  # 缩放系数，默认为1
                                 max_font_size=60,  # 字体最大值
                                 min_font_size=18,  # 字体最小值
                                 random_state=30  # 随机配色的数量
                                 )
word_cloud.generate(words_join)  # 生成词云

plt.imshow(word_cloud)  # 绘制图片
plt.axis("off")  # 去除坐标轴（不显示X轴和Y轴）
plt.show()  # 显示图片

# ### 词云生成库wordcloud
# HomePage: https://github.com/amueller/word_cloud
# 默认中文乱码，需要引入中文字体，在WordCloud构造函数的参数font_path可以指定中文字体文件；
# 也可使用系统自带的支持中文的字体文件，例如window系统下“C:\Windows\Fonts”中ttf格式的字体文件
#
# ### 中文分词库jieba
# HomePage: https://github.com/fxsjy/jieba
