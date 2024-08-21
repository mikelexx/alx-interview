#!/usr/bin/python3
"""
validating utf-8 authenticity of data
"""
from typing import List


def to_eight_bytes(n: int) -> str:
    """
    converts integer to bytes and extracts the 8 LSB
    """
    res: str = ''
    tmp = n
    while tmp > 0:
        rem = tmp % 2
        tmp = tmp // 2
        res += str(rem)

    res = res[0:8]
    res = res[::-1]
    res = ('0' * (8 - len(res))) + res
    return res


def validUTF8(data: List[int]) -> bool:
    """
     determines if a given data set represents a valid UTF-8 encoding.
        A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data, therefore you only
          need to handle the 8 least significant bits of each
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    bytesequence = ''
    for num in data:
        bytesequence += to_eight_bytes(num)

    identifiers = set(['0', '110', '1110', '11110'])
    curr_id = ''
    prev_slow = curr_slow = 0
    while curr_slow < len(bytesequence):
        curr_id += bytesequence[curr_slow]
        # print(f' curr_slow={curr_slow} curr_id = {
        #          curr_id} sq={bytesequence[curr_slow::]}')
        if curr_slow - prev_slow >= 5 and curr_id not in identifiers:
            # print("invalid utf->", bytesequence[prev_slow::])
            return False
        if curr_id in identifiers:
            fast = curr_slow + (8 - len(curr_id)) + 1
            # print(f'fast_pos = {fast}')
            for _ in range(1, len(curr_id) - 1, 1):
                continuam = bytesequence[fast:fast + 2]
                if continuam != '10' or fast >= len(bytesequence):
                    # print("invalid continuam-> ", bytesequence[fast::])
                    return False
                # else:
                # print(f"process-> {bytesequence[fast: fast + 8]} ")
                fast += 8
            curr_id = ''
            curr_slow = prev_slow = fast
        else:
            curr_slow += 1
    return True
