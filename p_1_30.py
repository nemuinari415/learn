# 問い合わせフォームのデータ処理（擬似バックエンド）
class InquiriesReception:
    def __init__(self, inquiries):
        self.inquiries = inquiries
    
    def add_inquiries(self):
        for item in self.inquiries:
            name, email, message = item["name"], item["email"], item["message"]
            print("--- 問い合わせ受付 ---")
    
            if message == "問い合わせテストです":
                message = "なし"
            print(f"名前 : {name}")
            print(f"メール : {email}")
            print(f"メッセージ : {message}")
            print("-----------------------------" + "\n")
        print("--- 以下略 ---")