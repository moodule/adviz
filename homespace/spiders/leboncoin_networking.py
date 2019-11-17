# -*- coding: utf-8 -*-

"""
=====================
Leboncoin Real-Estate
=====================

Search for real-estate in the list of ads hosted by leboncoin.
"""

from __future__ import division, print_function, absolute_import

from homespace.items import SmartphoneAd, SmartphoneAdLoader
from homespace.spiders.leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

BRAND_VALUES = []

COLOR_VALUES = []

MODEL_VALUES = []

PRICE_VALUES = (
    list(range(0, 50, 10))
    + list(range(50, 100, 25))
    + list(range(100, 550, 100)))

#####################################################################
# SPIDER
#####################################################################

class LeboncoinSmartphoneSpider(LeboncoinSpider):
    name = 'leboncoin_smartphone'
    allowed_domains = ['www.leboncoin.fr']

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinSmartphoneSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._search_args = {
            'category': '17',
            'locations': '',
            'page': '1',
            'phone_brand': '',
            'phone_color': '',
            'phone_memory': '',
            'phone_model': '',
            'price': '',
            'shippable': '1',
            'text': (
                '-fixe%20-fil%20-fax%20-minitel%20-talkie%20-montre%20-touche%20-vintage%20-gps'
                + '%20-brassard%20-boite'
                + '%20-ecouteur%20-kit%20-main%20-libre'
                + '%20-rallonge%20-chargeur%20-adaptateur%20-cable%20-batterie'
                + '%20-samsung%20-nokia%20-lumia%20-alcatel%20-logicom%20-motorola%20-asus%20-lg%20-jbl%20-siemens%20-doro'
                + '%20-vitre%20-verre'
                + '%20-pochette%20-coque%20-protection%20-support%20-housse%20-pied%20-perche%20-selfie%20-trepied%20-etui%20-protege')}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'brand': (
                '//div[contains(@data-qa-id, "criteria_item_phone_brand")]'
                + '/div/div[2]/text()'),
            'color': (
                '//div[contains(@data-qa-id, "criteria_item_phone_color")]'
                + '/div/div[2]/text()'),
            'model': (
                '//div[contains(@data-qa-id, "criteria_item_phone_model")]'
                + '/div/div[2]/text()'),
            'ram': (
                '//div[contains(@data-qa-id, "criteria_item_phone_memory")]'
                + '/div/div[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = SmartphoneAd
        self._loader_class = SmartphoneAdLoader