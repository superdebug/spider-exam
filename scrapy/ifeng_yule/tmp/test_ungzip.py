import gzip
g = gzip.GzipFile(mode="rb", fileobj=open('d1000_sp_posts.sql.gz', 'rb')) # python gzip 解压
open(r"d1000_sp_posts.sql", "wb").write(g.read())
