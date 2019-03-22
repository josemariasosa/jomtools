## Double Mask for Pandas :)

email = [x == row['email'] for x in pending['email']]
price = [x == row['total_price'] for x in pending['total_price']]
mask = pd.Series([a and b for a, b in zip(email, price)])
