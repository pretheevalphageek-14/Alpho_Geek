import time
import sys
import pygame

print("::::::::::::Welcome to Py Music::::::::::::")
print('''Naanum Rowdy Dhaan = r
      kadhale kadhale = w''')

i=input("Enter the Song No that You Want To Listen : ")

pygame.init()
pygame.mixer.init()
r='''
Good Boyum Illa Bad Boyum Illa
Rendoda Combo Namma Pulla
Nammaalu Weighta
Cha Cha Cha Illa
Dhavloondu Fightsu Kooda Poattathilla

Basha Pola Massa Ethuvum Senjathilla
Ranga Pola Wronga Onnum Kizhichathilla


Kathi Illa Ratham Illa Rowdy Dhaan
Kaathalikka Naeramulla Rowdy Dhaan
Vettu Kuthu Vaenaam Sollum Rowdy Dhaan
Vella Ullam Konda Nalla Rowdy Dhaan

Kathi Illa Ratham Illa Rowdy Dhaan
Kaathalikka Naeramulla Rowdy Dhaan
Vettu Kuthu Vaenaam Sollum Rowdy Dhaan
Vella Ullam Konda Nalla Rowdy Dhaan


Naanum Rowdy Dhaan dhaan dhaan
Naanum Rowdy Dhaan dhaan dhaan
Naanum Rowdy Dhaan dhaan dhaan
Naanum Rowdy Dhaan dhaan dhaan

Oru Kallula Pathu Maanga Onna Adipaane
Namma Pulla
Oru Vettula Nooru Thundu Pottu Piripaney
Nalla Pulla


Chinna Sanda Vantha
Konjam Thalli Nippaan
Periya Sanda Vantha
Paesi Puriya Vaippaan
Oru Unmaiyaala Nee Nønthupønaa
Oru Pøiya Šølli Nalla Širikka Vaipaan


Basha Pøla Massa Èthuvum Šenjathilla
Ranga Pøla Wrønga Onnum Kizhichathilla

Chørus Štart


Dum Adichi Møønji Maela Oøtha Maattaan
Thani Pøttu Thølla Yaethum Panna Mattaan
Pønnungala Kindal Panni Kølla Maattaan
Aana Šaami Maela Šathiyama Røwdy Dhaan

Šuper Ji Šuper Ji

Kathi Illa Ratham Illa Røwdy Dhaan
Kaathalikka Naeramulla Røwdy Dhaan paahh
Vettu Kuthu Vaenaam Šøllum Røwdy Dhaan
Vella Ullam Kønda Nalla Røwdy Dhaan

paap
Naanum Rowdy Dhaan dhaan dhaan
Naanum Rowdy Dhaan dhaan dhaan
Naanum Rowdy Dhaan dhaan dhaan
Naanum Rowdy Dhaan dhaan dhaan'''

w='''................wஓஓ… ஆஆ
காதலே காதலே
என்னை உடைத்தேனே
என்னில் உன்னை
அடைத்தேனே உயிர் கட்டி
இணைத்தேனே
நேற்றினை
காற்றிலே கொட்டி
இரைத்தேனே இமை
கட்டு அவிழ்த்தேனே
துயர் மட்டும் மறைத்தேனே
நிழல் ஆடும்
நினைவில் ரெண்டு
களவாடி தருவேன்
இன்று கடிகாரம் காலம்
நேரம் சுழற்றிடுவேன்
உன்னை காண
உலகம் சென்று அங்கேயும்
இதயம் தந்து புதிதான காதல்
ஒன்று நிகழ்த்திடுவேன்
இன்று நேற்று
நாளை என்றும் நீ என்
தேவதை காதல் செய்யும்
மாயை என் வானம் எங்கும்
பூ மழை
ஓஹோ ஓ
ஓஹோ ஓஹோ
ஓ ஓஹோ ஓஹோ
ஓ ஓஹோ ஓஹோ
மனதோடு
மட்டும் இங்கு உறவாடும்
நேசம் ஒன்று உயிரோடு
என்னை ஏதோ இறக்கியதே
படியேறி
கீழே செல்லும்
புரியாத பாதை
ஒன்று அதில் ஏறி
போக சொல்லி குழப்பியதே
காலம்
கடந்தாலும் மழை
நீரை போலே நேரம்
கண் முன் மெல்ல
சிந்துது என் சிந்தனையிலே
கடிகாரம்
வாங்க போனால்
அந்த நேரம் வாங்கி
தந்தாய் என்ன நானும்
செய்வேனோ எந்தன்
உயிரே
ஹா ஆஆ
ஹா ஆஆ ஹா
ஆஆ ஹா ஆஆ
ஹா ஆஆ ஹா
ஆஆ ஹா ஆஆ
நிபமப நிபமப பநிச கரிச நிச கரிச நிச (அஅஅ)
கரிசநிசக சமப மபநி மபமபநிச ஆஆஆஆ
இன்று நேற்று
நாளை என்றும் நீ என்
தேவதை காதல் செய்யும்
மாயை என் வானம் எங்கும்
பூ மழை
ஓஹோ ஓ
ஓஹோ ஓஹோ
ஓ ஓஹோ ஓஹோ
ஓ ஓஹோ ஓஹோ
ஓ ஓஹோ ஓஓஓஓஓ'''

q=0.1
e=0.1
if i=='r':
    sound = pygame.mixer.Sound('Naanum-Rowdy-Dhaan-wav.wav')
    sound.play(1, 0, 500)
    pygame.time.delay(11000)
    for char in r:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(q)
if i=='w':
    sound = pygame.mixer.Sound('Kadhale-Kadhale (1).wav')
    sound.play(1, 0, 500)
    pygame.time.delay(20000)
    for char in w:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(e)

