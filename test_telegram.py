from msg_handler import msg_handler

# 测试连接
print("测试Telegram连接...")
if msg_handler.test_connection():
    print("连接成功，发送测试消息...")
    msg_handler.send_to_wx("🤖 测试消息：空投监控系统已成功连接到Telegram！")
else:
    print("连接失败，请检查配置")