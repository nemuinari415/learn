# logic_025.py ファイルを読み込む
from logic.logic_025 import SurveyCounter

filename = "folder_output/" + "logic_025" + ".csv"

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

# bash
# PYTHONPATH=. python3 run/run_025.py