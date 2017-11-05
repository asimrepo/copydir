import os,time,shutil

def get_information(directory):
    dir="D:\\BE_DB\\BE - Backup - 31-05-2017"
    dir1="D:\\BE_DB\\"
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        #file_list.append([i,time.ctime(a.st_time),time.ctime          #(a.st_ctime)]) #[file,most_recent_access,created]
        file_list.append(i)
    for idx,value in enumerate(file_list):
        if((idx==0) | (idx==2) | (idx==3)):
       
            shutil.copy(os.path.join(dir,value),dir1)
   
    return file_list

print(get_information("D:\BE_DB\BE - Backup - 31-05-2017"))