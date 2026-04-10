# File: pdf2img.py
# To convert PDF to PNG images using PyMuPDF (fitz)
# Author: Neptune
# Created: 2026-Apr-9
# Last edited: 2026-Apr-9


# before running this code, make sure to install the required library:
# pip install PyMuPDF



import fitz  
import os

def convert_pdf_to_images(pdf_path, output_folder, base_filename, dpi=300):
    """
    
    parameters:
    - pdf_path: ที่อยู่ของไฟล์ PDF ต้นฉบับ
    - output_folder: โฟลเดอร์ปลายทางที่ต้องการบันทึกรูปภาพ
    - base_filename: ชื่อไฟล์รูปภาพที่ต้องการตั้ง
    - dpi: ความละเอียดของรูปภาพ (ยิ่งเยอะยิ่งชัด แต่ไฟล์จะใหญ่ขึ้น)
    """
    
    # 1. ตรวจสอบและสร้างโฟลเดอร์ปลายทางหากยังไม่มี
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"สร้างโฟลเดอร์ปลายทาง: {output_folder}")

    # 2. เปิดไฟล์ PDF
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการเปิดไฟล์ PDF: {e}")
        return

    # 3. ตั้งค่าความละเอียดของภาพ
    zoom = dpi / 72  # 72 คือ DPI มาตรฐาน
    mat = fitz.Matrix(zoom, zoom)

    # 4. วนลูปอ่าน PDF ทีละหน้าเพื่อแปลงเป็นรูปภาพ
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat)

        # กำหนดชื่อไฟล์ (เพิ่มเลขหน้าอัตโนมัติ)
        image_name = f"{base_filename}_page_{page_num + 1}.png"
        
        # นำโฟลเดอร์ปลายทางและชื่อไฟล์มาต่อกันเป็น Path ที่สมบูรณ์
        output_path = os.path.join(output_folder, image_name)

        # บันทึกไฟล์รูปภาพ
        pix.save(output_path)
        print(f"บันทึกรูปภาพสำเร็จ: {output_path}")

    doc.close()
    print("\n แปลงไฟล์ PDF เป็นรูปภาพเสร็จสมบูรณ์!")



# 1. ระบุที่อยู่ของไฟล์ PDF ที่คุณต้องการแปลง (ต้องมีไฟล์นี้อยู่จริง)
sample_file = "68/68_may_2.pdf"  

# 2. ระบุโฟลเดอร์ที่คุณต้องการให้รูปภาพไปอยู่ (ถ้าไม่มี โค้ดจะสร้างให้เอง)
image_path_folder = "68/pages/may"  

# 3. ระบุชื่อรูปภาพที่ต้องการตั้ง
image_name = "68_may_2"

# เรียกใช้งานฟังก์ชัน
convert_pdf_to_images(sample_file, image_path_folder, image_name, dpi=300)