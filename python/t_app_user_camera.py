# coding=utf-8
def write_sql():
    file = open('t_app_user_camera.sql', 'w')

    character = []
    for i in range(65, 91):
        character.append(chr(i))

    qid = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                qid.append('QMULU' + character[i] + character[j] + character[k])

    user = [0, 5687343462985000000, "NULL", True]

    for i in  range(1, len(qid)):
        sql = "INSERT INTO t_app_user_camera " \
                "VALUES(%d, %d, %d, %d, %d, '%s', %s, %d, %s, %s);" % \
              (i, user[1] + i, i, user[0], user[0], qid[i-1], user[3], user[0], user[2], user[2])
        file.write(sql)
        file.write("\n")

    file.close()
        
if __name__ == '__main__':
    write_sql()

