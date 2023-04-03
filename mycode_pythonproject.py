{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red183\green111\blue179;
\red202\green202\blue202;\red194\green126\blue101;\red140\green211\blue254;\red70\green137\blue204;\red212\green214\blue154;
\red89\green138\blue67;\red167\green197\blue152;\red67\green192\blue160;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c77255\c52549\c75294;
\cssrgb\c83137\c83137\c83137;\cssrgb\c80784\c56863\c47059;\cssrgb\c61176\c86275\c99608;\cssrgb\c33725\c61176\c83922;\cssrgb\c86275\c86275\c66667;
\cssrgb\c41569\c60000\c33333;\cssrgb\c70980\c80784\c65882;\cssrgb\c30588\c78824\c69020;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
import json\
from ibm_watson import LanguageTranslatorV3\
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator\
import os\
from dotenv import load_dotenv\
\
load_dotenv()\
\
apikey = os.environ['apikey']\
url = os.environ['url']\
\
authenticator =IAMAuthenticator(apikey)\
language_translator=LanguageTranslatorV3 (\
                    version='2018-05-01',\
                    authenticator=authenticator\
                                    )\
language_translator.set_service_url(url)\
\
def english_to_french(text1):\
\
#This function translates english to french\
\
\
 frenchtranslation =language_translator.translate(\
                text=text1,\
                model_id='en-fr'\
                    ) . get_result()\
 return frenchtranslation.get("translations") [0].get ("translation")\
\
def french_to_english(text1):\
\
# This function translates french to English\
\
 englishtranslation =language_translator.translate(\
                text=text1,\
                model_id='fr-en'\
                    ) . get_result()\
 return englishtranslation.get("translations") [0].get ("translation")\
\
\
\
import unittest\
from translator import french_to_english, english_to_french\
class TestEnglishFrench(unittest.TestCase): \
    def test1(self): \
        self.assertNotEqual(english_to_french('Hello'),None)# test if null is given output is null\
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # tests when hello is given output is Bonjour\
       \
        \
class TestFrenchEnglish(unittest.TestCase): \
    def test1(self): \
        self.assertNotEqual(french_to_english("Bonjor"),None) # test if null is given output is null\
        self.assertEqual( french_to_english("Bonjour"), "Hello")  # tests when hello is given output is Bonjour\
       \
        \
unittest.main()\
}