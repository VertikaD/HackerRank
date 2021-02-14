# code by Vertika Dhingra.
def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse=True)
    # converting list into dictionary and calculating frequency of each candle.
    candles_frequency = {}
    for i in candles:
        if i in candles_frequency:
            # if a candle is already present in the dictionary , increment its                          freqeuncy by 1.
            candles_frequency[i] += 1
        else:  # else set its frequency to 1 and store in dictionary.
            candles_frequency[i] = 1

    # returns tuples containing key(candle) and value(frequncy).
    candles_frequency_tuple = candles_frequency.items()
    c = list(candles_frequency_tuple)  # returns list of tuples.

    candles_frequency_list = [list(x) for x in candles_frequency_tuple]
    return candles_frequency_list[0][1]  # number of candles that are tallest.
