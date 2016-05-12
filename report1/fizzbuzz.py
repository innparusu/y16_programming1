#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def j_number(x):
    fizz = ["fizz", "", ""]
    buzz = ["buzz", "", "", "", ""]
    return (fizz[x%3]+buzz[x%5] or str(x))

for i in range(1,100):
    print(j_number(i))
