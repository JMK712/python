###一个从www.booksvooks.com下载书的爬虫###
#安卓版（运行于qpython）
#目前只有例子能用，别的书还需要获得具体的class名

from bs4 import BeautifulSoup
import requests

def getHTML(url):

    try:

        r = requests.get(url)

        r.raise_for_status()

        r.encoding = r.apparent_encoding

        return r.text

    except:

        return "HTML Get Wrong"

def saveFile(bookname,text):

    with open(r"/storage/emulated/0/"+bookname+".txt",'a') as f:

        for t in text:

            if len(t) > 0:                

                f.writelines(t.get_text() + "\n")

    f.close()

def gethead(url_input,page,part):       

    page_str = str(page)

    part_str = str(part)

    url = url_input + page_str + '&part=' + part_str

    bsObj = BeautifulSoup(getHTML(url),"lxml")

    head = bsObj.findAll(class_="CO")#实际上是第一段

    return head

def getbody(url_input,page,part):

    page_str = str(page)

    part_str = str(part)

    url = url_input + page_str + '&part=' + part_str

    bsObj = BeautifulSoup(getHTML(url),"lxml")

    body = bsObj.findAll(class_="TX")#除了第一段的正文

    return body

def main():    

    page=int(input("""start page(with words)

输入正文开始页码（如chapter 5就输入：5）:"""))

    part=1

    page_str = str(page)

    part_str = str(part)

    url_input ='https://books.feedvu.com/fullbook/network-effect-pdf-martha-wells.html?page='

    #input("""Need the BooksVooks's url,

#输入从BooksVooks获取的网址,尾部去掉page=后的部分

#such as:https://books.feedvu.com/fullbook/network-effect-pdf-martha-wells.html?page=

#例子如上

# input :""")

    url = url_input + page_str + '&part=' + part_str

    totalpage=int(input("""input endpage(ONLY THE MAIN CHARCTER):

输入正文结束页码(如chapter 24就输入：24):"""))

    totalpart=int(input("""maxpart(should little bigger):

最大部分数量（稍大些就OK，如：10）："""))

    bookname=input("""input the book's name(such as:Network Effect):

输入书名(如：Network Effect)：""")

    start=input("""默认路径：本地存储\ 书名.txt

(press enter to start):""")

    

    while page <= totalpage:            

        chapter = 1

        with open(r"/storage/emulated/0/"+bookname+".txt",'a') as f:

            f.write('\n')

            f.write("chapter"+str(chapter))

            f.write('\n')

            f.write('\n')

            f.write('\n')

        while part <= totalpart:

            #try:                

            text = gethead(url_input,page,part)

            saveFile(bookname,text)

            text = getbody(url_input,page,part)

            saveFile(bookname,text)

            print(" part",part,"OK")            

            part += 1                        

            #except:                                                                

                #print("part wrong")                                       

        part = 1

        page += 1

        print("###chapter",chapter,"load successful###")

        chapter = chapter + 1

    print("Totalbook Load Successful!")

main()
