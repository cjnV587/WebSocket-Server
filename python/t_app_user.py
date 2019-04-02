# coding=utf-8
def write_sql():
    file = open('t_app_user.sql', 'w')

    character = []
    for i in range(65, 91):
        character.append(chr(i))

    email = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                email.append('BCAAA' + character[i] + character[j] + character[k])

    user = [5687343462985000000, "NULL", "25d55ad283aa400af464c76d713c07ad", "0400", 1, True, "@qq.com"]

    for i in  range(1, len(email)):
        sql = "INSERT INTO t_app_user " \
                "VALUES(%d, %s, '%s', '%s', '%s', %d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %s, %s, %d, %s, %s);" % \
              (user[0] + i, user[1], email[i] + user[6], user[2], user[3], user[4], user[1], user[1], user[1], user[1], \
               user[1],  user[5], user[1], user[1], user[1], user[1], user[4], user[1], user[1], user[4], user[1], user[1],)
        file.write(sql)
        file.write("\n")

    file.close()
        
if __name__ == '__main__':
    write_sql()

