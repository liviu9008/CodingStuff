def isMyTicketLucky(ticketNumber):
    total1 = 0
    total2 = 0

    if not ticketNumber.isnumeric():
        return "Insert only numbers"

    if type(ticketNumber) is list:
        return "Insert only numbers"

    if len(ticketNumber) < 6 or len(ticketNumber) > 6:
        return "Insert a number with 6 characters"
    else:
        first_half = ticketNumber[:3]
        for i in first_half:
            total1 += int(i)
        second_half = ticketNumber[3:6]
        for i in second_half:
            total2 += int(i)
    return total1 == total2


print(isMyTicketLucky("123456"))  # false
print(isMyTicketLucky("123321"))  # true
print(isMyTicketLucky(""))  # "Insert a number with at least 6 characters"
print(isMyTicketLucky("1234567"))  # ""Insert a number with only 6 characters"
print(isMyTicketLucky("[123456]"))  # "Insert only numbers"
print(isMyTicketLucky("test_number"))  # "Insert only numbers"

# Dragan and Jovana
