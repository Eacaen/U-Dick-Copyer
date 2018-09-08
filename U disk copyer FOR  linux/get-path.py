import re
P2 = '/media/eacaen/EACAEN-32'
P1 = '/media/eacaen/EACAEN-32/taiwan visa/rutaizheng/1.必须填写的表格/1.入台证申请表-胡天赟.doc'

# pattern = re.compile(P2+r'/.*?/')   # re.I 表示忽略大小写
pattern = P2 + r'/(.*?)(.*)/'
mm = re.findall(pattern, P1 )

for value in mm:
	print(value)

print(mm[0][1])