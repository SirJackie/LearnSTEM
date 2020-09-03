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

def Element(element):
    result = ""

    # Add Serial Number
    result += "%3d" % int(element[0])
    result += Spaces(1)

    # Add Symbol of Element
    result += element[1] + LineupSpaces(element[1], 3)
    result += Spaces(1)

    # Add Chinese Name
    result += element[2] + LineupSpaces(element[2], 2)
    result += Spaces(1)

    # Add Latin/English Name
    judger = lambda: element[4] if element[4][0].lower() == element[1][0].lower() else element[3] + LineupSpaces(element[3], 16) + "(Latin)"
    result += judger()
    result += "\n"

    return result


# def ElementWithOnlyLatinOrEnglishName(element):
#     result = ""
#
#     # Add Latin/English Name
#     result += lambda: element[4] if element[4][0].lower() == element[1][0].lower() else element[3] + LineupSpaces(element[3], 16) + "(Latin)"
#     result += "\n"
#
#     return result


def SearchOnTable(table, chinese_name):
    index_of_element = [table[i][0] for i in range(0, len(table)) if table[i][2] == chinese_name]
    index_of_element = int(index_of_element[0]) - 1
    return Element(table[index_of_element])


# def SearchOnTableWithOnlyLatinOrEnglishName(table, chinese_name):
#     index_of_element = table[i][0] for i in range(0, len(table)) if table[i][2] == chinese_name
#     return ElementWithOnlyLatinOrEnglishName(table[index_of_element])


#
# Main Function
#

if __name__ == "__main__":
    table = GetTable("E002OriginPeriodicTableRaw.txt")
    # result_with_only_latin_or_english_name = ""
    #
    # for i in range(0, 5):
    #     result_with_only_latin_or_english_name += ElementWithOnlyLatinOrEnglishName(table[i])
    # result_with_only_latin_or_english_name += "\n"
    #
    # for i in range(5, 10):
    #     result_with_only_latin_or_english_name += ElementWithOnlyLatinOrEnglishName(table[i])
    # result_with_only_latin_or_english_name += "\n"
    #
    # for i in range(10, 15):
    #     result_with_only_latin_or_english_name += ElementWithOnlyLatinOrEnglishName(table[i])
    # result_with_only_latin_or_english_name += "\n"
    #
    # for i in range(15, 20):
    #     result_with_only_latin_or_english_name += ElementWithOnlyLatinOrEnglishName(table[i])
    # result_with_only_latin_or_english_name += "\n"
    #
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "金")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "银")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "铜")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "铁")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "锌")
    # result_with_only_latin_or_english_name += "\n"
    #
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "钡")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "铂")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "锰")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "汞")
    # result_with_only_latin_or_english_name += SearchOnTableWithOnlyLatinOrEnglishName(table, "碘")
    # result_with_only_latin_or_english_name += "\n"
    #
    # print(result_with_only_latin_or_english_name)
    #
    # with open("PeriodicTableWithOnlyLatinOrEnglishName.txt", "wb") as f:
    #     f.write(result_with_only_latin_or_english_name.encode(encoding="utf-8"))

    result = ""

    for i in range(0, 5):
        result += Element(table[i])
    result += "\n"

    for i in range(5, 10):
        result += Element(table[i])
    result += "\n"

    for i in range(10, 15):
        result += Element(table[i])
    result += "\n"

    for i in range(15, 20):
        result += Element(table[i])
    result += "\n"

    result += SearchOnTable(table, "金")
    result += SearchOnTable(table, "银")
    result += SearchOnTable(table, "铜")
    result += SearchOnTable(table, "铁")
    result += SearchOnTable(table, "锌")
    result += "\n"

    result += SearchOnTable(table, "钡")
    result += SearchOnTable(table, "铂")
    result += SearchOnTable(table, "锰")
    result += SearchOnTable(table, "汞")
    result += SearchOnTable(table, "碘")
    result += "\n"

    print(result)

    with open("PeriodicTable.txt", "wb") as f:
        f.write(result.encode(encoding="utf-8"))

