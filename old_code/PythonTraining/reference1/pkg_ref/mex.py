def square(x):
    """Saure function
    takes one arg"""
    z = x*x 
    return z
    
# 'avg' which takes one list of numbers 
#and return average of that numbers 

def avg(lst):
    return sum(lst)/len(lst)
    
#'std' - std deviation 

def std(lst):
    import math 
    m = avg(lst)
    lst_p = [(x-m)**2 for x in lst]
    return math.sqrt( sum(lst_p)/len(lst)   )
    
    
def median(lst):
    lst_s = sorted(lst)
    mid = len(lst)//2
    if len(lst) % 2 == 1:
        return lst_s[mid]
    else :
        return avg( [ lst_s[mid], lst_s[mid-1] ] )
        
#####################
def download(url):
    import requests
    import time
    import threading
    time.sleep(5)
    print("Starting to download ", url, " from thread ", threading.current_thread().getName())
    conn = requests.get(url)    
    return [url, len(conn.text)]

def is_prime(n):
    import math
    if n == 2 : return True 
    if n % 2 == 0:	return False
    sqrt_n = int(math.sqrt(n))
    a = [1 for i in range(3, sqrt_n + 1, 2) if n % i == 0]
    return False if sum(a) > 0 else True