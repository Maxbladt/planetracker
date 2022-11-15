import tweepy
import time
import os
import requests
import csv
import sys



api_key = "f3JzpJaqDY8CLWgVbEjFFoIbC"
api_key_secret = "KtagoMuv154dBkhW8jESVwx4H17oOmSBrlDprM238jfg3tjqHS"
access_token = "1554109608259686400-7aMEcj0twjLJsrcTLor4VNmZLvHS8d"
access_token_secret = "6Nkh0qJX8tXCizixQAszosPXXSFznuTvcmVgz1GqrhNhb"

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token( access_token, access_token_secret)
api = tweepy.API(authenticator, wait_on_rate_limit=True)



# Go from ISO to country name
    

def ISO_country_to_continent(ISO_country_abreviation, Airport):
    Azië = ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CY', 'GE', 'HK', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 'KP', 'KR', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP', 'OM', 'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'LK', 'SY', 'TW', 'TJ', 'TH', 'TL', 'TR', 'TM', 'AE', 'UZ', 'VN', 'YE']
    Europa = ['AX', 'AL', 'AD', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CZ', 'DK', 'EE', 'FO', 'FI', 'FR', 'DE', 'GI', 'GR', 'GG', 'VA', 'HU', 'IS', 'IE', 'IM', 'IT', 'JE', 'LV', 'LI', 'LT', 'LU', 'MT', 'MD', 'MC', 'ME', 'NL', 'MK', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SJ', 'SE', 'CH', 'UA', 'GB']
    Afrika = ['DZ', 'AO', 'BJ', 'BW', 'IO', 'BF', 'BI', 'CV', 'CM', 'CF', 'TD', 'KM', 'CG', 'CD', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'SZ', 'ET', 'TF', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'YT', 'MA', 'MZ', 'nan', 'NE', 'NG', 'RE', 'RW', 'SH', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'TZ', 'TG', 'TN', 'UG', 'EH', 'ZM', 'ZW']
    Zuid_Amerika = ['AI', 'AG', 'AW', 'BS', 'BB', 'BZ', 'BM',  'BQ', 'BV',  'CA', 'KY',   'CR', 'CU', 'CW', 'DM', 'DO',  'SV',   'GL', 'GD', 'GP', 'GT',  'HT', 'HN', 'JM', 'MQ', 'MX', 'MS', 'NI', 'PA',   'PR', 'BL', 'KN', 'LC', 'MF', 'PM', 'VC', 'SX', 'GS',  'TT', 'TC', 'US',   'VG', 'VI']
    Noord_Amerika = ['AR', 'BO', 'BR', 'CL', 'CO','EC','FK','GF','GY','SR','PY','PE','UY','VE']
    Oceanië = ['AS', 'AU', 'CX', 'CC', 'CK', 'FJ', 'PF', 'GU', 'HM', 'KI', 'MH', 'FM', 'NR', 'NC', 'NZ', 'NU', 'NF', 'MP', 'PW', 'PG', 'PN', 'WS', 'SB', 'TK', 'TO', 'TV', 'UM', 'VU', 'WF']
    Antartica = ['AQ']


    if Airport == "Amsterdam Airport Schiphol":
        return "Schiphol"
    elif ISO_country_abreviation in Europa:
        return "Europa"

    elif ISO_country_abreviation in Azië:
        return "Azië"
    
    elif ISO_country_abreviation in Afrika:
        return "Afrika"
    
    elif ISO_country_abreviation in Zuid_Amerika:
        return "Zuid_Amerika"
    
    elif ISO_country_abreviation in Noord_Amerika:
        return "Noord_Amerika"
    
    elif ISO_country_abreviation in Oceanië:
        return "Oceanië"
    
    elif ISO_country_abreviation in Antartica:
        return "Antartica"
    
    
    else:
        return "Anders"
    
    

    
#function to create tweet


def create_tweet(callsign,vliegveld, continent, plane_action, lat_coordinaten, lon_coordinaten, vlucht_duur = "NA", afstand = "NA", kosten_vlucht = "NA"):


    if plane_action == "opstijgen":
        text_tweet = f"Beste landgenoten,\n\nDe {callsign} is opgestegen vanaf {vliegveld}. Dit vliegveld ligt op de volgende coordinaten https://maps.google.com/?q={lat_coordinaten},{lon_coordinaten}"
        try:
            media = api.media_upload(f"Twitter_photos_King_Willie/{continent}_{plane_action}.jpg")
            post_result = api.update_status(status=text_tweet, media_ids=[media.media_id])
            return post_result
        except:
            return "Tried to create tweet for opstijgen but didnt work properly"
    
    if plane_action == "landen":
        text_tweet = f"Beste landgenoten,\n\nDe {callsign} is geland op {vliegveld}.\nVlucht duur: {vlucht_duur} \nAfstand: {afstand}km \nKosten vlucht: €{kosten_vlucht}\nDit vliegveld ligt op de volgende coordinaten: \n\nhttps://maps.google.com/?q={lat_coordinaten},{lon_coordinaten}"
        try:
            media = api.media_upload(f"Twitter_photos_King_Willie/{continent}_{plane_action}.jpg")
            post_result = api.update_status(status=text_tweet, media_ids=[media.media_id])
            return post_result
        except Exception as e:
            return(e)

