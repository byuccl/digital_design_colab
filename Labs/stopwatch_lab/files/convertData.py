# @title vcd2dataframe
def vcd2dataframe(vcd_file):
    with open(vcd_file, "r") as f:
        # Remove Date, Program and  Timescale
        for i in range(20):
            line = f.readline()
            words = line.split()
            try:
                words[0]
            except:
                line = f.readline()
                words = line.split()
                continue
            if (
                words[0] == "$date"
                or words[0] == "$timescale"
                or words[0] == "$version"
            ):
                for i in range(10):
                    line = f.readline()
                    words = line.split()
                    if words[0] == "$end" or words[-1] == "$end":
                        break
            else:
                break
            line = f.readline()
        # Create the dictionary of lists for inputs
        signals = {}
        line = f.readline()
        words = line.split()
        symbols = {}
        for i in range(50):
            try:
                words[0]
            except:
                line = f.readline()
                words = line.split()
                continue
            if words[0] == "$var":
                signals[words[4]] = []
                symbols[words[3]] = words[4]

            elif words[0] == "$enddefinitions":
                break
            line = f.readline()
            words = line.split()
        # print(signals)
        # print(symbols)
        k = 0

        value = 0
        for i in range(0, 13000):
            if not words:
                line = f.readline()
                words = line.split()
                continue
            elif words[0] == "$dumpvars":
                line = f.readline()
                words = line.split()
                for i in range(50):
                    if words[0] == "$end":
                        break
                    else:
                        lines = f.readline()
                        words = line.split()

            elif len(words) > 1:
                if words[0][0] == "b":
                    # print(line)
                    if words[0][1] == "x":
                        value = 0
                    else:
                        try:
                            value = int(words[0][1:], 2)

                        except:
                            value = int(words[0][1], 2)
                    symbol = words[1]
                    signals[symbols[symbol]].append(value)
            elif words[0][0] == "#" and words[0][0] != "0":
                k = k + 1
                for key in signals:
                    if len(signals[key]) < k:
                        try:
                            signals[key].append(signals[key][-1])
                        except:
                            signals[key].append(0)
            else:
                if words[0][0] == "x":
                    value = 0
                else:
                    value = int(words[0][0:-1])
                symbol = words[0][-1]
                signals[symbols[words[0][-1]]].append(value)
            line = f.readline()
            words = line.split()
        length_df = 0
        dataframe = signals
        for i in dataframe:
            if length_df < len(dataframe[i]):
                length_df = len(dataframe[i])
            # print(length_df)
        for i in dataframe:
            if len(dataframe[i]) < length_df:
                dataframe[i].append(dataframe[i][-1])
    return dataframe
    # print(signals)
    # Create a list of variables and their names (ignore types)
    # Create a key to translate the signals
    # Begin Cycling through the signals


# @title dataframe to wavedrom
def df2wd(filename):
    dataframe = vcd2dataframe("/content/tmp_code/logs/vlt_dump.vcd")
    string_list = []
    name_list = []
    starting_value = 4
    for i in dataframe:
        value = ""
        value_str = ""
        last_value = ""
        for j in dataframe[i]:
            value_list = dataframe[i]
            if last_value == str(j):
                value = "."
            else:
                if int(j) > 2:
                    x = starting_value
                    starting_value += 1
                    if starting_value >= 9:
                        starting_value = 4
                    value = str(x)
                else:
                    value = str(j)
                last_value = str(j)
            value_str = value_str + value
        string_list.append(value_str)
        name_list.append(i)

    wavedrom_format = """{ signal : ["""
    for i in range(len(string_list)):
        if name_list[i] == "clk":
            new_line = (
                """{ name: "clk",  wave: "p"""
                + "." * (-1 + len(value_str))
                + """\", period: 2 },"""
                + f"\n"
            )
        elif max(dataframe[name_list[i]]) > 1:
            int_list = dataframe[name_list[i]]
            new_string_list = string_list[i]
            int_string = ""
            current_value = ""
            last_value = ""
            # Fix String List
            new_string_list = new_string_list.replace("0", "2")
            new_string_list = new_string_list.replace("1", "3")
            # Create a Data Set
            for j in int_list:
                current_value = j
                if current_value == last_value:
                    pass
                else:
                    int_string += str(current_value) + " "
                last_value = current_value
            new_line = (
                '{ name: "'
                + name_list[i]
                + """\",  wave: \""""
                + new_string_list
                + """\", data:\" """
                + int_string
                + """ \" },"""
                + f"\n"
            )
        else:
            new_line = (
                """{ name: \""""
                + name_list[i]
                + """ \",  wave: \""""
                + string_list[i]
                + """\" },"""
                + f"\n"
            )
        wavedrom_format += new_line
    wavedrom_format += """
    ]}
"""
    filename = "/content/tmp_code/" + filename + ".txt"
    with open(filename, "w") as f:
        f.write(wavedrom_format)
