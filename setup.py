from setuptools import setup

with open("README.md", "r") as fh:
      long_description = fh.read()

setup(
    name = "PiWarsTurkiyeRobotKiti2019",
    version = "0.9.6",
    author = "Yaşar İdikut, Sarp Yoel Kastro",
    author_email = "yasar.idikut@hisarschool.k12.tr, sarp.kastro@hisarschool.k12.tr",
    description = "Library that makes use of sensors, motors, and servos in the PiWars Turkey robot kit by HisarCS",
    packages = ["PiWarsTurkiyeRobotKiti2019"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Development Status :: 4 - Beta"],
    install_requires=[
        'cv2',
        'picamera',
        'pygame',
        'pololu_drv8835_rpi',
        'RPi.GPIO',
        'wiringpi'
    ]


)
