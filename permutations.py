def perm(s):
    results=[]
    s=list(s)
    help([],s,results)
    return results
    
def help(prefix,suffix,results):
    if not suffix:
        results.append("".join(prefix))
    else:
        for i in range(len(suffix)):
                help(prefix+[suffix[i]],suffix[:i]+suffix[i+1:],results)


if __name__ == "__main__":
    print (perm('dev'))

