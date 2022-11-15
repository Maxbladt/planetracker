import pandas as pd

pd.options.display.max_rows = 999
data = pd.read_csv(r'Continents_by_ISO_Country.csv')
df = pd.DataFrame(data, columns= ['alpha-2', 'region'])

Asia = []
Europe = []
Africa = []
Americas = []
Australia = []
Antartice = []

for index, row in df.iterrows():
    if row['region'] == "Asia":
        Asia.append(row["alpha-2"])
    
    if row['region'] == "Europe":
        Europe.append(row["alpha-2"])
    
    if row['region'] == "Africa":
        Africa.append(row["alpha-2"])
    
    if row['region'] == "Americas":
        Americas.append(row["alpha-2"])
    
    if row['region'] == "Australia":
        Australia.append(row["alpha-2"])
    if row['region'] == "Oceania":
        Australia.append(row["alpha-2"])
    
    if row['region'] == "Antartice":
        Antartice.append(row["alpha-2"])



# print(Asia )
# print(Europe )
# print(Africa )
# print(Americas )
# print(Australia)
print(Antartice)

Asia = ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CY', 'GE', 'HK', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 'KP', 'KR', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP', 'OM', 'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'LK', 'SY', 'TW', 'TJ', 'TH', 'TL', 'TR', 'TM', 'AE', 'UZ', 'VN', 'YE']

Europe = ['AX', 'AL', 'AD', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CZ', 'DK', 'EE', 'FO', 'FI', 'FR', 'DE', 'GI', 'GR', 'GG', 'VA', 'HU', 'IS', 'IE', 'IM', 'IT', 'JE', 'LV', 'LI', 'LT', 'LU', 'MT', 'MD', 'MC', 'ME', 'NL', 'MK', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SJ', 'SE', 'CH', 'UA', 'GB']

Africa = ['DZ', 'AO', 'BJ', 'BW', 'IO', 'BF', 'BI', 'CV', 'CM', 'CF', 'TD', 'KM', 'CG', 'CD', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'SZ', 'ET', 'TF', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'YT', 'MA', 'MZ', 'nan', 'NE', 'NG', 'RE', 'RW', 'SH', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'TZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW']

Americas = ['AI', 'AG', 'AR', 'AW', 'BS', 'BB', 'BZ', 'BM', 'BO', 'BQ', 'BV', 'BR', 'CA', 'KY', 'CL', 'CO', 'CR', 'CU', 'CW', 'DM', 'DO', 'EC', 'SV', 'FK', 'GF', 'GL', 'GD', 'GP', 'GT', 'GY', 'HT', 'HN', 'JM', 'MQ', 'MX', 'MS', 'NI', 'PA', 'PY', 'PE', 'PR', 'BL', 'KN', 'LC', 'MF', 'PM', 'VC', 'SX', 'GS', 'SR', 'TT', 'TC', 'US', 'UY', 'VE', 'VG', 'VI']

Oceania = ['AS', 'AU', 'CX', 'CC', 'CK', 'FJ', 'PF', 'GU', 'HM', 'KI', 'MH', 'FM', 'NR', 'NC', 'NZ', 'NU', 'NF', 'MP', 'PW', 'PG', 'PN', 'WS', 'SB', 'TK', 'TO', 'TV', 'UM', 'VU', 'WF']

Antartice = ['AQ']


# print(Asia)

# len_asia = len(Asia)
# len_europe = len(Europe)
# len_africa = len(Africa)
# len_americas = len(Americas)
# len_australia = len(Australia)

# total_len = len(Asia) + len(Europe) + len(Africa) + len(Americas) + len(Australia) + len(Antartice)

# print(total_len)
# print(f'\n{len_asia}')
# print(len_europe)
# print(len_africa)
# print(len_americas)
# print(len_australia)
# print(len(Antartice))



