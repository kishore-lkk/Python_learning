unique_list = set()
with open("Learning/day_1/input.txt", "r", encoding="utf-8") as rf:
    with open("Learning/day_1/output.txt", "w", encoding="utf-8") as wf:
        for line in rf:
            if len(line.strip()) > 0:
                if line.strip() not in unique_list:
                    unique_list.add(line.strip())
                    wf.write(line.strip(" "))
        