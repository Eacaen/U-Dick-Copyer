##检测Ｕ盘插入
## 从Ｕ盘复制文件
### 递归获取Ｕ盘中文件夹下的文件列表
 * 判断是os.path.isdir or os.path.isfile

### 正则匹配，创建新的原始文件夹
 * 创建文件夹　os.makedirs(path)　直接给字符串路径
 
### 文件复制
 * shutil.copy(file_path, save_path )　