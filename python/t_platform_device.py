# coding=utf-8
def write_sql():
    file = open('t_platform_device.sql', 'w')
    character = []
    for i in range(65, 91):
        character.append(chr(i))

    qid = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                qid.append('QMULU' + character[i] + character[j] + character[k])

    qkey = "MJERZXCA"
    md_qkey = "80DD074A8C0CE267"
    sn = "LOBRDTEST0019"
    mac = "D2262504B239"
    version = "V1.0.00.001"
    hw_version = "03.01.00"
    make_date = "NULL"
    model = "0403"
    status = 2
    create_date = "NULL"
    l_upd_date = "NULL"
    ssn = "QMULUXRDTEST0019"
    md_qkey2 = "A439651E2E419B0F"
    device_id = "NULL"
    for i in  range(1, len(qid)):
        #sn = snpro + '%0.4d' % i
        #mac = macpro + str(i + 200)
        sql = "INSERT INTO t_platform_device " \
              "VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', %d, %s, %s, '%s', '%s', %s);" % \
              (i, qid[i], qkey, md_qkey, sn, mac, version, hw_version, make_date, model, status, create_date, l_upd_date, ssn, md_qkey2, device_id)
        file.write(sql)
        file.write("\n")

    file.close()
        
if __name__ == '__main__':
    write_sql()

