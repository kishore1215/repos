import threading, concurrent.futures  #in Py2, must do, pip install futures
import requests,time,urllib.parse
import os.path ,sys,bs4
import functools

#debug print 
def printD(debug,printLck, *args, **kargs):
    if debug:
        with printLck:
            print(threading.current_thread().getName(),*args, **kargs)

#without query etc 
def getBaseDomain(url):
    u = urllib.parse.urlsplit(url)
    #reset query and fragment 
    return urllib.parse.urlunsplit( (u.scheme, u.netloc,u.path,'','') )
    
def getFileName(url):
    u = urllib.parse.urlsplit(url)
    return u.path[u.path.rfind("/")+1:]  #might '' or actual path 
    
def getAllLinks(url, page, baseDomain,printLck, debug=True):
    soup = bs4.BeautifulSoup(page, "html.parser")  
    raw_links = [link.get('href') for link in soup.find_all('a')]
    def process_each(link):
        fullUrl = urllib.parse.urljoin(url,link)
        return fullUrl if baseDomain in fullUrl else ''
    result = [ process_each(link)  for link in raw_links if process_each(link) ]
    printD(debug, printLck, ": parsed: ", result)
    return result

def load(url, printLck, sleep=0.1,debug=True, dir=r".", createFile=True):
    time.sleep(sleep)
    printD(debug, printLck, ": starting download ",url)
    conn = requests.get(url)  
    fileName = getFileName(url)
    if createFile and fileName:
        #create files 
        #might fail 
        try:
            with open(os.path.normpath(os.path.join(dir,fileName)), "wt") as f:
                f.write(conn.text)
        except Exception as ex :
            printD(debug, printLck, ":", str(ex)) 
    return [url, conn.text]
    
if __name__ == '__main__':
    baseUrl = sys.argv[1] if len(sys.argv) >= 2 else "http://ss64.com/bash/"
    basedomain = getBaseDomain(baseUrl)
    masterSetWithLinks = set()
    #* lock creation- for printing , lock var name is pLck
    #other vars 
    sleep = 0.1
    debug = True
    dir = r"./download"
    createFile = True
    maxDepth = 1 
    HACK = True
    #*Create executor - var name executor 
    #*submit for base url 
    #*parse and get all links 
    #update master set 
    masterSetWithLinks.update(set(urls))
    
    ###Hack start - to download only 20 
    hackMaxDownload = 20
    if HACK:
        urls = urls[:hackMaxDownload]
    ###Hack -end 
    
    #fire maps 
    fnload = functools.partial(load, printLck=pLck, sleep=sleep,debug=debug, dir=dir, createFile=createFile)
    fnlinks = functools.partial(getAllLinks, baseDomain=basedomain, printLck=pLck, debug=debug)
    depth = 0
    while depth < maxDepth:
        #res = [ (url,page),...]
        #* call map to get above res 
        
        #* and process to get urls, pages 

        #* get all pages links via map with result as below 
        #res = [ [links], [links] ]        
        

        #flatten res 
        res = [item for sublist in res for item in sublist]
        #take only diff 
        urls = list(set(res) - masterSetWithLinks)
        masterSetWithLinks.update(set(res))
        depth += 1
        printD(debug, pLck, ":next depth:",depth, urls ) 
    #executor.shutdown()