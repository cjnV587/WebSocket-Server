# WebSocket-Server-data

为方便后续WebSocket Server并发测试，目前使用Python批量生成数据，具体描述如下：
1、	添加ipc的qid从QMULUAAB开始到QMULUZZZ结束，一共26*26*26 - 1=17575个ipc。
2、	邮箱从BCAAAAAB@qq.com开始到BCAAAZZZ@qq.com结束，一共26*26*26 - 1=17575个注册用户，并为每个用户绑定了一个相机。
3、	相机qid与用户邮箱的对应关系：邮箱是以BCAAA开头，相机的qid以QMULU开头，后三位对应。例如：BCAAAAAB@qq.com对应于QMULUAAB。

数据库测试数据说明：
1、	执行t_app_user.py、t_app_user_camera.py、t_platform_device.py、t_platform_ipcamera.py脚本分别对应生成t_app_user.sql、t_app_user_camera.sql、t_platform_device.sql、t_platform_ipcamera.sql文件；
2、	将数据库的四个表导入到并发测试所使用的数据库中；
