unique_link = set()
with open("Learning/day_1/input.txt", "r", encoding="utf-8") as rf:
    with open("Learning/day_1/output.txt", "w", encoding="utf-8") as wf:
        for line in rf:
            if line.strip():
                if line.strip() not in  unique_link:
                    unique_link.add(line.strip())
                    wf.write(line.strip(" "))
    wf.close()
rf.close()