import requests
import time
from colorama import init, Fore, Style
import os
from dotenv import load_dotenv

load_dotenv()

#Токены для Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text, symbol=None, buy_exchange=None, sell_exchange=None):
    try:
        urls = {
            "binance": f"https://www.binance.com/en/trade/{symbol}",
            "bybit": f"https://www.bybit.com/trade/spot/{symbol}",
            "mexc": f"https://www.mexc.com/exchange/{symbol}",
            "okx": f"https://www.okx.com/trade-spot/{symbol}",
            "kucoin": f"https://www.kucoin.com/trade/{symbol}",
            "poloniex": f"https://poloniex.com/trade/{symbol}",
            "gate": f"https://www.gate.io/trade/{symbol}",
            "coinex": f"https://www.coinex.com/exchange/{symbol}",
            "xt": f"https://www.xt.com/en/trade/{symbol}",
            "coinw": f"https://www.coinw.com/frontSpot/trade/{symbol}",
            "bitget": f"https://www.bitget.com/spot/{symbol}_USDT",
            "bitmart": f"https://www.bitmart.com/trade/en?symbol={symbol}"
        }

        buttons = []
        if buy_exchange:
            buy_url = urls.get(buy_exchange.lower())
            if buy_url:
                buttons.append({
                    "text": f"🔴 Покупка: {buy_exchange.capitalize()}",
                    "url": buy_url
                })

        if sell_exchange:
            sell_url = urls.get(sell_exchange.lower())
            if sell_url:
                buttons.append({
                    "text": f"🟢 Продажа: {sell_exchange.capitalize()}",
                    "url": sell_url
                })

        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "HTML"
        }

        if buttons:
            payload["reply_markup"] = {
                "inline_keyboard": [buttons]
            }

        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json=payload, timeout=5)
    except Exception as e:
        print(f"⚠ Telegram error: {e}")

init(autoreset=False)  # отключаем авто-сброс цвета

