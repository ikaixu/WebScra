# 期末考核：爬虫项目 #
## 前期准备工作 ##
### 知识储备 ###
 万维网上有着无数的网页，包含着海量的信息，无孔不入、森罗万象。但很多时候，无论出于数据分析或产品需求，我们需要从某些网站，提取出我们感兴趣、有价值的内容，但是纵然是进化到21世纪的人类，依然只有两只手，一双眼，不可能去每一个网页去点去看，然后再复制粘贴。 __所以我们需要一种能自动获取网页内容并可以按照指定规则提取相应内容的程序，这就是爬虫。__  
+  __原理__  
> 传统爬虫从一个或若干初始网页的URL开始  
> 获得初始网页上的URL  
> 在抓取网页的过程中，不断从当前页面上抽取新的URL放入队列,直到满足系统的一定停止条件  
> 聚焦爬虫的工作流程较为复杂，需要根据一定的网页分析算法过滤与主题无关的链接，保留有用的链接并将其放入等待抓取的URL队列。  
> 然后，它将根据一定的搜索策略从队列中选择下一步要抓取的网页URL，并重复上述过程，直到达到系统的某一条件时停止。  
> 另外，所有被爬虫抓取的网页将会被系统存贮，进行一定的分析、过滤，并建立索引，以便之后的查询和检索；所以一个完整的爬虫一般会包含如下三个模块：  
1. 网络请求模块  
2. 爬取流程控制模块  
3. 内容分析提取模块  
+ __爬虫过程__  
> 请求网页  
> 获取网页  
> 匹配信息  
> 下载数据  
> 数据清洗  
> 存入数据  
+ __爬虫框架__
> scrapy  
> pyspider  
