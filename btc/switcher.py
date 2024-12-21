from bitcoinlib.wallets import Wallet

passphrase = "pride about ten indoor sweet moral scrap danger unique abstract virtual adapt"

try:
    w = Wallet.create("capyboss", keys=passphrase, network='bitcoin')
    print("Wallet created successfully.")
except Exception as e:
    print("Error creating wallet:", e)