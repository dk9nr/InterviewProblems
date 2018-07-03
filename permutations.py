def perm(s):
    results=[]
    help([],s,results)
    return results
    
def help(prefix,suffix,results):
    if not suffix:
        results.append(prefix)
    else:
        for i in range(len(suffix)):
                help(prefix+[suffix[i]],suffix[:i]+suffix[i+1:],results)


if __name__ == "__main__":
    print (perm([1,2,3,4,5]))

