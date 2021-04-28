# coding: UTF-8
#!/usr/bin/python
import sys
import os
import glob
import csv

class CobolAnalyzer:
    def __init__(self, path):
        self.path = path                        # /export/home/bp/cobol/main/src/SAMPLE.cob

    def basename(self):
        return os.path.basename(self.path)      # SAMPLE.cob

    def load(self):
        return self.basename().split('.')[0]    # SAMPLE

    def search_assigned_jcl(self):
        ### �{�ԋ@����
        # �Y���v���O�������A�T�C������Ă���jcl���������A
        # jcl�̃t���p�X�����X�g�`���ŕԋp����B

        result = []

        # �����Ώ�jcl���C�u����
        jcl_lib = []
        jcl_lib.append("/export/home/bp/jcl")
        jcl_lib.append("/export/home/bp/unyou1/jcl")
        jcl_lib.append("/export/home/bpp/bpw00/*/jcl")

        # �����Ώ�jcl���C�u�����z���ɑ��݂���S�t�@�C���̑S�s���������A
        # exec���Ƀv���O���������܂܂�Ă��邩���肷��B
        # ���R�����g�s�͏���
        for lib in jcl_lib:
            jcl_list = glob.glob(lib + '/*')
            for jcl in jcl_list:
                try:
                    with open(jcl, "r") as j:
                        for line in j:
                            if line.find("exec " + self.load() + " ") >= 0 and not line[0:2] == "*#":
                                result.append(jcl)
                except Exception as e:
                    print(str(e))

        return result

    def search_using_copy(self):
        ### �J���@����
        # �Y���v���O���������p���Ă���R�s�[����������A
        # �R�s�[�喼�̂ƃv���O�������ł̊Y���s�����X�g�`���ŕԋp����B

        result = []

        # �Ώۃv���O�����̑S�s���������A
        # �R�s�[�傪�w�肳��Ă���s�𔻒肷��B
        # ���R�����g�s�A�ėp���W���[���p�R�s�[��iBPU2Xxxx�j�͏���
        with open(self.path, "r") as p:
            for line in p:
                if line.find("COPY ") >= 0 and not line[6] == '*' and line.find("BPU2X") < 0:
                    result.append(line.split()[2].replace('.', ''))
                    # result.append(line.replace('\n', ''))

        return result

        
if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    script_name = args[0]

    # �����`�F�b�N
    if num != 2:
        print "Usage: %s program_path_list" % script_name
        quit()

    input_filepath = args[1]

#    with open(input_filepath, "r") as f:
#        cr = csv.reader(f, delimiter="\n")
#
#        for c in cr:
#            for program_path in c:
#                pg = Cobol(program_path)
#                l = []
#                l.append(pg.basename())
#
#                for jcl in pg.search_assigned_jcl():
#                    l.append(jcl)
#
#                with open("/BP/UNY020/s1yst.out", "a") as o:
#                    cw = csv.writer(o)
#                    cw.writerow(l)

    with open(input_filepath, "r") as f:
        cr = csv.reader(f, delimiter="\n")

        for c in cr:
            for pg_path in c:
                cob = CobolAnalyzer(pg_path)
                l = []
                l.append(cob.basename())
                for copy in cob.search_using_copy():
                    l.append(copy)
                with open("/BP/UNY020/" + script_name[:-3] + "_s1yst.out", "a") as o:
                    cw = csv.writer(o, delimiter="\t")
                    cw.writerow(l)
