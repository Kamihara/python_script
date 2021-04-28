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

def sapDenpyoTestHonban(jcl):
    # �萔��`
    wkvol = "/BP/UNY020/"
    jcl_name = os.path.basename(jcl)
    step = []
    out_jcl = wkvol + jcl_name

    with open(out_jcl, "w") as o:
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
    print(out_jcl + "���쐬���܂���")

def sapDenpyoTestKaihatsu(jcl):
    # �萔��`
    wkvol = "/BP/UNY010/"
    newvol = "/KEIRI1/SAP/BP/"
    jcl_name = os.path.basename(jcl)
    step = []
    out_jcl = wkvol + jcl_name

    with open(out_jcl, "w") as o:
        with open(jcl, "r") as i:
            while(True):
                # jcl����s���ǂ݁A�p�X�ϊ�
                l = i.readline().replace("/BP/", newvol)
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
    print(out_jcl + "���쐬���܂���")

#
# ���C������
#

if __name__ == "__main__":
    args = sys.argv
    num = len(args)
    pgname = args[0]

    # �����`�F�b�N
    if num != 3:
        print "Usage: %s jcl type[hon|kai]" % pgname
        quit()

    jcl = args[1]
    type = args[2].lower()

    # jcl�̑��݃`�F�b�N
    if os.path.isfile(jcl) == False:
        print "Error: jcl does not exist"
        quit()
    
    # �����敪�ŕ���
    if type == 'hon':
        sapDenpyoTestHonban(jcl)
    elif type == 'kai':
        sapDenpyoTestKaihatsu(jcl)
    else:
        print "Error: type is not illegal"
        quit()
