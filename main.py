import requests

def evaluatePrice(item, response):
    latestClose = float(response['c'][0])
    todaysHigh = float(response['h'][0])
    dailyHigh = float(response['h'][1])

    if todaysHigh > dailyHigh:
        highDifferenceFloat = dailyHigh - todaysHigh
    else:
        highDifferenceFloat = todaysHigh - dailyHigh


    highDifferencePercentage = '{:.2%}'.format(highDifferenceFloat/dailyHigh)

    if latestClose > todaysHigh:
        closeDifferenceToTodaysHighFloat = todaysHigh - latestClose
    else:
        closeDifferenceToTodaysHighFloat = latestClose - todaysHigh

    closeDifferenceToTodaysHighPercentageFloat = closeDifferenceToTodaysHighFloat/todaysHigh
    closeDifferenceToTodaysHighPercentageString = '{:.2%}'.format(closeDifferenceToTodaysHighFloat/todaysHigh)

    if latestClose > dailyHigh:
        closeDifferenceToDailyHighFloat = dailyHigh - latestClose
    else:
        closeDifferenceToDailyHighFloat = latestClose - dailyHigh

    closeDifferenceToDailyHighPercentageFloat = closeDifferenceToDailyHighFloat/todaysHigh
    closeDifferenceToDailyHighPercentageString = '{:.2%}'.format(closeDifferenceToDailyHighFloat/dailyHigh)

    print(f'Pair: {item}')
    print(f'Current price: {latestClose}')
    print(f'Todays high: {todaysHigh}')
    print(f'Last 24h high: {dailyHigh}')

    if todaysHigh > dailyHigh:
        print(f'Todays high is {highDifferencePercentage} higher than 24h high')
    if todaysHigh == dailyHigh:
        print(f'Todays high is ATH')
    else:
        print(f'Todays high is {highDifferencePercentage} lower than 24h high')

    if latestClose > todaysHigh:
        print(f'Latest price is {closeDifferenceToTodaysHighPercentageString} higher than todays high')
    else:
        print(f'Latest price is {closeDifferenceToTodaysHighPercentageString} lower than todays high')

    if latestClose > dailyHigh:
        print(f'Latest price is {closeDifferenceToDailyHighPercentageString} higher than daily high')
    else:
        print(f'Latest price is {closeDifferenceToDailyHighPercentageString} lower than 24h high')

    if (closeDifferenceToDailyHighPercentageFloat * -1) >= 0.10:
        print('Recommendation: BUY')
    else:
        print('Recommendation: WAIT')
    print('')

r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTEUR,ETHEUR,DOTEUR,ADAEUR,SNXEUR,GRTEUR')
rawResponse = r.json()
# rawResponse = {"error":[],"result":{"XXBTZEUR":{"a":["37169.00000","3","3.000"],"b":["37168.90000","1","1.000"],"c":["37169.00000","0.00123082"],"v":["6152.77661756","7389.20542912"],"p":["37693.58863","37879.44235"],"t":[72745,89238],"l":["36038.10000","36038.10000"],"h":["39094.50000","39242.50000"],"o":"38386.20000"}}}
response = rawResponse['result']['XXBTZEUR']
for item in rawResponse['result']:
    evaluatePrice(item, rawResponse['result'][item])