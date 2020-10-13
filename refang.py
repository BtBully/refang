# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:59:41 2020

@author: chris
"""

def refang(chars):
    
    def process_digits(length, digits):
        if length == 0:
            return []
        if length > len(digits):
            return []
        first = digits[0]
        short_rs = process_digits(length-1, digits[1:])
        long_rs = process_digits(length, digits[1:])
        results = [first + short for short in short_rs] + long_rs
        if short_rs == []:
            results = [first] + long_rs
        return results
            
    def process_chars():
        for i in range(char_length):
            entry = chars[i]
            if entry.isdigit():
                digits.append(entry)
                
    def add_periods():
        for i in range(len(results)):
            r = results[i]
            new_result = r[:3] + '.' + r[3:6] + '.' + r[6:9] + '.' + r[9:12]
            results[i] = new_result
            
    def remove_duplicates():
        new_results = list(dict.fromkeys(results))
        return new_results
    
    def filter_results():
        new_results = []
        for entry in results:
            if (
                    int(entry[ :3]) <= 255
                and int(entry[3:6]) <= 255
                and int(entry[6:9]) <= 255
                and int(entry[9: ]) <= 255
               ):
                    new_results.append(entry)
        return new_results
                
    
    ip_length = 12
    digits = []
    char_length = len(chars)
    process_chars()
    results = process_digits(ip_length, digits)
    results = remove_duplicates()
    results = filter_results()
    add_periods()
    return results
    
    
results = refang('25wef5..wef.255wefwe25wef.12553645126')