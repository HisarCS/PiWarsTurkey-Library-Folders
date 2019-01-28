from setuptools import setup

with open("README.md", "r") as fh:
      long_description = fh.read()


setup(
      name = "PiWarsTurkiyeRobotKiti2019",
      version = "0.3",
      author = "Yaşar İdikut, Sarp Yoel Kastro",
      author_email = "yasar.idikut@hisarschool.k12.tr, sarp.kastro@hisarschool.k12.tr",
      description = "Library that makes use of sensors, motors, and servos in the PiWars Turkey robot kit by HisarCS",
      py_modules = ["PiWarsTurkiyeRobotKiti2019"],
      package_dir = {"": "src"},
      long_description=long_description,
      long_description_content_type="text/markdown"

)
