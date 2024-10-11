import numpy as np

# Simulated price data
price_data = [100.0, 101.0, 102.5, 101.8, 100.5, 99.7, 98.0, 97.5, 96.5, 97.2]

def generate_signals(price_data):
    signals = []
    for i in range(1, len(price_data)):
        if price_data[i] > price_data[i - 1]:
            signals.append(1)  # Buy signal
        else:
            signals.append(0)  # Sell signal
    return signals

def binary_options_trading(signals):
    capital = 1000  # Initial capital in dollars
    position_size = 100  # Number of binary options contracts to buy/sell
    payout = 85  # Payout percentage on a successful trade

    for i in range(len(signals)):
        if signals[i] == 1:
            # Buy a binary option for the next period
            capital -= position_size  # Deduct the cost of the option
            if np.random.uniform(0, 1) < 0.5:  # Simulated random chance of success
                capital += position_size * (payout / 100)  # Add profit on success
        elif signals[i] == 0:
            # Sell a binary option for the next period
            capital -= position_size  # Deduct the cost of the option
            if np.random.uniform(0, 1) < 0.5:  # Simulated random chance of success
                capital += position_size * (payout / 100)  # Add profit on success

    return capital

if __name__ == "__main__":
    signals = generate_signals(price_data)
    final_capital = binary_options_trading(signals)
    print(f"Final capital: ${final_capital:.2f}")
