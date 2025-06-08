class Main:
    def __init__(self):
        print("実行します" + "\n")

    def p_1_01(self):
        # p_1_01.py ファイルを読み込む
        from p_1_01 import Even_odd_num

        even_odd_num = Even_odd_num()
        even_odd_num.input_number()
        even_odd_num.check_even_odd()

    def p_1_02(self):
        # p_1_02.py ファイルを読み込む
        from p_1_02 import Words_list

        words = ["Python", "Programming", "Practice", "File", "Write"]

        words_list = Words_list(words)
        words_list.print_words()

    def p_1_03(self):
        # p_1_03.py ファイルを読み込む
        from p_1_03 import Rectangle

        r = Rectangle()
        r.input_v()
        r.area()
        r.print_v()

    def p_1_04(self):
        # p_1_04.py ファイルを読み込む
        from p_1_04 import Min_Max

        numbers = [13, 7, 20, 3, 19, 2, 8]

        min_max = Min_Max(numbers)
        min_max.min_max_calc()
        min_max.print_num()

    def p_1_05(self):
        # p_1_05.py ファイルを読み込む
        from p_1_05 import JankenGame

        # 実行
        game = JankenGame()
        game.input_player()

        while True:
            game.start_game()
            game.judge()
            
            if game.p1_c == game.p2_c:
                pass
            elif (game.p1_c == 1 and game.p2_c == 2) or \
                (game.p1_c == 2 and game.p2_c == 3) or \
                (game.p1_c == 3 and game.p2_c == 1):
                break
            else:
                break    

    def p_1_06(self):
        # p_1_06.py ファイルを読み込む
        from p_1_06 import Even_Number

        numbers = [11, 22, 33, 44, 55, 66]

        even_number = Even_Number(numbers)
        even_number.calc_num()
        even_number.print_even()

    def p_1_07(self):
        # p_1_07.py ファイルを読み込む
        from p_1_07 import Dict_Marge

        dict_a = {"apple": 100, "banana": 150}
        dict_b = {"orange": 120, "grape": 200}

        dict_marge = Dict_Marge(dict_a, dict_b)
        dict_marge.marges()
        dict_marge.print_marges()

    def p_1_08(self):
        # p_1_08.py ファイルを読み込む
        from p_1_08 import Palindrome

        palindrome = Palindrome()
        palindrome.input_word()
        palindrome.is_palindrome()
        palindrome.print_p()

    def p_1_09(self):
        # p_1_09.py ファイルを読み込む
        from p_1_09 import Data_list

        data = [1, 3, 5, 7]

        data_list = Data_list(data)
        data_list.map_lambda()
        data_list.print_data()

    def p_1_10(self):
        # p_1_10.py ファイルを読み込む
        from p_1_10 import Info_Profile

        info_profile = Info_Profile()
        info_profile.input_profile()
        info_profile.print_profile() 

    def p_1_11(self):
        # p_1_11.py ファイルを読み込む
        from p_1_11 import Phone_Books

        phone_book = {
                    "田中": "090-1234-5678",
                    "佐藤": "080-2345-6789",
                    "鈴木": "070-3456-7890"
                    }

        while True:
            try:
                name = input("名前を入力してください >> ")
            except:
                print("入力が間違ってます")

            if name in phone_book:
                phone_books = Phone_Books(phone_book, name)
                phone_books.print_book()
                break
            
            else:
                print("登録されていません")    

    def p_1_12(self):
        # p_1_12.py ファイルを読み込む
        from p_1_12 import Revers_Num_List

        num_list = []
        n = 1

        while len(num_list) < 5:
            try:
                num_list.append(int(input(f"{n}つ目の数値を入力してください >>")))
                n += 1
            except ValueError:
                print("入力が間違ってます")

        revers_num_list = Revers_Num_List(num_list)
        revers_num_list.revers_num()

    def p_1_13(self):
        # p_1_13.py ファイルを読み込む
        from p_1_13 import Write_Files

        lines = ["こんにちは", "Pythonを学習中です", "ファイルに書き込みます"]

        write_files = Write_Files(lines)
        write_files.write_file()

    def p_1_14(self):
        # p_1_14.py ファイルを読み込む
        from p_1_14 import Circle

        radius = int(input("半径を入力(cm) >>"))

        c = Circle(radius)
        c.area_calc()
        c.circum_calc()
        c.print_circle()

    def p_1_15(self):
        # p_1_15.py ファイルを読み込む
        from p_1_15 import WeekDay

        weekday_jp = ["月", "火", "水", "木", "金", "土", "日"]

        while True:
            day = input("日付を入力(2025-05-29) >>")
            try:
                weekday = WeekDay(day, weekday_jp)
                weekday.d_times()
                weekday.print_weekday()
                break
            except ValueError:
                print("入力が間違ってます")

    def p_1_16(self):
        # p_1_16.py ファイルを読み込む
        from p_1_16 import DiaryLogger

        diary = input("今日の出来事（１行）を入力 >>")

        diary_today = DiaryLogger(diary)
        diary_today.write_diary()
        diary_today.print_diary()

    def p_1_17(self):
        # p_1_17.py ファイルを読み込む
        from p_1_17 import DailyLogger

        memo = input("今日のメモを入力 >>")

        dailylogger = DailyLogger(memo)
        dailylogger.write_dialy()
        dailylogger.print_dialy()

    def p_1_18(self):
        # p_1_18.py ファイルを読み込む
        from p_1_18 import ContactManager

        contact_list = {}

        contact_list["名前"] = input("名前を入力 >>")
        contact_list["電話"] = input("電話を入力 >>")
        contact_list["メール"] = input("メールを入力 >>")

        contact_manager = ContactManager(contact_list)
        contact_manager.add_contact()
        contact_manager.read_contacts()

    def p_1_19(self):
        # p_1_19.py ファイルを読み込む
        from p_1_19 import ToDoManager

        todo_manager = ToDoManager()
        todo_manager.add_task()
        todo_manager.show_tasks()

    def p_1_20(self):
        # p_1_20.py ファイルを読み込む
        from p_1_20 import SalesCalculator

        file_name = "p_1_20_sales.csv"

        sales_calculator = SalesCalculator(file_name)
        sales_calculator.read_csv()
        sales_calculator.calc_total()
        sales_calculator.print_result()

    def p_1_21(self):
        # p_1_21.py ファイルを読み込む
        from p_1_21 import ScoreAnalyzer

        scores = [70, 82, 65, 92, 83, 78]
        filenames = "scores.csv"

        score_analyzer = ScoreAnalyzer(scores, filenames)
        score_analyzer.calc_scores()
        score_analyzer.print_scores()
        score_analyzer.write_scores()
        score_analyzer.read_scores()

    def p_1_22(self):
        # p_1_22.py ファイルを読み込む
        from p_1_22 import SalesAggregator

        filenames = "p_1_22_sales_log.csv"

        sales_aggregator = SalesAggregator(filenames)
        sales_aggregator.read_data()
        sales_aggregator.print_summary()

    def p_1_23(self):
        # p_1_23.py ファイルを読み込む
        from p_1_23 import ContactSearcher

        filenames = "p_1_23_contacts.csv"

        input_names = input("名前を入力 >>")
        contact_searcher = ContactSearcher(filenames, input_names)
        contact_searcher.read_contacts()
        contact_searcher.search_contact() 

    def p_1_24(self):
        # p_1_24.py ファイルを読み込む
        from p_1_24 import SalesAnalyzer

        filenames = "p_1_24_sales.csv"

        sales_analyzer = SalesAnalyzer(filenames)
        sales_analyzer.read_csv_data()
        sales_analyzer.calculate_total_sales()
        sales_analyzer.print_csv_data()

    def p_1_25(self):
        # p_1_25.py ファイルを読み込む
        from p_1_25 import SurveyCounter

        filename = "survey_result.csv"

        votes = {
            "Python": 0,
            "Java": 0,
            "C++": 0,
            "JavaScript": 0
            }

        survery_counter = SurveyCounter(votes)

        while True:
            try:
                print("Python[1] | Java[2] | C++[3] | JavaScript[4]")
                language = int(input("好きな言語に投票してください >>"))
                if language not in [1, 2, 3, 4]:
                    print("入力が間違ってます。")
                    continue
            except ValueError:
                print("入力が間違ってます。")
                
            survery_counter.add_vote(language)
                
            is_continue = input("投票を続けますか？[y | n] >>")
            if is_continue.lower() == "y":
                pass
            else:
                print("投票を終了します")
                break

        survery_counter.print_result()
        survery_counter.write_results(filename)

    def p_1_26(self):
        # p_1_26.py ファイルを読み込む
        from p_1_26 import FolderScanner

        folder_path = input("フォルダのパスを入力 >>")
        # ./sample_folder など

        filename = "file_list.csv"

        folder_scanner = FolderScanner(folder_path)
        folder_scanner.scan_files()
        folder_scanner.save_to_csv(filename)
        folder_scanner.print_summary(filename)

    def p_1_27(self):
        # p_1_27.py ファイルを読み込む
        from p_1_27 import ExtensionCounter

        folder_path = "./sample_folder"
        filename = "ext_summary.csv"

        extension_counter = ExtensionCounter(folder_path)
        extension_counter.scan_folder()
        extension_counter.print_summary()
        extension_counter.write_summary(filename)

    def p_1_28(self):
        # p_1_28.py ファイルを読み込む
        from p_1_28 import SalesManagement

        price_dic = {}
        filename = "sales.csv"

        while True:
            price = input("商品名を入力 >>")
            try:
                price_dic[price] = int(input(f"{price}の価格を入力 >>"))
            except ValueError:
                print("入力ミスです")
                
            cont = input("入力を続けますか？[y | n] >> ")
            if cont.lower() != "y":
                break
        
        sales_management = SalesManagement(price_dic)
        sales_management.add_data()
        sales_management.write_csv(filename)
        sales_management.read_csv(filename)
    
    def p_1_29(self):
        from p_1_29 import SalesManagement

        filename = "p_1_29.csv"
        sales_dic = {}

        sales_management = SalesManagement(sales_dic)
        sales_management.read_add_sales(filename)
        sales_management.print_sales()

    def p_1_30(self):
        from p_1_30 import InquiriesReception
        
        inquiries = [
            {"name": "田中",
             "email": "tanaka@example.com",
             "message": "資料を送ってください"},
            {"name": "山田",
             "email": "yamada@example.com",
             "message": "セミナーの開催日は？"},
            {"name": "佐藤",
             "email": "sato@example.com",
             "message": "問い合わせテストです"}
        ]

        inquiries_reception = InquiriesReception(inquiries)
        inquiries_reception.add_inquiries()
                
    def p_1_31(self):
        from p_1_31 import ProductsPrice

        products = [
            {"name": "りんご", "category": "果物", "price": 120},
            {"name": "バナナ", "category": "果物", "price": 80},
            {"name": "にんじん", "category": "野菜", "price": 100},
            {"name": "ピーマン", "category": "野菜", "price": 90},
            {"name": "牛乳", "category": "飲料", "price": 150}
        ]

        products_price = ProductsPrice(products)
        products_price.group_by_category()
        products_price.output()
    
    def p_1_32(self):
        from p_1_32 import Inquiries

        inquiries = [
        {"name": "田中", "category": "製品", "message": "新しいモデルについて教えて"},
        {"name": "山田", "category": "サポート", "message": "動作がおかしい"},
        {"name": "佐藤", "category": "製品", "message": "価格が知りたい"},
        {"name": "鈴木", "category": "その他", "message": "営業電話を止めてほしい"},
        {"name": "中村", "category": "サポート", "message": "Wi-Fiの接続が不安定"}
    ]
        
        inquiries_obj = Inquiries(inquiries)
        inquiries_obj.group_by_category()
        inquiries_obj.print_category()

    def p_1_33(self):
        from p_1_33 import ProductFilter

        products = [
            {"name": "りんご", "category": "果物", "price": 120},
            {"name": "バナナ", "category": "果物", "price": 80},
            {"name": "にんじん", "category": "野菜", "price": 100},
            {"name": "ピーマン", "category": "野菜", "price": 90},
            {"name": "牛乳", "category": "飲料", "price": 150}
        ]

        category = input("カテゴリーを入力 >>")

        products = ProductFilter(products)
        products.filter_by_category(category)
    
    def p_1_34(self):
        from p_1_34 import ProductStats

        products = [
            {"name": "りんご", "category": "果物", "price": 120},
            {"name": "バナナ", "category": "果物", "price": 80},
            {"name": "にんじん", "category": "野菜", "price": 100},
            {"name": "ピーマン", "category": "野菜", "price": 90},
            {"name": "牛乳", "category": "飲料", "price": 150},
            {"name": "コーヒー", "category": "飲料", "price": 200}
        ]

        products_stats = ProductStats(products)
        products_stats.group_by_category()
        products_stats.print_average_price()
    
    def p_1_35(self):
        from p_1_35 import ProductFilter

        products = [
            {"name": "りんご", "price": 120},
            {"name": "バナナ", "price": 80},
            {"name": "牛乳", "price": 150},
            {"name": "コーヒー", "price": 200}
        ]

        filter_obj = ProductFilter(products)
        filter_obj.filter_by_min_price(150)

# 出力するクラス
main = Main()
main.p_1_35()