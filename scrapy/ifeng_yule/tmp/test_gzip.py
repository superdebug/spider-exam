import gzip
f_in = open('d1000_sp_posts.sql','rb')
f_out = gzip.open('d1000_sp_posts.gz','wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()
