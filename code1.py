# -- coding: utf-8 --
from inv import *
from image_match.goldberg import ImageSignature

def sort(matrix,n):
    result=[]
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            if matrix[i][n]<matrix[j][n]:
                tmp=[]
                for k in matrix[i]:
                    tmp.append(k)
                for t in range(len(matrix[i])):
                    matrix[i][t]=matrix[j][t]
                    matrix[j][t]=tmp[t]
    return matrix

def sort1(matrix,n):
    result=[]
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            if matrix[i][n]>matrix[j][n]:
                tmp=[]
                for k in matrix[i]:
                    tmp.append(k)
                for t in range(len(matrix[i])):
                    matrix[i][t]=matrix[j][t]
                    matrix[j][t]=tmp[t]
    return matrix
def computeDeviation(self):
        for ratings in self.data.values():
            for item,rating in ratings.items():
                self.frequency.setdefault(item,{})
                self.deviation.setdefault(item,{})
                for item2,rating2 in ratings.items():
                    if item!=item2:
                        self.frequency[item].setdefault(item2,0)
                        self.deviation[item].setdefault(item2,0.0)
                        self.frequency[item][item2]+=1
                        self.deviation[item][item2]+=(rating-rating2)
        for item,ratings in self.deviation.items():
            for item2 in ratings:
                ratings[item2]/=self.frequency[item][item2]

def predictRating(self,userRatings,k):
    recommendations={}
    frequencies={}
    for item,rating in userRatings.items():
        for diffItem,diffRating in self.deviation.items():
            if diffItem not in userRatings and item in self.deviation[diffItem]:
                fre=self.frequency[diffItem][item]
                recommendations.setdefault(diffItem,0.0)
                frequencies.setdefault(diffItem,0)
                recommendations[diffItem]+=(diffRating[item]+rating)*fre
                frequencies[diffItem]+=fre
    recommendations=[(k,v/frequencies[k]) for (k,v) in recommendations.items()]
    recommendations.sort(key=lambda a_tuple:a_tuple[1],reverse=True)
    return recommendations

def ms(command):
    STORE_DIR = "index1"    
    vm_env.attachCurrentThread()
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    if command == '':
        return
    query = QueryParser(Version.LUCENE_CURRENT, "name",
                        analyzer).parse(command)
    scoreDocs = searcher.search(query, 500).scoreDocs
    result=[]
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)                  
        a=[doc.get('name'),doc.get('url'),doc.get('score'),doc.get('ys'),doc.get('qs'),doc.get('ps'),doc.get('time'),doc.get('imgurl')]
        result.append(a)              
    sort(result,2)
    sort1(result,3)      
    return  result
def xs(command):
    STORE_DIR = "index2"
    vm_env.attachCurrentThread()
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    if command == '':
        return
    query = QueryParser(Version.LUCENE_CURRENT, "name",
                        analyzer).parse(command)
    scoreDocs = searcher.search(query, 500).scoreDocs
    result=[]
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)                  
        a=[doc.get('name'),doc.get('url'),doc.get('score'),doc.get('ys'),doc.get('qs'),doc.get('ps'),doc.get('time'),doc.get('imgurl')]
        result.append(a)    
    sort(result,2)
    sort1(result,3)                  
    return  result
def mf(command):
    STORE_DIR = "index19"
    vm_env.attachCurrentThread()
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    if command == '':
        return
    query = QueryParser(Version.LUCENE_CURRENT, "name",
                        analyzer).parse(command)
    scoreDocs = searcher.search(query, 500).scoreDocs
    result=[]
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)                  
        a=[doc.get('name'),doc.get('url'),doc.get('name2'),doc.get('price'),doc.get('tj'),doc.get('imgurl')]
        result.append(a)
    sort1(result,3)
    sort(result,4)                     
    return  result
