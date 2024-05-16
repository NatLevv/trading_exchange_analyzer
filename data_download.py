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