import os

def copyImg():
    in_dir=os.path.join('.','source','_post','')
    
    in_dir=os.path.abspath(in_dir)
    
    # for a in os.walk(r'O:\github\Pastry97\Pastry97.github.io'):
    #     print('x',a)
    print(in_dir)

    for root,dirs,files in os.walk(r'O:\github\Pastry97\Pastry97.github.io\source\_post'):
        print('a')
        for f in files:
            print(f)
        for d in dirs:
            print(d)
        print('x',root,dirs,files)
    print('b')
    


# cmd='echo a'

# os.system(cmd)
copyImg()