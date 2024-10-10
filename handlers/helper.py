
class Helper:
    def year_declension(year):
        if year % 10 == 1 and year % 100 != 11:
            return f"{year} рік"
        elif 2 <= year % 10 <= 4 and not (12 <= year % 100 <= 14):
            return f"{year} роки"
        else:
            return f"{year} років"
        
    def month_declension(month):
        if not (-1 < month < 13): raise  Exception("Місяць має бути вказаний в діапазоні від 0 до 12")
        if month == 1:
            return f"{month} місяць"
        elif 2 <= month <= 4:
            return f"{month} місяці"
        else:
            return f"{month} місяців"