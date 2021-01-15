"""
用于封装各种常用函数功能
"""
import logging
import qrcode
import requests
from openpyxl import Workbook
from collections import Counter
from docx import Document
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def count_list(array):
    """
    统计列表中元素出现的频率
    :param array: 列表
    :return: 频率由高到低
    """
    result = Counter(array)
    # 排序
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return result


def read_txt_file(path):
    """
    读取txt的每一行放入列表中
    :param path: txt文件路径
    :return: 列表， txt文件的每一行的内容
    """
    with open(path, 'r', encoding="utf-8") as f:
        content = [_.strip() for _ in f.readlines()]
    return content


def creat_excel():
    """
    :return 当前活动文件及表格
    """
    wb = Workbook()
    wb.create_sheet(index=0, title="Sheet1")
    ac_sheet = wb.active
    return wb, ac_sheet


def name_repeat(drug_list):
    """
    除掉嵌套的药品名称
    :param drug_list: 药品名称列表
    :return: 去重后的药品名称列表
    """
    repeat = []
    drug_list = sorted(drug_list, key=lambda x: len(x), reverse=False)  # 按药品名称长度升序排列
    for m in range(len(drug_list) - 1):
        flag = 0
        for n in range(m + 1, len(drug_list)):
            if drug_list[m] in drug_list[n]:
                flag = 1
        if flag == 0:  # 如果不是子字符串
            repeat.append(drug_list[m])
    repeat.append(drug_list[-1])  # 最后一个字符串长度最长，一定不是子字符串
    return repeat


def get_html(url, headers):
    """
    利用requests爬虫获取网页html
    :param url: 网址路径
    :param headers： 浏览器请求头
    :return 网页html
    """
    n = 0
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.encoding = response.apparent_encoding
        html = response.text
        return html
    except ConnectionError:
        n += 1
        if n < 4:
            print('连接超时，正在重新爬取数据......')
            return get_html(url, headers)
        else:
            return None


def load_data(filename):
    """
    加载NER数据
    单条格式：[(片段1, 标签1), (片段2, 标签2), (片段3, 标签3), ...]
    """
    D = []
    with open(filename, encoding='utf-8') as f:
        f = f.read()
        for l in f.split('\n\n'):
            if not l:
                continue
            d, last_flag = [], ''
            for c in l.split('\n'):
                char, this_flag = c.split(' ')
                if this_flag == 'O' and last_flag == 'O':
                    d[-1][0] += char
                elif this_flag == 'O' and last_flag != 'O':
                    d.append([char, 'O'])
                elif this_flag[:1] == 'B':
                    d.append([char, this_flag[2:]])
                else:
                    d[-1][0] += char
                last_flag = this_flag
            D.append(d)
    return D


def log_print(log_path, content):
    """
    打印输出日志
    :param log_path: 日志输出保存路径
    :param content： 保存内容
    :return 网页html
    """
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename=log_path,
                        filemode='a',  # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志,a是追加模式，默认如果不写的话，就是追加模式
                        format='%(asctime)s - %(levelname)s: %(message)s'  # 日志格式
                        )
    logging.info('\n' + content)


def qr_code(url, path='qrcode.png'):
    # 输入一个链接，生成其对应的二维码
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(path)


def pdf2word(src_path, result_path):
    document = Document()
    # rb以二进制读模式打开本地pdf文件
    fn = open(src_path, 'rb')
    # 创建一个pdf文档分析器
    parser = PDFParser(fn)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码doc.initialize("lianxipython")
    # 如果没有密码 就创建一个空的字符串
    doc.initialize("")
    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed

    else:
        # 创建PDf资源管理器
        resource = PDFResourceManager()
        # 创建一个PDF参数分析器
        laparams = LAParams()
        # 创建聚合器,用于读取文档的对象
        device = PDFPageAggregator(resource, laparams=laparams)
        # 创建解释器，对文档编码，解释成Python能够识别的格式
        interpreter = PDFPageInterpreter(resource, device)
        # 循环遍历列表，每次处理一页的内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            # 利用解释器的process_page()方法解析读取单独页数
            interpreter.process_page(page)
            # 使用聚合器get_result()方法获取内容
            layout = device.get_result()
            # 这里layout是一个LTPage对象,里面存放着这个page解析出的各种对象
            for out in layout:
                # 判断是否含有get_text()方法，获取我们想要的文字
                if hasattr(out, "get_text"):
                    # print(out.get_text(), type(out.get_text()))
                    content = out.get_text().replace(u'\xa0', u' ')  # 将'\xa0'替换成u' '空格，这个\xa0就是&nbps空格
                    # with open('example_dis.test','a') as f:
                    #     f.write(out.get_text().replace(u'\xa0', u' ')+'\n')
                    document.add_paragraph(
                        content, style='ListBullet'  # 添加段落，样式为unordered list类型
                    )
                document.save(result_path)  # 保存这个文档
