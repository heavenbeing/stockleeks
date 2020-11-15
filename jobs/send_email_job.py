# smtplib 用于邮件的发信动作
import smtplib
import requests
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header

# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = 'heavenbeing@foxmail.com'
password = 'vxmovadvviffbgbj'

# 收信方邮箱
to_addr = '1257358834@qq.com,heavenbeing@outlook.com,603331215@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
response = requests.get('http://ip.cip.cc')

print('ip address:')
print(response.text)

# /stock/data?table_name=guess_indicators_lite_buy_daily
# /stock/data?table_name=guess_indicators_lite_sell_daily
email_content = "Ip address:" + "heavenbeing.tpddns.cn\n" \
                + "stock address:" + "http://heavenbeing.tpddns.cn:8888/\n" \
                + "买入猜想(超买):" + "http://heavenbeing.tpddns.cn:8888/stock/data?table_name=guess_indicators_lite_buy_daily\n" \
                + "卖出猜想(超卖):" + "http://heavenbeing.tpddns.cn:8888/stock/data?table_name=guess_indicators_lite_sell_daily\n" \
                + " \r\n" \
                + " \r\nsend by python"
msg = MIMEText(email_content, 'plain', 'utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('路由器动态ip')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr.split(','), msg.as_string())
# 关闭服务器
server.quit()
