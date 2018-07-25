# -*- coding: utf-8 -*-
import random


class SFunc:

    def s_choice(self, req2):
        return random.choice(req2)  # random.choice(seq)：从任何序列seq中返回随机的元素

    def s_sample(self, req3, n):
        return random.sample(req3, n)  # random.sample(seq,n)：从指定的序列seq中，随机的截取指定长度n的片断，不作原地修改