def xf(command):
    STORE_DIR = "index20"
    vm_env.attachCurrentThread()
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    if command == '':
        return
    query = QueryParser(Version.LUCENE_CURRENT, "name",
                        analyzer).parse(command)
    scoreDocs = searcher.search(query, 500).scoreDocs
    result=[]
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)                  
        a=[doc.get('name'),doc.get('url'),doc.get('name2'),doc.get('price'),doc.get('tj'),doc.get('imgurl')]
        result.append(a)  
    sort1(result,3)
    sort(result,4)                          
    return  result

def pict(command):
    STORE_DIR = "index"+command
    vm_env.attachCurrentThread()
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)
    if command == '':
        return
    query = QueryParser(Version.LUCENE_CURRENT, "name",
                        analyzer).parse('')
    scoreDocs = searcher.search(query, 500).scoreDocs
    result=[]
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)                  
        a=[doc.get('name'),doc.get('url'),doc.get('name2'),doc.get('price'),doc.get('tj'),doc.get('imgurl')]
        result.append(a)  
    return result

def getmatch(img1,img2):
 gis = ImageSignature()
 a = gis.generate_signature(img1)
 b = gis.generate_signature(img2)
 return gis.normalized_distance(a, b)


def pic_search(img):
    result=0
    f=100
    for i in range(8):
        tmp=0
        mins=100
        for j in range(1,11):
            num=10*i+j
            img2="/static/pic_search/"+str(num)+".jpg"
            dis=getmatch(img,img2)
            if mins>dis: mins=dis
        if f>mins: 
            f=mins
            result=i
    return result+11

urls = (
    '/', 'minhangshop',
    '/mf', 'minhangfood',
    '/xs','xuhuishop',
    '/xf','xuhuifood',
    '/sms', 'mshop', 
    '/smf', 'mfood',
    '/sxs', 'xshop', 
    '/sxf', 'xfood',
    '/tp','foodtp',
    '/hb','hb',
    '/fan','fan',
    '/yrc','yrc',
    '/nc','nc',
    '/zhou',"zhou",
    '/mb','mb',
    '/zj','zj',
    '/mian','mian'
)

render = web.template.render('templates/') 

class minhangshop:
    def GET(self):
        print 'user_data'
        return render.searchshopm()
class minhangfood:
    def GET(self):
        return render.searchfoodm()    
class xuhuishop:
    def GET(self):
        return render.searchshopx()
class xuhuifood:
    def GET(self):
        return render.searchfoodx()
class mshop:
    def GET(self):
        user_data = web.input()
        a = ms(user_data.keyword)
        return render.resultof(a)
class mfood:
    def GET(self):
        user_data = web.input()
        a = mf(user_data.keyword)
        return render.resultoffood(a)
class xshop:
    def GET(self):
        user_data = web.input()
        a = xs(user_data.keyword)
        return render.resultof(a)
class xfood:
    def GET(self):
        user_data = web.input()
        a = xf(user_data.keyword)
        return render.resultoffood(a)
class bj:
    def GET(self):
        return render.resultofbj()
class hb:
    def GET(self):
        a = xf("汉堡")
        return render.resultoffood(a)
class fan:
    def GET(self):
        a = xf("饭")
        return render.resultoffood(a)
class yrc:
    def GET(self):
        a = xf("串")
        return render.resultoffood(a)
class nc:
    def GET(self):
        a = xf("奶茶")
        return render.resultoffood(a)
class zhou:
    def GET(self):
        a = xf("粥")
        return render.resultoffood(a)
class mb:
    def GET(self):
        a = xf("包")
        return render.resultoffood(a)
class zj:
    def GET(self):
        a = xf("鸡")
        return render.resultoffood(a)
class mian:
    def GET(self):
        a = xf("面")
        return render.resultoffood(a)
class pic:
    def GET(self):
        i = web.input(imgfile={})
        filename = 'i.filename'
        a=pic_search(filename)
        b=pict(a)
        return render.resultoffood(b)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    del searcher
