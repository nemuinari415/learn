# 都道府県ごとの人口集計
from logic.population_data_1 import PopulationData as PD


def population_aggregate(pd):
    new_pd = {}
    for data in pd:
        pref = data["pref"]
        city = data["city"]
        pop = data["pop"]

        if pref not in new_pd:
            new_pd[pref] = 0
        new_pd[pref] += pop

    return new_pd


def print_result(result):
    for pref, pop in sorted(
        result.items(),
        key=lambda x: x[1],
        reverse=True,
    ):
        print(f"{pref} : {pop:,}人")


if __name__ == "__main__":
    pd = PD.population_data
    pa = population_aggregate(pd)
    print_result(pa)
