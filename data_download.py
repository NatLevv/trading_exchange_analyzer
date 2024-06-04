import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(df):    #задача1.Расчет и вывод сред.ц. закр.акц.в опред.периоде

    average_price = df['Close'].mean()
    print(f"Средняя цена закрытия акций за заданный период.: {average_price}")

def notify_if_strong_fluctuations(df, threshold):
    max_price = df['Close'].max()
    min_price = df['Close'].min()
    price_difference = max_price - min_price
    relative_difference = (price_difference / ((max_price + min_price) / 2)) * 100

    if relative_difference > threshold:
        print(f"Уведомление: Цена акций колебалась на {relative_difference:.2f}% за заданный период.")

def export_data_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Данные сохранены в файл {filename}")
