def get_StochasticOscilator(df, periodK, smoothK, periodD):
    # Calculate %K
    df['%K'] = (df['close'] - df['low'].rolling(window=periodK).min()) / (
        df['high'].rolling(window=periodK).max() - df['low'].rolling(window=periodK).min()
    ) * 100
    df['%K'] = df['%K'].rolling(window=smoothK).mean()
    df['%D'] = df['%K'].rolling(window=periodD).mean()
if __name__ == '__main__':
    f = open("documents/data.txt", "r")
    data = f.readlines()
    data = eval(data[0])
    f.close()
    data = formatDataset(data) # Turns dataset into pandas dataset
    get_StochasticOscilator(data, 14, 3, 3)
    print(data['%K'], data['%D'])
