def count_substring(string, sub_string):
    c=0
    n=len(string)
    m=len(sub_string)
    for i in range(n-m+1):
        k=0
        for j in range(i,m+i):
            try:
                if string[j] != sub_string[k]:
                    break;
            except:
                pass
            c+=1
            k+=1    
    c/=m    
    return c

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
