import requests
import json
from config import *  # файл с токеном


class ConvertionExeption(Exception):
    pass


class Converter:
    @staticmethod
    def convert(sym: str, base: str, amount: str):

        if sym == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валютыю')

        try:
            sym_ticker = keys[sym]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {sym}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/fixer/convert?to={sym_ticker}&from={base_ticker}&amount={amount}"
        headers = {"apikey": "2TMuBgqhX0MMIFAUgrjoChLit9QossM2"}
        response = requests.request("GET", url, headers=headers)
        res = json.loads(response.content)['result']
        return res
