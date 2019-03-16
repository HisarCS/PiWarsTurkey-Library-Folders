from setuptools import setup

with open("README.md", "r") as fh:
      long_description = fh.read()


print("                                                                                 ")
print("*********************************************************************************")
print("         PiWarsTurkiyeRobotKiti2019 kutuphanesine hosgeldiniz!")
print("         Gerekli dokumantosyonu https://github.com/HisarCS/PiWarsTurkey-Library-Folders adresinden bulabilirsiniz.")
print("         Herhangi bir sorun cikarsa once yukaridaki dokumantosyona goz atmanizi, eger sorun hala devam ederse bize ulasmaktan cekinmeyin.")
print("         Bu kutuphaneyi indirirken de kullanirken de programin sudo ile calistigindan emin olun.")
print("*********************************************************************************")
print("                                                                                 ")

setup(
    name = "PiWarsTurkiyeRobotKiti2019",
    version = "1.1.4",
    author = "Yasar İdikut, Sarp Yoel Kastro",
    author_email = "yasar.idikut@hisarschool.k12.tr, sarp.kastro@hisarschool.k12.tr",
    description = "Library that makes use of sensors, motors, and servos in the PiWars Turkey robot kit by HisarCS",
    packages = ["PiWarsTurkiyeRobotKiti2019"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Development Status :: 4 - Beta"],
    install_requires=[
        'picamera',
        'pygame',
        'RPi.GPIO',
        'wiringpi',
    ]

)
