#!/usr/bin/python
#! coding: shift-jis

#
# ���C�u�����C���|�[�g
#

import sys
import os

#
# �֐���`
#

def sapdentest(jcl):
    # �萔��`
    wkvol = "/BP/UNY020/"
    jcl_name = os.path.basename(jcl)
    step = []

    with open(wkvol + "test_" + jcl_name, "w") as o:
        with open(jcl, "r") as i:
            while(True):
                # jcl����s���ǂ�
                l = i.readline()
                # ���t�}�X�^�t�ւ�
                if "/BP/FLVP01/YRS.DATE.MST" in l:
                    step.append("*#*" + l)
                    step.append(l.replace("/BP/FLVP01/YRS.DATE.MST", "/BP/FLVP01/SAP.DATE.MST"))
                else:
                    step.append(l)

                # stepend�܂ŗ��ߍ��݁Astepend�ŏo��
                if "stepend" in l:
                    # �o�b�N�A�b�v�X�e�b�v�̓R�����g��
                    for s in step:
                        if "/export/home/bp/sh/BACKUP_DAY.csh" in s:
                            comment_step = []
                            comment_step = map(lambda x: "*#*" + x, step)
                            step = comment_step
                    o.writelines(step)
                    step = []
                # jobend�ŏI��
                if l.startswith("jobend") == True:
                    o.writelines(step)
                    break

#
# ���C������
#

if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # �����`�F�b�N
    if num != 2:
        print "Usage: %s jcl" % pgname
        quit()

    jcl = args[1]

    # jcl�̑��݃`�F�b�N
    if os.path.isfile(jcl) == False:
        print "Error: jcl does not exist"
        quit()

    sapdentest(jcl)
