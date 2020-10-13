# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:59:41 2020

@author: chris
"""


def refang(chars):
    
    def process_digits(pos):
        
        def check_entry(new_entry):
            
            def check_group_max():
                groups = len(s) // 3
                beg_group = groups * 3 
                group = ''.join(s[beg_group:])
                new_group= group + new_entry
                for max_group in group_max:
                    if int(new_group) > max_group:
                        return False
                return True
            
            def check_memo():
                memo_list = memo[len(s)]
                if new_entry in memo_list:
                    return False
                return True
        
            return (check_group_max() and check_memo())
        
        def record_memo(new_entry):
            result_pos = len(s)-1
            memo[result_pos].append(new_entry)
            
        def clear_old_memo():
            if len(s) >= 11:
                return
            old_entries_index = (len(s) - 1) + 2
            if memo[old_entries_index] != []:
                memo[old_entries_index] = []
        
        if len(s) == ip_length:
            result_str = ''.join(s)
            results.append(result_str)
            return
        if pos >= dig_length:
            return
        new_entry = digits[pos]
        if check_entry(new_entry):
            s.append(new_entry)
            record_memo(new_entry)
            process_digits(pos+1)
            s.pop()
            clear_old_memo()
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
            
            
    group_max = [255]
    ip_length = 12
    s = []
    results = []
    digits = []
    memo = [[] for i in range(ip_length)]
    char_length = len(chars)
    process_chars()
    dig_length = len(digits)
    process_digits(0)
    add_periods()
    return results
    


results = refang('25wef5..wef.255wefwe25wef.12553645126')