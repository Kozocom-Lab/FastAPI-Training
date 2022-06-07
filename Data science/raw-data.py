import csv

with open("data.txt", "r") as file:
    datas = file.read().split("\n")
with open("data-raw.csv", "w", encoding="utf8", newline="") as file_csv:
    header = ["sbd", "họ tên", "ngay", "thang", "nam", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]
    write = csv.writer(file_csv)
    write.writerow(header)

sbd = 2000000
for data in datas:
    sbd += 1
    sbd_str = "0" + str(sbd)
    data = data.split("\\n")
    unempty_line = []
    for i in range(len(data)):
        data[i] = data[i].replace("\\r","").replace("\\t", "")
        tags = []
        for j in range(len(data[i])):
            if data[i][j] == "<":
                begin = j
            if data[i][j] == ">":
                end = j
                tags.append(data[i][begin:end+1])  
        for tag in tags:
            data[i] = data[i].replace(tag, "")
        data[i] = data[i].strip()

        if data[i] != "":
            unempty_line.append(data[i])
    data  = unempty_line
    name  = data[7]
    bod   = data[8]
    scores = data[9]

    chars = []
    codes = []

    with open("utf8.txt", "r", encoding="utf8") as file:
        unicode_table = file.read().split("\n")
        for code in unicode_table:
            x = code.split("	")
            chars.append(x[0])
            codes.append(x[1])

    for i in range(len(chars)):
        name = name.replace(codes[i], chars[i])
        scores = scores.replace(codes[i], chars[i])

    # chr -> convert
    for i in range(len(name)):
        if name[i:i+2] == "&#":
            name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]

    for i in range(len(scores)):
        if scores[i:i+2] == "&#":
            scores = scores[:i] + chr(int(scores[i+2:i+5])) + scores[i+6:]

    # change to lower case
    name = name.lower()
    scores = scores.lower()
    # split bod
    bod = bod.split("/")
    dd = bod[0]
    mm = bod[1]
    yy = bod[2]

    #remove
    scores = scores.replace(":", "")
    scores = scores.replace("khxh ", "khxh   ")
    scores = scores.replace("khtn ", "khtn   ")
    scores = scores.split("   ")

    data  = [sbd_str, name,str(dd),str(mm),str(yy)]

    for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]:
        if subject in scores:
            data.append(str(scores[scores.index(subject) + 1]))
        else:
            data.append("-1")

    #write data csv
    with open("data-raw.csv", "a", encoding="utf8", newline="") as file:
        write = csv.writer(file)
        write.writerow(data)