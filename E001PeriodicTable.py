#
# Table Getting Function
#

def GetTable(filename):
    with open(filename, "rb") as f:
        # Get Lines
        table_raw = f.read()
        table_string = table_raw.decode("utf-8")
        table_lines = table_string.split("\n")

        # Split Each Lines Into Lists
        for i in range(len(table_lines)):
            table_lines[i] = table_lines[i].split(" ")

        return table_lines


#
# Formatting Functions
#

def Spaces(length):
    return " " * length


def LineupSpaces(content_before_spaces, spaces_and_content_total_length):
    return " " * (spaces_and_content_total_length - len(content_before_spaces))


#
# Element Outputting Functions
#

def Element(element, serial=True, symbol=True, chinese=True, english=True):
    result = ""

    # Add Serial Number
    if serial is True:
        result += "%3d" % int(element[0])
        result += Spaces(1)

    # Add Symbol of Element
    if symbol is True:
        result += element[1] + LineupSpaces(element[1], 3)
        result += Spaces(1)

    # Add Chinese Name
    if chinese is True:
        result += element[2] + LineupSpaces(element[2], 2)
        result += Spaces(1)

    # Add Latin/English Name
    if english is True:
        judger = lambda: element[4] if element[4][0].lower() == element[1][0].lower() else element[3] + LineupSpaces(element[3], 16) + "(Latin)"
        result += judger()
        result += "\n"

    return result


def SearchOnTable(table, chinese_name, serial=True, symbol=True, chinese=True, english=True):
    index_of_element = [table[i][0] for i in range(0, len(table)) if table[i][2] == chinese_name]
    index_of_element = int(index_of_element[0]) - 1
    return Element(table[index_of_element], serial=serial, symbol=symbol, chinese=chinese, english=english)


#
# Selecting Functions
#
def ElementsIWant(table, serial=True, symbol=True, chinese=True, english=True):
    result = ""

    for i in range(0, 5):
        result += Element(table[i], serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += "\n"

    for i in range(5, 10):
        result += Element(table[i], serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += "\n"

    for i in range(10, 15):
        result += Element(table[i], serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += "\n"

    for i in range(15, 20):
        result += Element(table[i], serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += "\n"

    result += SearchOnTable(table, "金", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "银", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "铜", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "铁", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "锌", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += "\n"

    result += SearchOnTable(table, "钡", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "铂", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "锰", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "汞", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += SearchOnTable(table, "碘", serial=serial, symbol=symbol, chinese=chinese, english=english)
    result += "\n"

    print(result)

    return result




#
# Main Function
#

if __name__ == "__main__":
    table = GetTable("E002OriginPeriodicTableRaw.txt")

    result = ElementsIWant(table)
    result_with_english = ElementsIWant(table, serial=False, symbol=False, chinese=False)
    result_with_chinese = ElementsIWant(table, serial=False, symbol=False, english=False)

    with open("PeriodicTable.txt", "wb") as f:
        f.write(result.encode(encoding="utf-8"))

    with open("PeriodicTableWithEnglish.txt", "wb") as f:
        f.write(result_with_english.encode(encoding="utf-8"))

    with open("PeriodicTableWithChinese.txt", "wb") as f:
        f.write(result_with_chinese.encode(encoding="utf-8"))
