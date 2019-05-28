import pandas as pd


def budget_info():
    """Aplikacja ma za zadanie pobierać dane o wydatkach z pliku tekstowego"""

    budget = pd.read_csv('./Oplata.csv', sep=";")
    budget.drop(columns=['Data waluty', 'Waluta'], inplace=True)
    return budget


def pay_card_deb():
    """Aplikacja ma za zadanie wyodrębnić z danych o wydatkach płatność kartą"""

    payment = budget_info()
    pay_card = payment[payment['Typ transakcji'] == 'Płatność kartą']
    pay_card['Lokalizacja'] = pay_card['Lokalizacja'].str.lower()
    pay_card = pay_card.dropna(how='all', axis='columns')

    pay_card.to_csv('platnosc_karta.csv')
    return pay_card


if __name__ == "__main__":
    pay_card_deb()


