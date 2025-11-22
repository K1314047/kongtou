import requests

class msg_handler:
    
    # Telegram Bot 配置
    TELEGRAM_BOT_TOKEN = "you_telegram_bot_token"  # 从 @BotFather 获取
    TELEGRAM_CHAT_ID = "you_telegram_chat_id"      # 个人/群组聊天ID
    
    @classmethod
    def send_to_wx(cls, msg):
        """发送消息到Telegram（保持原方法名不变）"""
        print(f"📱 发送Telegram消息: {msg}")
        return cls.send_to_telegram(msg)
    
    @classmethod
    def send_to_telegram(cls, msg):
        """发送消息到Telegram"""
        if not cls.TELEGRAM_BOT_TOKEN or not cls.TELEGRAM_CHAT_ID:
            print("❌ Telegram配置不完整，请设置BOT_TOKEN和CHAT_ID")
            return False
            
        url = f"https://api.telegram.org/bot{cls.TELEGRAM_BOT_TOKEN}/sendMessage"
        
        payload = {
            "chat_id": cls.TELEGRAM_CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown",  # 支持Markdown格式
            "disable_web_page_preview": True  # 禁用链接预览
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print("✅ 消息已发送到Telegram")
                return True
            else:
                print(f"❌ Telegram发送失败: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ 发送Telegram消息时出错: {e}")
            return False
    
    @classmethod
    def other_notify(cls, msg):
        """其他通知方式（可选）"""
        print(msg)
        # 可以在这里添加其他通知方式，如邮件、钉钉等
        pass

    @classmethod
    def test_connection(cls):
        """测试Telegram连接"""
        if not cls.TELEGRAM_BOT_TOKEN:
            print("❌ 请先设置TELEGRAM_BOT_TOKEN")
            return False
            
        url = f"https://api.telegram.org/bot{cls.TELEGRAM_BOT_TOKEN}/getMe"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                bot_info = response.json()
                print(f"✅ Bot连接成功: {bot_info['result']['first_name']} (@{bot_info['result']['username']})")
                return True
            else:
                print(f"❌ Bot连接失败: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ 连接测试失败: {e}")
            return False
