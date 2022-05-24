from __future__ import print_function
from mailmerge import MailMerge
from datetime import date


template="E:/teja.docx"

document=MailMerge(template)
print(document.get_merge_fields())

document.merge(
    name="yanagala teja",
    email="teja.yangala@dvara.com",
    skills="python",
    phonenumber="9182020065"
)

document.write('E:/test-output.docx.docx')