PAIRS = [
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT",
    "VANAUSDT", "ADAUSDT", "TRXUSDT", "LTCUSDT",
    "APEXUSDT", "XRPUSDT", "MNTUSDT", "ONDOUSDT",
    "SUIUSDT", "PEPEUSDT", "UNIUSDT", "AAVEUSDT", "AVAXUSDT",
    "APEUSDT", "AVAUSDT", "ATOMUSDT", "BCHUSDT", "SPXUSDT",
    "TONUSDT", "DOGEUSDT", "SHIBUSDT", "APTUSDT", "ARBUSDT",
    "OPUSDT", "DOTUSDT", "USDCUSDT",
    "LINKUSDT", "DOTUSDT", "NEARUSDT", "FLOKIUSDT",
    "TIMEUSDT", "PPTUSDT", "XECUSDT", "SCRTUSDT",
    "QTUMUSDT", "ARBUSDT", "DAIUSDT",
    # Пары с USDC (Bybit также поддерживает USDC-квоты)
    "LINKUSDC", "AVAXUSDC", "PEPEUSDC", "WIFUSDT",
    "BONKUSDT", "TONUSDC", "NOTUSDC", 
"LINKUSDT", "NEARUSDT", "TIMEUSDT", "FETUSDT",
    "MATICUSDT", "CHZUSDT", "ICPUSDT", "RUNEUSDT",
    "TAOUSDT", "QTUMUSDT", "SCRTUSDT", "XECUSDT",
    "CAKEUSDT", "EOSUSDT", "NEOUSDT", "1INCHUSDT",
    "SUSHIUSDT", "AXSUSDT", "GRTUSDT", "ALGOUSDT", "FETUSDT", "QTUMUSDT", 
    "FILUSDT", "1INCHUSDT", "SNXUSDT", "YFIUSDT", 
    "XTZUSDT", "ZRXUSDT", "MANAUSDT", "KAVAUSDT", 
    "AMPUSDT", "RENUSDT", "FLUXUSDT", "CELRUSDT",
    "CMPUSDT", "ALPHAUSDT", "MASKUSDT", "MKRUSDT",
    "GRTUSDT", "ALGOUSDT", "FILUSDT", "SNXUSDT", "YFIUSDT",
    "XTZUSDT", "ZRXUSDT", "MANAUSDT", "KAVAUSDT", "AMPUSDT",
    "RENUSDT", "FLUXUSDT", "CELRUSDT", "CMPUSDT", "ALPHAUSDT",
    "MASKUSDT", "MKRUSDT", "EOSUSDT", "NEOUSDT", "AXSUSDT",
    "BATUSDT", "BANDUSDT", "BADGERUSDT", "BAKEUSDT", "BALUSDT",
    "AUDIOUSDT", "BADGERUSDT", "LINKUSDT", "LTCUSDT", "BCHUSDT",
    "BADGERUSDT", "INJUSDT", "QNTUSDT", "ICXUSDT", "HBARUSDT",
    "MOVRUSDT", "CVXUSDT", "YGGUSDT", "COMPLUSDT", "ETCUSDT",
    "NEARUSDT", "ROSEUSDT", "CAKEUSDT", "EOSUSDT", "THETAUSDT",
    "POLYUSDT", "ANYUSDT", "JASMYUSDT", "PARTIUSDT", "MATICUSDT", "SKATEUSDT", "RESOLVUSDT", "HOMEUSDT", "CUDISUSDT",
"INJUSDT", "QNTUSDT", "HBARUSDT", "MOVRUSDT",
"CVXUSDT", "YGGUSDT", "COMPLUSDT", "ETCUSDT",
"ROSEUSDT", "THETAUSDT", "POLYUSDT", "ANYUSDT",
"JASMYUSDT", "PARTIUSDT",
"ZETAUSDT", "POPCATUSDT", "VIRTUALUSDT", "TRUMPUSDT",
"KASUSDT", "GRASSUSDT", "NXPCUSDT", "MKRUSDT",
"NEARUSDT", "ATHUSDT", "APTUSDT", "SUNDOGUSDT", "JTOUSDT",
"ZILUSDT", "RNDRUSDT", "LDOUSDT", "XLMUSDT", "GLMRUSDT",
"DYDXUSDT", "ENSUSDT", "CFXUSDT", "IOTXUSDT", "STGUSDT",
"IMXUSDT", "KAVAUSDT", "LRCUSDT", "GNOUSDT", "SXPUSDT",
"CHZUSDT", "CLVUSDT", "BLZUSDT", "CROUSDT", "CTSIUSDT",
"ANKRUSDT", "CELRUSDT", "DASHUSDT", "DGBUSDT", "DCRUSDT",
"FETUSDT", "GALAUSDT", "HNTUSDT", "KSMUSDT",
"MINAUSDT", "NKNUSDT", "OCEANUSDT", "RUNEUSDT",
"SKLUSDT", "SNXUSDT", "SOLUSDT", "STMXUSDT", "SUSHIUSDT",
"TORNUSDT", "TWTUSDT", "UMAUSDT", "VETUSDT", "WAVESUSDT",
"XEMUSDT", "XNOUSDT", "YFIUSDT", "ZRXUSDT",
"ALPHAUSDT", "MASKUSDT", "FLUXUSDT", "CMPUSDT", "AMPUSDT",
"MANAUSDT", "FILUSDT", "CAKEUSDT", "NEOUSDT", "1INCHUSDT",
"BATUSDT", "BANDUSDT", "BADGERUSDT", "BAKEUSDT", "BALUSDT",
"AUDIOUSDT", "ARBUSDT", "LINAUSDT", "GLMRUSDT", "QNTUSDT", "STMXUSDT",
"RNDRUSDT", "PEOPLEUSDT", "IMXUSDT", "MOVRUSDT", "WOOUSDT",
"ROSEUSDT", "PLAUSDT", "POLYUSDT", "GALAUSDT", "FETUSDT",
"GNOUSDT", "RLCUSDT", "NKNUSDT", "CKBUSDT", "SANDUSDT",
"CELOUSDT", "GRTUSDT", "DYDXUSDT", "LRCUSDT", "ENSUSDT",
"JASMYUSDT", "TWTUSDT", "MINAUSDT", "SPELLUSDT", "XEMUSDT",
"FXSUSDT", "HNTUSDT", "ANKRUSDT", "LUNA2USDT", "CTSIUSDT",
"MASKUSDT", "ROOKUSDT", "ALGOUSDT", "CELRUSDT", "1INCHUSDT",
"STORJUSDT", "GMTUSDT", "PEPEUSDT", "RUNEUSDT", "APTUSDT",
"GMTUSDT", "XECUSDT", "FLUXUSDT", "SXPUSDT", "OPUSDT",
"ZILUSDT", "CHZUSDT", "SRMUSDT", "KSMUSDT", "WAVESUSDT",
"BLZUSDT", "COMPUSDT", "CVXUSDT", "BNTUSDT", "NEARUSDT",
"ARBUSDT", "LUNAUSDT", "DYDXUSDT", "AUDIOUSDT", "QNTUSDT",
"TRUUSDT", "SRMUSDT", "ZRXUSDT", "OCEANUSDT", "MTLUSDT",
"XNOUSDT", "BADGERUSDT", "BAKEUSDT", "BALUSDT", "BADGERUSDT",
"FXSUSDT", "GTCUSDT", "CVXUSDT", "KNCUSDT", "BTRSTUSDT",
"GLMRUSDT", "CROUSDT", "NKNUSDT", "MOVRUSDT", "GALUSDT",
"QNTUSDT", "ANKRUSDT", "FLOWUSDT", "API3USDT", "PLAUSDT",
"API3USDT", "REIUSDT", "ROOKUSDT", "GALUSDT", "FXSUSDT",
"HOOKUSDT", "POLYUSDT", "MULTIUSDT", "FXSUSDT", "RLCUSDT",
"SKLUSDT", "INJUSDT", "MASKUSDT", "XNOUSDT", "XECUSDT",
"MINAUSDT", "IMXUSDT", "GLMRUSDT", "OCEANUSDT", "FLUXUSDT",
"REIUSDT", "SPELLUSDT", "STORJUSDT", "PEOPLEUSDT", "ALPHAUSDT",
"ALPHAUSDT", "MOVRUSDT", "CROUSDT", "WOOUSDT", "TWTUSDT",
"TRUUSDT", "SANDUSDT", "PLAUSDT", "RLCUSDT", "STORJUSDT",
"ROOKUSDT", "SXPUSDT", "JASMYUSDT", "GMTUSDT", "FETUSDT",
"NEARUSDT", "LINAUSDT", "CKBUSDT", "AUDIOUSDT", "ANKRUSDT",
"CHZUSDT", "BADGERUSDT", "SPELLUSDT", "CTSIUSDT", "BADGERUSDT",
"KSMUSDT", "BNTUSDT", "WAVESUSDT", "MTLUSDT", "BTRSTUSDT",
"SRMUSDT", "QNTUSDT", "GALAUSDT", "GTCUSDT", "COMPUSDT",
"CREAMUSDT", "DENTUSDT", "NMRUSDT", "RIFUSDT", "REQUSDT",
"DOCKUSDT", "MLNUSDT", "TOMOUSDT", "PERLUSDT", "POWRUSDT",
"MDTUSDT", "STRAXUSDT", "ARDRUSDT", "BURGERUSDT", "BELUSDT",
"WNXMUSDT", "DODOUSDT", "LITUSDT", "FORTHUSDT", "PONDUSDT",
"PSGUSDT", "ACMUSDT", "ASRUSDT", "CITYUSDT", "ATMUSDT",
"OGUSDT", "BARUSDT", "LAZIOUSDT", "VIBUSDT", "NULSUSDT",
"VITEUSDT", "TLMUSDT", "SUPERUSDT", "HIGHUSDT", "POLSUSDT",
"FARMUSDT", "QUICKUSDT", "IDEXUSDT", "UOSUSDT", "ORNUSDT",
"ALPACAUSDT", "XVSUSDT", "MDXUSDT", "AUTOUSDT", "TRBUSDT",
"RAMPUSDT", "LTOUSDT", "DEXEUSDT", "NBSUSDT", "AUCTIONUSDT",
"RAREUSDT", "RAYUSDT", "SLPUSDT", "ALCXUSDT", "DNTUSDT",
"ASTUSDT", "DATAUSDT", "ADXUSDT", "AGIXUSDT", "OXTUSDT",
"MITHUSDT", "TROYUSDT", "STMXUSDT", "CVCUSDT", "BNTUSDT",
"BEAMXUSDT", "BICOUSDT", "REIUSDT", "RLCUSDT", "EGLDUSDT",
"WNTRUSDT", "FIDAUSDT", "C98USDT", "ERNUSDT", "GODSUSDT",
"NFTUSDT", "ALICEUSDT", "RBNUSDT", "JOEUSDT", "SPELLUSDT",
"GMTUSDT", "PORTOUSDT", "VOXELUSDT", "MCUSDT", "PYRUSDT",
"DARUSDT", "GALUSDT", "BONDUSDT", "CLAYUSDT", "HOOKUSDT",
"STGUSDT", "LINAUSDT", "IDUSDT", "RDNTUSDT", "ACAUSDT",
"BICOUSDT", "AGLDUSDT", "XCNUSDT", "LOKAUSDT", "LEVERUSDT",
"GMXUSDT", "ASTRUSDT", "KDAUSDT", "ACHUSDT", "LOOMUSDT",
"SSVUSDT", "BANDUSDT", "TRUUSDT", "CKBUSDT", "WOOUSDT",
"ILVUSDT", "SYLUSDT", "MNUSDT", "MBLUSDT", "YGGUSDT",
"DFIUSDT", "BSWUSDT", "QIUSDT", "BLURUSDT", "JOEUSDT",
"RIFUSDT", "ANTUSDT", "NMRUSDT", "DREPUSDT", "DUSKUSDT",
"PHBUSDT", "UNFIUSDT", "CVPUSDT", "JASMYUSDT", "EWTUSDT",
"FISUSDT", "MOBUSDT", "KMDUSDT", "TVKUSDT", "GLMUSDT",
"XAUTUSDT", "STORJUSDT", "BMXUSDT", "XVGUSDT", "ARPAUSDT",
"ELFUSDT", "KLAYUSDT", "BAKEUSDT", "AMBUSDT", "NTRNUSDT",
"MTLUSDT", "PUNDIXUSDT", "PROSUSDT", "YFIIUSDT", "RLCUSDT"
]

