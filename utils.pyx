import random

def gen_rand_num(num_len):
    return int(random.random() * (10 ** num_len))

def create_rand_array(int size, int num_len = 2):
    array = [gen_rand_num(num_len) for _ in range(size)]
    return array