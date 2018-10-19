'''
hacker rank

https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''


def birthdayCakeCandles(ar):
    
    max_data = max(ar)
    
    jumlah = 0
    for data in ar:
        
        if data == max_data:
            jumlah += 1
    
    return jumlah


if __name__ == '__main__':
    candle = [3, 2, 1, 3]
    birthdayCakeCandles(candle)