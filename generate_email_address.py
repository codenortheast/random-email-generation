# -*- coding: utf-8 -*-
"""generate-email-address.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nymZlyVqRxTTuyyq_mzx-ZxE-lczSYQi
"""

import random as r
import time as t
import os

"""Generate a random email. Write down the email addresses in a text file """

def randomMailGeneration():
  alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  domainNames = ["@gmail", "@yahoo", "@outlook", "@tata", "@notadomain", "@fakeme", "@msn", "@xxx", "@support"]
  endDomainNames = [".com", ".org", ".edu", ".in", ".io", ".net"]
  randomName = ""
  i=1
  nameLength = r.randint(4,7)

  while i < nameLength:
    randomName = randomName + alphabets[r.randint(0, 25)]
    i+=1

  randomNumber = str(r.randint(111, 999))
  randomMail = randomName + randomNumber + domainNames[r.randint(0, 8)] + endDomainNames[r.randint(0, 5)]
  print(randomMail)

  saveMailFile = open("fakemailids.txt", "a")
  saveMailFile.write(randomMail + "\n")

while 1:
  randomMailGeneration()
  t.sleep(1)

