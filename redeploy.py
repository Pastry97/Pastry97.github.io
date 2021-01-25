import os
import shutil

img_suffix=['bmp','jpg','png','tif','gif','pcx','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','ai','raw','WMF','webp','avif']

def copyImg():
    in_dir=os.path.join('.','source','_posts','')
    in_dir=os.path.abspath(in_dir)

    out_dir=os.path.join('.','public','img')
    out_dir=os.path.abspath(out_dir)

    for root,dirs,files in os.walk(in_dir):
        for fname in files:
            suffix=fname.rsplit('.',1)[1]
            #print(suffix)
            if suffix not in img_suffix:
                continue
            out_fp=os.path.join(out_dir,fname)
            if os.path.exists(out_fp):
                continue
            in_fp=os.path.join(root,fname)
            
            #print('{}\n=>{}\n\n'.format(in_fp,out_fp))
            print(fname)
            shutil.copyfile(in_fp,out_fp)

def hexo_reploy():
    cmd='hexo c'
    os.system(cmd)

    cmd='hexo g'
    os.system(cmd)

    cmd='hexo d'
    os.system(cmd)


# cmd='echo a'
# os.system(cmd)
copyImg()
hexo_reploy()