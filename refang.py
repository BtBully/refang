# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:59:41 2020

@author: chris
"""

def refang(chars):
    
    def process_digits(pos):
        
        def check_entry(new_entry):
            last_entry_pos = len(s) % 3
            entry_pos = last_entry_pos + 1
            max_entry = pos_dict[entry_pos]
            if int(new_entry) > max_entry:
                return False
            return True
        
    
        if len(s) == ip_length:
            result_str = ''.join(s)
            results.append(result_str)
            return
        if pos >= dig_length:
            return
        new_entry = digits[pos]
        if check_entry(new_entry):
            s.append(new_entry)
            process_digits(pos+1)
            s.pop()
        process_digits(pos+1)
    
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
            
    
    pos_dict = {1:2, 2:5, 3:5}
    ip_length = 12
    s = []
    results = []
    digits = []
    char_length = len(chars)
    process_chars()
    dig_length = len(digits)
    process_digits(0)
    add_periods()
    return results
    

results = refang('25wef5..wef.255wefwe25wef.123645126')