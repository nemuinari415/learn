# 部署ごとの平均年齢を集計して表示する
class DepartmentStats:
    def __init__(self, users):
        self.users = users
        self.department_data = {}
        self.user_data = {}

    def group_by_department(self):
        for user in self.users:
            name = user["name"]
            department = user["department"]
            age = user["age"]

            if department not in self.department_data:
                self.department_data[department] = [0, 0]
                self.user_data[department] = [name, age, name, age]
            # [0]最年長者の名前, [1]最年長者の年齢, [2]最年少者の名前, [3]最年少者の年齢
            if self.user_data[department][1] < age:
                self.user_data[department][0] = name
                self.user_data[department][1] = age

            if self.user_data[department][3] > age:
                self.user_data[department][2] = name
                self.user_data[department][3] = age

            self.department_data[department][0] += age
            self.department_data[department][1] += 1

    def print_average_age(self):
        for department, (total, count) in self.department_data.items():
            avg = total / count
            for departments, (max_name, max_age, min_name, min_age) in self.user_data.items():
                if departments == department:
                    if max_age == min_age:
                        max_str = f" - 最年長{max_age}歳: {max_name}さん"
                        min_str = ""
                    else:
                        max_str = f" - 最年長{max_age}歳: {max_name}さん"
                        min_str = f" - 最年少{min_age}歳: {min_name}さん"

                    print(f"部署: {department} - 平均年齢: {avg:.0f}歳{max_str}{min_str}")

                else:
                    continue
