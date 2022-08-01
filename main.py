def calculate_change():
    available_money = [20, 20, 50, 5, 5, 100]
    ticket_price = int(input("Ticket price ?:"))
    payment = int(input("Payment ?:"))
    change = payment - ticket_price
    available_money.sort()
    available_money.reverse()
    change_money = calculate_money(change, available_money.copy())
    total_change = sum(change_money)
    if total_change == change:
        print("change: ", change, "\nmoneys: ", change_money)
    else:
        print("Not enough change, available moneys: ", available_money)


def calculate_money(amount, moneys):
    result = []
    for m in moneys:
        if amount >= m:
            result.append(m)
            break
    if len(result) > 0:
        amount = amount - result[0]
        moneys.remove(result[0])
        _result = calculate_money(amount, moneys)
        result = result + _result
        return result
    else:
        return []


if __name__ == '__main__':
    continue_ = 1
    while continue_ == 1:
        calculate_change()
        continue_ = int(input("Repeat ? 1/0:"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
