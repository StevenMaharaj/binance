for VAR in $(ls /home/steve/freqtrade/user_data/data/binance | grep 5m)
do
    cp /home/steve/freqtrade/user_data/data/binance/$VAR $VAR
done
