import os
import shutil

path_main = input('pls enter your directory')
abs_path = os.listdir(path_main)
for f in abs_path:
    if f.endswith('.pdf'):
        if abs_path.count('PDFFolder') == 0:
            os.mkdir(path_main + '/PDFFolder')
            shutil.move(path_main + '/' + f, path_main + '/PDFFolder')
        else:
            shutil.move(path_main + '/' + f, path_main + '/PDFFolder')
        print(abs_path)
    if f.endswith('docx'):
        if abs_path.count('WordFolder') == 0:
            os.mkdir(path_main + '/WordFolder')
            shutil.move(path_main + '/' + f, path_main + '/WordFolder')
        else:
            shutil.move(path_main + '/' + f, path_main + '/WordFolder')
        print(abs_path)
    if f.endswith('psd'):
        if abs_path.count('PsdFolder') == 0:
            os.mkdir(path_main + '/PsdFolder')
            shutil.move(path_main + '/' + f, path_main + '/PsdFolder')
        else:
            shutil.move(path_main + '/' + f, path_main + '/PsdFolder')
        print(abs_path)
    if f.endswith('jpg'):
        if abs_path.count('JpgFolder') == 0:
            os.mkdir(path_main + '/JpgFolder')
            shutil.move(path_main + '/' + f, path_main + '/JpgFolder')
        else:
            shutil.move(path_main + '/' + f, path_main + '/JpgFolder')
        print(abs_path)
    if f.endswith('png'):
        if abs_path.count('PngFolder') == 0:
            os.mkdir(path_main + '/PngFolder')
            shutil.move(path_main + '/' + f, path_main + '/PngFolder')
        else:
            shutil.move(path_main + '/' + f, path_main + '/PngFolder')
        print(abs_path)
    if f.endswith('pptx'):
        if abs_path.count('PptxFolder') == 0:
            os.mkdir(path_main + '/PptxFolder')
            shutil.move(path_main + '/' + f, path_main + '/PptxFolder')
        else:
            shutil.move(path_main + '/' + f, path_main + '/PptxFolder')
        print(abs_path)
print('123')
#ถ้าต้องการให้คัดแยก ไฟล์เพิ่ม ก็ copy ตั้งแต่ง บรรทัด 21-27 มาเลย แล้วก็เปลี่ยน
#แล้วก็เปลี่ยนในวงเล็บ endswitch เป็น นามสกุล file นั้นๆ
#แล้วก็เปลี่ยนชื่อ Folder ด้วย (เปลี่ยนให้เหมือนกัน)
#เปลี่ยน direcyory ตามปกติ
# ถ้าเกิด Eror ให้ลองเปลี่ยน directory จาก ตัวนี้ \ เป็น ตัวนี้/
