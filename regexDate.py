import re
def regex(date):
    return re.search("(20|21|22|23)\d{2}-(0[1-9]\1[0-2])-(0[1-9]|[12][0-9]|3[01])",date) #yyyy-mm-dd
date = "2021-10-4"
print(regex(date))