def arithmetic_arranger(problems:list, answers:bool=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        tmpObj = {
            "top": [],
            "bottom": [],
            "-": [],
            "answers": []
        }
        arranged_problems = ""

        for problem in problems:
            top, f, bottom = tuple(problem.split())

            # Errors
            # invalid operants
            if f not in ["+", "-"]:
                return "Error: Operator must be '+' or '-'."
            
            # try on int parsing
            try:
                tmpInt = int(top)
                tmpInt = int(bottom)
                
                # more than 4 digits
                if len(top) > 4 or len(bottom) > 4:
                    return "Error: Numbers cannot be more than four digits."

            except:
                return "Error: Numbers must only contain digits."

            #
            _len = len(top) if len(top) >= len(bottom) else len(bottom)
            tmpObj["top"].append(f"  {' '*(_len-len(top))}{top}")
            tmpObj["bottom"].append(f"{f} {' '*(_len-len(bottom))}{bottom}")
            tmpObj["-"].append("-"*(_len+2))

            # answers
            if answers:
                ans = (int(top) + int(bottom)) if f == "+" else (int(top) - int(bottom))
                ansString = f"{' '*(_len-len(str(ans)))}{ans}"
                tmpObj["answers"].append(f"{' '*(2-len(ansString)+_len)}{ans}")

        arranged_problems = "    ".join(tmpObj["top"]) + "\n" + "    ".join(tmpObj["bottom"]) + "\n" + "    ".join(tmpObj["-"]) + (("\n" + "    ".join(tmpObj["answers"])) if answers else "")
        

        return arranged_problems

#print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))