def exchange():
    usd_vs_rmb = 7.15

    currenct_value = input('How much money you want to exchange: ')

    if currenct_value[0] == '$':
        RMB = int(currenct_value[1:]) * usd_vs_rmb
        print("USD to RMB is: %.2f" % RMB)
    elif currenct_value[0] == '¥':
        USD = int(currenct_value[1:]) / usd_vs_rmb
        print("USD to AUD is: %.2f" % USD)
    else:
        print("Wrong format")

if __name__ == "__main__":
    exchange()