EXCHANGES = {
    "binance": "https://api.binance.com/api/v3/ticker/bookTicker",
    "bybit": "https://api.bybit.com/v5/market/tickers?category=spot",
    "mexc": "https://api.mexc.com/api/v3/ticker/bookTicker",
    "okx": "https://www.okx.com/api/v5/market/tickers?instType=SPOT",
    "kucoin": "https://api.kucoin.com/api/v1/market/allTickers",
    "poloniex": "https://api.poloniex.com/markets/ticker24h",
    "gate": "https://data.gateapi.io/api2/1/tickers",
    "coinex": "https://api.coinex.com/v1/market/ticker/all",
    "xt": "https://sapi.xt.com/v4/public/ticker/book",
    "coinw": "https://api.coinw.com/api/v1/public/market/ticker",
    "bitget": "https://api.bitget.com/api/spot/v1/market/tickers",
    "bitmart": "https://api-cloud.bitmart.com/spot/quotation/ticker"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_binance():
    try:
        fee = 0.001  # комиссия 0.1%

        resp = requests.get(EXCHANGES["binance"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data:
            symbol = item['symbol']
            if symbol in PAIRS:
                bid = float(item['bidPrice'])
                ask = float(item['askPrice'])
                bid_qty = float(item['bidQty'])
                ask_qty = float(item['askQty'])

                # Учет комиссии
                effective_bid = bid * (1 - fee)  # меньше получим при продаже
                effective_ask = ask * (1 + fee)  # больше заплатим при покупке

                # Перевод в USDT
                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ Binance error: {e}")
        return {}

def fetch_bybit():
    try:
        fee = 0.001  # комиссия 0.1%

        resp = requests.get(EXCHANGES["bybit"], timeout=5, headers=HEADERS)
        data = resp.json()
        
        # DEBUG вывод
        if "result" not in data or "list" not in data["result"]:
            print("⚠ Структура Bybit изменилась или пустая:", data)
            return {}
        
        prices = {}
        for item in data["result"]["list"]:
            symbol = item.get("symbol") or item.get("s")
            if symbol in PAIRS:
                bid = float(item["bid1Price"])
                ask = float(item["ask1Price"])
                bid_qty = float(item["bid1Size"])
                ask_qty = float(item["ask1Size"])

                # Учет комиссии
                effective_bid = bid * (1 - fee)  # меньше при продаже
                effective_ask = ask * (1 + fee)  # дороже при покупке

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ Bybit error: {e}")
        return {}

def fetch_mexc():
    try:
        fee = 0.001  # комиссия 0.1%

        resp = requests.get(EXCHANGES["mexc"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data:
            symbol = item['symbol']
            if symbol in PAIRS:
                bid = float(item['bidPrice'])
                ask = float(item['askPrice'])
                bid_qty = float(item['bidQty'])
                ask_qty = float(item['askQty'])

                # Учет комиссии
                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ MEXC error: {e}")
        return {}

def fetch_okx():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["okx"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data['data']:
            symbol = item['instId']
            if symbol in PAIRS:
                bid = float(item['bidPx'])
                ask = float(item['askPx'])
                bid_qty = float(item['bidSz'])
                ask_qty = float(item['askSz'])

                # Учет комиссии
                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ OKX error: {e}")
        return {}

def fetch_kucoin():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["kucoin"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data['data']['ticker']:
            symbol = item['symbol']
            if symbol in PAIRS:
                bid = float(item['buy'])
                ask = float(item['sell'])
                bid_qty = float(item.get('buySize', 0))
                ask_qty = float(item.get('sellSize', 0))

                # Учет комиссии
                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ KuCoin error: {e}")
        return {}
       
def fetch_poloniex():
    try:
        fee = 0.001  # комиссия 0.1%
        url = "https://api.poloniex.com/markets/ticker24h"
        resp = requests.get(url, timeout=5, headers=HEADERS)
        data = resp.json()

        if not isinstance(data, list):
            print(f"⚠ Poloniex: неожиданный формат данных: {data}")
            return {}

        prices = {}
        for item in data:
            market = item.get("symbol")  # например: "BTC_USDT"
            if not market:
                continue

            # Приводим к стандартному формату: "BTCUSDT"
            symbol = market.replace("_", "")

            if symbol in PAIRS:
                bid = float(item["bid"])
                ask = float(item["ask"])
                bid_qty = float(item.get("baseVolume", 0))
                ask_qty = float(item.get("baseVolume", 0))

                # Учет комиссии
                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }

        return prices

    except Exception as e:
        print(f"⚠ Poloniex error: {e}")
        return {}

def fetch_gate():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["gate"], timeout=5, headers=HEADERS)
        data = resp.json()
        if not isinstance(data, list):
            data = data.get("data", [])

        prices = {}
        for item in data:
            symbol = item["currency_pair"].replace("_", "").upper()
            if symbol in PAIRS:
                bid = float(item["highest_bid"])
                ask = float(item["lowest_ask"])

                bid_qty = float(item.get("base_volume", 0)) / bid if bid > 0 else 0
                ask_qty = float(item.get("base_volume", 0)) / ask if ask > 0 else 0

                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": round(bid_qty, 4),
                    "ask_volume": round(ask_qty, 4),
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ Gate.io error: {e}")
        return {}

def fetch_coinex():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["coinex"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for symbol, item in data["data"].items():
            normalized_symbol = symbol.replace("_", "").upper()  # нормализация в формат без подчёркивания
            if normalized_symbol in PAIRS:
                bid = float(item["bid"][0])
                ask = float(item["ask"][0])
                bid_qty = float(item["bid"][1])
                ask_qty = float(item["ask"][1])

                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[normalized_symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ CoinEx error: {e}")
        return {}
        
def fetch_xt():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["xt"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data.get('result', []):
            symbol = item['s'].upper()
            if symbol in PAIRS:
                bid = float(item['bp'])
                ask = float(item['ap'])
                bid_qty = float(item['bv'])
                ask_qty = float(item['av'])

                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ XT error: {e}")
        return {}
        
def fetch_coinw():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["coinw"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data.get("data", []):
            symbol = item['symbol'].replace("_", "").upper()
            if symbol in PAIRS:
                bid = float(item['buy'])
                ask = float(item['sell'])
                bid_qty = float(item['buy_amount'])
                ask_qty = float(item['sell_amount'])

                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ CoinW error: {e}")
        return {}
        
def fetch_bitget():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["bitget"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data.get("data", []):
            symbol = item["symbol"].replace("-", "").upper()
            if symbol in PAIRS:
                bid = float(item["buyOne"])
                ask = float(item["sellOne"])
                quote_volume = float(item.get("quoteVolume", 0))

                # считаем эффективные цены с комиссией
                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                # пересчитываем объёмы в базовой валюте, избегая деления на 0
                bid_qty = quote_volume / bid if bid > 0 else 0
                ask_qty = quote_volume / ask if ask > 0 else 0

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": round(bid_qty, 4),
                    "ask_volume": round(ask_qty, 4),
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ Bitget error: {e}")
        return {}
        
def fetch_bitmart():
    try:
        fee = 0.001  # комиссия 0.1%
        resp = requests.get(EXCHANGES["bitmart"], timeout=5, headers=HEADERS)
        data = resp.json()
        prices = {}
        for item in data.get("data", {}).get("tickers", []):
            symbol = item["symbol"].replace("_", "").upper()
            if symbol in PAIRS:
                bid = float(item["best_bid"])
                ask = float(item["best_ask"])
                bid_qty = float(item.get("bid_size", 0))
                ask_qty = float(item.get("ask_size", 0))

                effective_bid = bid * (1 - fee)
                effective_ask = ask * (1 + fee)

                max_sell_usdt = effective_bid * bid_qty
                max_buy_usdt = effective_ask * ask_qty

                prices[symbol] = {
                    "bid": bid,
                    "ask": ask,
                    "effective_bid": round(effective_bid, 6),
                    "effective_ask": round(effective_ask, 6),
                    "bid_volume": bid_qty,
                    "ask_volume": ask_qty,
                    "max_sell_usdt": round(max_sell_usdt, 2),
                    "max_buy_usdt": round(max_buy_usdt, 2)
                }
        return prices
    except Exception as e:
        print(f"⚠ BitMart error: {e}")
        return {}

def gather_all_prices():
    all_prices = {}

    binance = fetch_binance()
    bybit = fetch_bybit()
    mexc = fetch_mexc()
    okx = fetch_okx()
    kucoin = fetch_kucoin()
    poloniex = fetch_poloniex()
    gate = fetch_gate()
    coinex = fetch_coinex()
    xt = fetch_xt()
    coinw = fetch_coinw()
    bitget = fetch_bitget()
    bitmart = fetch_bitmart()

    exchanges_prices = {
        "BINANCE": binance,
        "BYBIT": bybit,
        "MEXC": mexc,
        "OKX": okx,
        "KUCOIN": kucoin,
        "POLONIEX": poloniex,
        "GATE": gate,
        "COINEX": coinex,
        "XT": xt,
        "COINW": coinw,
        "BITGET": bitget,
        "BITMART": bitmart
    }

    for symbol in PAIRS:
        all_prices[symbol] = {}
        for ex_name, ex_prices in exchanges_prices.items():
            if symbol in ex_prices:
                all_prices[symbol][ex_name] = ex_prices[symbol]

    return all_prices

sent_signals = set()

def calculate_real_profit(symbol, buy_ex, sell_ex, trade_usdt, buy_price, sell_price):
    # Комиссия спота (%)
    spot_fee = {
        "binance": 0.1,
        "bybit": 0.1,
        "mexc": 0.1,
        "okx": 0.1,
        "kucoin": 0.1,
        "poloniex": 0.1,
        "gate": 0.2,
        "coinex": 0.2,
        "xt": 0.2,
        "coinw": 0.2,
        "bitget": 0.1,
        "bitmart": 0.2
    }

    # Комиссия вывода (USDT, ориентировочно)
    withdraw_fee = {
        "binance": 1,
        "bybit": 1,
        "mexc": 1,
        "okx": 1,
        "kucoin": 1,
        "poloniex": 1,
        "gate": 1,
        "coinex": 1,
        "xt": 1,
        "coinw": 1,
        "bitget": 1,
        "bitmart": 1
    }

    # Объём в монете
    amount = trade_usdt / buy_price
    buy_fee = amount * buy_price * (spot_fee.get(buy_ex, 0.1) / 100)
    sell_fee = amount * sell_price * (spot_fee.get(sell_ex, 0.1) / 100)
    total_fees = buy_fee + sell_fee + withdraw_fee.get(buy_ex, 1)

    revenue = amount * sell_price
    real_profit = revenue - trade_usdt - total_fees
    real_spread = (real_profit / trade_usdt) * 100 if trade_usdt else 0

    return {
        "real_profit": round(real_profit, 2),
        "real_spread": round(real_spread, 2),
        "total_fees": round(total_fees, 2)
    }

def find_opportunities(all_prices):
    opportunities = []
    for symbol, ex_data in all_prices.items():
        exchanges = list(ex_data.keys())
        for i in range(len(exchanges)):
            for j in range(len(exchanges)):
                if i == j:
                    continue
                buy_ex = exchanges[i]
                sell_ex = exchanges[j]
                buy_info = ex_data[buy_ex]
                sell_info = ex_data[sell_ex]

                buy_price = buy_info["ask"]
                sell_price = sell_info["bid"]
                if buy_price == 0 or sell_price == 0:
                    continue

                max_buy_usdt = buy_info.get("max_buy_usdt", 0)
                max_sell_usdt = sell_info.get("max_sell_usdt", 0)
                trade_usdt = min(max_buy_usdt, max_sell_usdt)

                if trade_usdt == 0:
                    continue

                amount_in_coin = trade_usdt / buy_price
                usdt_after_sell = amount_in_coin * sell_price
                gross_profit = usdt_after_sell - trade_usdt
                gross_spread = (gross_profit / trade_usdt) * 100

                # Комиссии
                spot_fee = trade_usdt * 0.001 + usdt_after_sell * 0.001
                withdraw_fee = 1.5  # фиксированная комиссия перевода
                total_fee = spot_fee + withdraw_fee

                net_profit = gross_profit - total_fee
                net_spread = (net_profit / trade_usdt) * 100

                signal_key = f"{symbol}_{buy_ex}_{sell_ex}_{round(net_spread, 2)}"

                if 0.1 <= net_spread <= 10 and signal_key not in sent_signals:
                    message = (
                        f"📌 {symbol}\n"
                        f"Spread: +{net_spread:.2f}%\n\n"
                        f"[{buy_ex}]🔴 Ask: {buy_price:.4f} (Vol: ${max_buy_usdt:.0f})\n"
                        f"[{sell_ex}]🟢 Bid: {sell_price:.4f} (Vol: ${max_sell_usdt:.0f})\n\n"
                        f"💧 Liquidity: ${trade_usdt:.2f}\n"
                        f"💰 Fees: ${total_fee:.2f}\n"
                        f"📈 Прибыль: ${net_profit:.2f} ({net_spread:.2f}%)"
                    )
                    send_telegram_message(message, symbol, buy_ex, sell_ex)
                    sent_signals.add(signal_key)

                opportunities.append({
                    "symbol": symbol,
                    "buy": buy_ex,
                    "sell": sell_ex,
                    "buy_price": buy_price,
                    "sell_price": sell_price,
                    "profit_usdt": round(net_profit, 4),
                    "spread": round(net_spread, 4),
                    "volume_usdt": round(trade_usdt, 2)
                })
    return opportunities

def animated_print(text, delay=0.0005):
    color_codes = ""
    rest_text = text
    if text.startswith('\033['):
        end_idx = text.find('m') + 1
        color_codes = text[:end_idx]
        rest_text = text[end_idx:]
    
    print(color_codes, end="", flush=True)
    for char in rest_text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def print_opportunities(opportunities):
    if not opportunities:
        animated_print(Fore.MAGENTA + "⚠ Нет прибыльных маршрутов.")
        return

    opportunities = sorted(opportunities, key=lambda x: x["spread"], reverse=True)[:10]

    animated_print(Fore.MAGENTA + "\n📊 Топ-10 прибыльных маршрутов:\n")

    for op in opportunities:
        symbol = op['symbol']
        buy = op['buy']
        sell = op['sell']
        buy_price = op['buy_price']
        sell_price = op['sell_price']
        profit = op['profit_usdt']
        spread = op['spread']
        volume = op['volume_usdt']

        # Цветовая разметка по спреду
        if spread >= 0.5:
            color = Fore.GREEN
        elif 0 < spread < 0.5:
            color = Fore.YELLOW
        else:
            color = Fore.RED

        animated_print(color + f"{symbol}:")
        animated_print(Fore.CYAN + f"  ▸ BUY: {buy} по {buy_price:.6f}")
        animated_print(Fore.CYAN + f"  ▸ SELL: {sell} по {sell_price:.6f}")
        animated_print(Fore.LIGHTBLUE_EX + f"  ▸ VOLUME: {volume:.2f} USDT")
        animated_print(color + f"  ▸ Прибыль: +{profit:.4f} USDT")
        animated_print(color + f"  ▸ Спред: {spread:.4f}%\n")

def main():
    animated_print(Fore.GREEN + "📡 Межбиржевой арбитраж по выбранным парам:\n")
    while True:
        all_prices = gather_all_prices()
        if all_prices:
            opportunities = find_opportunities(all_prices)
            print_opportunities(opportunities)
        else:
            animated_print(Fore.MAGENTA + "⚠ Не удалось получить данные с бирж.")

        animated_print(Fore.GREEN + "\n🔄 Обновление через 10 секунд...\n" + "-" * 80)
        time.sleep(10)

if __name__ == "__main__":
    main()
