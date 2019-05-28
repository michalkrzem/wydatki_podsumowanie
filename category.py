import account
import pandas as pd
import matplotlib.pyplot as plt

# Deklarowanie zmiennych wzskazujących na miejsce płatności kartą
grocery_store = 'biedronka|top market|carrefour|mieso|zabka|delikatesy|cukiernia|pajda|spolem|piotr'
petrol_station = 'orlen|lotos|bp'
repair_shop = 'leroy|castorama|obi'
mac = 'mcdonalds'
pharmacy = 'apteka'

# Pobieranie danych o płatności kartą
payment_card = account.pay_card_deb()


def schema(kind):
    """Funkcja ma za zadanie zagregować dane dla poszczególnych miejsc płatności kartą
    do rozdzielczości dziennej, miesięcznej i rocznej. Następnie wyniki bedą zobrazowane na wykresach"""

    what_kind = payment_card['Lokalizacja'].str.contains(kind)  # Wyodrębniamy poszczególne miejsca płatności
    payment_for_kind = payment_card[what_kind]
    payment_for_kind['Kwota'] *= (-1)  # Zmieniamy wartości płatności z "-" na "+"

    payment_for_kind["Data operacji"] = pd.to_datetime(payment_for_kind["Data operacji"])
    payment_for_kind['Miesiac'] = payment_for_kind['Data operacji'].dt.month  # Dodajemy dodatkowe kolumny
    payment_for_kind['Dzien'] = payment_for_kind['Data operacji'].dt.day
    payment_for_kind['Rok'] = payment_for_kind['Data operacji'].dt.year

    fig, (days, months, year) = plt.subplots(1, 3, figsize=(15, 6))  # Tworzymy obszar wykresu
    fig.suptitle('Wydatki na ' + kind, fontsize=14)
    plt.style.use('seaborn-pastel')

    group_day = payment_for_kind.groupby(by=['Rok', 'Miesiac', 'Dzien'])  # Wykonujemy agregacje - dzienne
    group_day['Kwota'].sum().plot(ax=days, kind='line', x=None, title='W ciągu dnia', rot=45, fontsize=9)
    group_month = payment_for_kind.groupby(by=['Rok', 'Miesiac'])  # Wykonujemy agregacje - miesięczne
    group_month['Kwota'].sum().plot(ax=months, kind='bar', title='W ciągu miesiąca', rot=45, fontsize=9)
    group_year = payment_for_kind.groupby('Rok')  # Wykonujemy agregacje - roczne
    group_year['Kwota'].sum().plot(ax=year, kind='bar', title='W ciągu roku', rot=45, fontsize=9)

    plt.show()  # Wyświetlamy wykres

    return payment_for_kind  # Zwracamy wartości płatności
                             # za rodzaj produktu


schema(grocery_store)  # Wywołujemy funkcję schema dla poszczególnych miejsc płatności kartą
schema(petrol_station)
schema(repair_shop)
schema(mac)
schema(pharmacy)
