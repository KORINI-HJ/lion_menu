# -*- coding: utf-8 -*-
"""lion_menu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wJtzXxJdcR0Asvfkn8yTFfU_-0hLMJfg
"""

import random
import time

lunch = ["떡볶이", "짜장면", "찜닭", "돈가스", "제육볶음"]

while True:
  print(lunch)
  item = input("음식을 추가해 주세요: ")
  if(item == "q"):
    break
  else:
    lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
  print(set_lunch)
  item = input("음식을 삭제해 주세요: ")
  if(item=="q"):
    break
  else:
    set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))