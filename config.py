'''

@author:54kk&Chatgpt

'''



TARGET_DATE = '20230921'                                       # 定义目标日期，用于检查是否有更新
NO_UPDATE_TEXT = "NOT YET UPDATED"                             # 定义未更新时输出的文本
MONITORED_URLS = ['url1', 'url2', 'url3', 'url7', 'url8']      # 定义需要监测的URL列表
SLEEP_TIME = 21600                                             # 定义程序每次休眠的时间（秒）


'''
一些关于监控的URL的说明:
按照下面给的例子塞进去即可

url:你需要爬取的首页网址
alias:相当于你给这个url的备注
publish_date_xpath:发布日期的xpath地址
doc_url_xpath:文章的url xpath地址
doc_title_xpath:文章题目的xpath地址

具体如何找到xpath地址请看README,xpath语法自行学习

'''

URL_ALIAS = {
    'url1': {
        'url': 'https://xxgk.fudan.edu.cn/zszcwzszchgdwzszymlhfzyzsjhwfslqbf/list.htm',
        'alias': '招生章程、招生政策和规定、招生专业目录和分专业招生计划、复试录取办法',
        'publish_date_xpath': '//div[@class="fields ex_fields"]/span[@class="Article_PublishDate"]/text()',
        'doc_url_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@href',
        'doc_title_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@title'
    },
    'url2': {
        'url': 'https://xxgk.fudan.edu.cn/yjszs/list.htm',
        'alias': '研究生招生汇总',
        'publish_date_xpath': '//div[@class="fields ex_fields"]/span[@class="Article_PublishDate"]/text()',
        'doc_url_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@href',
        'doc_title_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@title'
    },
    'url3': {
        'url': 'https://xxgk.fudan.edu.cn/gywxwswhxkwzyzsyjsrs/list.htm',
        'alias': '各院（系、所）或学科、专业招收研究生人数',
        'publish_date_xpath': '//div[@class="fields ex_fields"]/span[@class="Article_PublishDate"]/text()',
        'doc_url_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@href',
        'doc_title_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@title'
    },
    'url4': {
        'url': 'https://xxgk.fudan.edu.cn/cjyjsfsksdcscjwfscjwzcj/list.htm',
        'alias': '参加研究生复试考生的初试成绩、复试成绩、总成绩',
        'publish_date_xpath': '//div[@class="fields ex_fields"]/span[@class="Article_PublishDate"]/text()',
        'doc_url_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@href',
        'doc_title_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@title'
    },
    'url5': {
        'url': 'https://xxgk.fudan.edu.cn/nlqksmd/list.htm',
        'alias': '拟录取考生名单',
        'publish_date_xpath': '//div[@class="fields ex_fields"]/span[@class="Article_PublishDate"]/text()',
        'doc_url_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@href',
        'doc_title_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@title'
    },
    'url6': {
        'url': 'https://gsao.fudan.edu.cn/15156/list.htm',
        'alias': '简章目录',
        'publish_date_xpath': '//span[@class="cols_meta"]/text()',
        'doc_url_xpath':   '//span[@class="cols_title"]/a/@href',
        'doc_title_xpath': '//span[@class="cols_title"]/a/@title'
    },
    'url7': {
        'url': 'https://gsao.fudan.edu.cn/main.htm',
        'alias': '简章目录',
        'publish_date_xpath': '//span[@class="news_date"]/text()',
        'doc_url_xpath':   '//span[@class="news_title"]/a/@href',
        'doc_title_xpath': '//span[@class="news_title"]/a/@title'
    },
    'url8': {
        'url': 'https://yjsy.fjmu.edu.cn/2439/list1.htm',
        'alias': '福建医科大学招生简章',
        'publish_date_xpath': '//div[@class="fields ex_fields"]/span[@class="Article_PublishDate"]/text()',
        'doc_url_xpath':   '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@href',
        'doc_title_xpath': '//div[@class="fields pr_fields"]/span[@class="Article_Title"]/a/@title'
    }
}
