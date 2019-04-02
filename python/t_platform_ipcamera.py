# coding=utf-8
def write_sql():
    file = open('t_platform_ipcamera.sql', 'w')
    character = []
    for i in range(65, 91):
        character.append(chr(i))

    qid = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                qid.append('QMULU' + character[i] + character[j] + character[k])
    ipc = [0, "NULL"]

    for i in  range(1, len(qid)):
        sql = "INSERT INTO t_platform_ipcamera " \
              "VALUES(%d, '%s', %s, %d, %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" % \
              (i, qid[i], ipc[1], ipc[0], ipc[0], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1], ipc[1])
        file.write(sql)
        file.write("\n")

    file.close()
        
if __name__ == '__main__':
    write_sql()

