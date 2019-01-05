#! /bin/env python
# encoding=utf-8
# author: nickgu 
# 

import pydev

class SlotFileWriter:
    def __init__(self, filename):
        self.__fd = file(filename, 'w')
        self.__cur_slot_cnt = 0

        self.__ins_cnt = 0
        self.__slot_cnt = 0
        self.__fea_cnt = 0

    def begin_instance(self, label=0):
        self.__cur_slot_cnt = 0
        self.__fd.write('%s\t'%label)

    def write_slot(self, slot_id, slot_fea_id_list):
        if self.__cur_slot_cnt != 0:
            self.__fd.write('\t')

        self.__fd.write('%s:%s' % (slot_id, ','.join(map(lambda x:str(x), slot_fea_id_list))))

        self.__cur_slot_cnt += 1
        self.__slot_cnt += 1
        self.__fea_cnt += len(slot_fea_id_list)

    def end_instance(self):
        self.__fd.write('\n')
        self.__ins_cnt += 1

    def summary(self):
        pydev.info('Summary: ins=%d, slot=%d, fea=%d' % (self.__ins_cnt, self.__slot_cnt, self.__fea_cnt))


class SlotFileReader:
    def __init__(self, filename):
        self.__fd = file(filename)

    def read_one(self):
        pass

    def generate(self, count):
        pass



class Unittest(pydev.App):
    def __init__(self):
        pydev.App.__init__(self)

    def test_SlotFileWriter(self):
        writer = SlotFileWriter('test.ins')
        for i in range(1000):
            writer.begin_instance( i % 2 )
            for j in range(10):
                slot_id = 'slot%s' % j
                writer.write_slot(slot_id, list(range(j)))
            writer.end_instance()
        writer.summary()
        pydev.info('passed')


if __name__=='__main__':
    ut = Unittest()
    ut.run()