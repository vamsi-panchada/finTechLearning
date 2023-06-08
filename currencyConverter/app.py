import streamlit as st
import requests

country_codes = {
    "Afghan Afghani": "AFN",
    "Albanian Lek": "ALL",
    "Algerian Dinar": "DZD",
    "Angolan Kwanza": "AOA",
    "Argentine Peso": "ARS",
    "Armenian Dram": "AMD",
    "Aruban Florin": "AWG",
    "Australian Dollar": "AUD",
    "Azerbaijani Manat": "AZN",
    "Bahamian Dollar": "BSD",
    "Bahraini Dinar": "BHD",
    "Bangladeshi Taka": "BDT",
    "Barbados Dollar": "BBD",
    "Belarusian Ruble": "BYN",
    "Belize Dollar": "BZD",
    "Bermudian Dollar": "BMD",
    "Bhutanese Ngultrum": "BTN",
    "Bolivian Boliviano": "BOB",
    "Bosnia and Herzegovina Convertible Mark": "BAM",
    "Botswana Pula": "BWP",
    "Brazilian Real": "BRL",
    "Brunei Dollar": "BND",
    "Bulgarian Lev": "BGN",
    "Burmese Kyat": "MMK",
    "Burundian Franc": "BIF",
    "CFP Franc": "XPF",
    "Cambodian Riel": "KHR",
    "Canadian Dollar": "CAD",
    "Cape Verdean Escudo": "CVE",
    "Cayman Islands Dollar": "KYD",
    "Central African CFA Franc": "XAF",
    "Chilean Peso": "CLP",
    "Chinese Renminbi": "CNY",
    "Colombian Peso": "COP",
    "Comorian Franc": "KMF",
    "Congolese Franc": "CDF",
    "Costa Rican Colon": "CRC",
    "Croatian Kuna": "HRK",
    "Cuban Peso": "CUP",
    "Czech Koruna": "CZK",
    "Danish Krone": "DKK",
    "Djiboutian Franc": "DJF",
    "Dominican Peso": "DOP",
    "East Caribbean Dollar": "XCD",
    "Egyptian Pound": "EGP",
    "Eritrean Nakfa": "ERN",
    "Eswatini Lilangeni": "SZL",
    "Ethiopian Birr": "ETB",
    "Euro": "EUR",
    "Falkland Islands Pound": "FKP",
    "Faroese Króna": "FOK",
    "Fiji Dollar": "FJD",
    "Gambian Dalasi": "GMD",
    "Georgian Lari": "GEL",
    "Ghanaian Cedi": "GHS",
    "Gibraltar Pound": "GIP",
    "Guatemalan Quetzal": "GTQ",
    "Guernsey Pound": "GGP",
    "Guinean Franc": "GNF",
    "Guyanese Dollar": "GYD",
    "Haitian Gourde": "HTG",
    "Honduran Lempira": "HNL",
    "Hong Kong Dollar": "HKD",
    "Hungarian Forint": "HUF",
    "Icelandic Króna": "ISK",
    "Indian Rupee": "INR",
    "Indonesian Rupiah": "IDR",
    "Iranian Rial": "IRR",
    "Iraqi Dinar": "IQD",
    "Israeli New Shekel": "ILS",
    "Jamaican Dollar": "JMD",
    "Japanese Yen": "JPY",
    "Jersey Pound": "JEP",
    "Jordanian Dinar": "JOD",
    "Kazakhstani Tenge": "KZT",
    "Kenyan Shilling": "KES",
    "Kiribati Dollar": "KID",
    "Kuwaiti Dinar": "KWD",
    "Kyrgyzstani Som": "KGS",
    "Lao Kip": "LAK",
    "Lebanese Pound": "LBP",
    "Lesotho Loti": "LSL",
    "Liberian Dollar": "LRD",
    "Libyan Dinar": "LYD",
    "Macanese Pataca": "MOP",
    "Macedonian Denar": "MKD",
    "Malagasy Ariary": "MGA",
    "Malawian Kwacha": "MWK",
    "Malaysian Ringgit": "MYR",
    "Maldivian Rufiyaa": "MVR",
    "Manx Pound": "IMP",
    "Mauritanian Ouguiya": "MRU",
    "Mauritian Rupee": "MUR",
    "Mexican Peso": "MXN",
    "Moldovan Leu": "MDL",
    "Mongolian Tögrög": "MNT",
    "Moroccan Dirham": "MAD",
    "Mozambican Metical": "MZN",
    "Namibian Dollar": "NAD",
    "Nepalese Rupee": "NPR",
    "Netherlands Antillian Guilder": "ANG",
    "New Taiwan Dollar": "TWD",
    "New Zealand Dollar": "NZD",
    "Nicaraguan Córdoba": "NIO",
    "Nigerian Naira": "NGN",
    "Norwegian Krone": "NOK",
    "Omani Rial": "OMR",
    "Pakistani Rupee": "PKR",
    "Panamanian Balboa": "PAB",
    "Papua New Guinean Kina": "PGK",
    "Paraguayan Guaraní": "PYG",
    "Peruvian Sol": "PEN",
    "Philippine Peso": "PHP",
    "Polish Złoty": "PLN",
    "Pound Sterling": "GBP",
    "Qatari Riyal": "QAR",
    "Romanian Leu": "RON",
    "Russian Ruble": "RUB",
    "Rwandan Franc": "RWF",
    "Saint Helena Pound": "SHP",
    "Samoan Tālā": "WST",
    "Saudi Riyal": "SAR",
    "Serbian Dinar": "RSD",
    "Seychellois Rupee": "SCR",
    "Sierra Leonean Leone": "SLL",
    "Singapore Dollar": "SGD",
    "Solomon Islands Dollar": "SBD",
    "Somali Shilling": "SOS",
    "South African Rand": "ZAR",
    "South Korean Won": "KRW",
    "South Sudanese Pound": "SSP",
    "Special Drawing Rights": "XDR",
    "Sri Lanka Rupee": "LKR",
    "Sudanese Pound": "SDG",
    "Surinamese Dollar": "SRD",
    "Swedish Krona": "SEK",
    "Swiss Franc": "CHF",
    "Syrian Pound": "SYP",
    "São Tomé and Príncipe Dobra": "STN",
    "Tajikistani Somoni": "TJS",
    "Tanzanian Shilling": "TZS",
    "Thai Baht": "THB",
    "Tongan Paʻanga": "TOP",
    "Trinidad and Tobago Dollar": "TTD",
    "Tunisian Dinar": "TND",
    "Turkish Lira": "TRY",
    "Turkmenistan Manat": "TMT",
    "Tuvaluan Dollar": "TVD",
    "UAE Dirham": "AED",
    "Ugandan Shilling": "UGX",
    "Ukrainian Hryvnia": "UAH",
    "United States Dollar": "USD",
    "Uruguayan Peso": "UYU",
    "Uzbekistani So'm": "UZS",
    "Vanuatu Vatu": "VUV",
    "Venezuelan Bolívar Soberano": "VES",
    "Vietnamese Đồng": "VND",
    "West African CFA franc": "XOF",
    "Yemeni Rial": "YER",
    "Zambian Kwacha": "ZMW",
    "Zimbabwean Dollar": "ZWL",
}

countryList = list(country_codes.keys())


def converter():
    st.header('Currency Converter application')
    fromCode = st.selectbox('From : ', countryList)
    toCodesList = countryList.copy()
    toCodesList.remove(fromCode)

    toCode = st.selectbox('To :', toCodesList)
    amount = st.number_input('Enter amount in '+fromCode + ' :')

        
    url = f'https://api.exchangerate-api.com/v4/latest/{country_codes[fromCode]}'
    response = requests.get(url).json()
    rate = response['rates'][f'{country_codes[toCode]}']
    result = amount*round(rate, 2)
    st.header('Result:')
    st.header(f'{amount} {fromCode} equals to {result} {toCode}')


def predictor():
    st.write('predictor app is under processing.')
    pass


def main():
    st.sidebar.header('Currency Converter and Rate Predictor App')
    opt = st.sidebar.selectbox('Select an option: ', ['Converter', 'Prediction'])
    if opt == 'Converter':
        converter()
    elif opt == 'Prediction':
        predictor()
    else:
        st.write('please select an option from sidebar.')


if __name__ == '__main__':
    main()

# main()
