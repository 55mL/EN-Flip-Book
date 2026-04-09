import fitz  
import os

def convert_pdf_to_images(pdf_path, output_folder, base_filename, dpi=300):
    """
    ฟังก์ชันสำหรับแปลงไฟล์ PDF เป็นรูปภาพ PNG
    
    พารามิเตอร์:
    - pdf_path: ที่อยู่ของไฟล์ PDF ต้นฉบับ
    - output_folder: โฟลเดอร์ปลายทางที่ต้องการบันทึกรูปภาพ
    - base_filename: ชื่อไฟล์รูปภาพที่ต้องการตั้ง
    - dpi: ความละเอียดของรูปภาพ (ยิ่งเยอะยิ่งชัด แนะนำที่ 300)
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

    # 3. ตั้งค่าความละเอียดของภาพ (Zoom factor)
    zoom = dpi / 72  # 72 คือ DPI มาตรฐาน
    mat = fitz.Matrix(zoom, zoom)

    # 4. วนลูปอ่าน PDF ทีละหน้าเพื่อแปลงเป็นรูปภาพ
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=mat)

        # กำหนดชื่อไฟล์ (เพิ่มเลขหน้าลงไปเพื่อไม่ให้ชื่อซ้ำกัน)
        image_name = f"{base_filename}_page_{page_num + 1}.png"
        
        # นำโฟลเดอร์ปลายทางและชื่อไฟล์มาต่อกันเป็น Path ที่สมบูรณ์
        output_path = os.path.join(output_folder, image_name)

        # บันทึกไฟล์รูปภาพ
        pix.save(output_path)
        print(f"บันทึกรูปภาพสำเร็จ: {output_path}")

    doc.close()
    print("\n แปลงไฟล์ PDF เป็นรูปภาพเสร็จสมบูรณ์!")



# 1. ระบุที่อยู่ของไฟล์ PDF ที่คุณต้องการแปลง (ต้องมีไฟล์นี้อยู่จริง)
ไฟล์ต้นฉบับ = "63/63_jan_1.pdf"  

# 2. ระบุโฟลเดอร์ที่คุณต้องการให้รูปภาพไปอยู่ (ถ้าไม่มี โค้ดจะสร้างให้เอง)
โฟลเดอร์เก็บรูป = "63/pages"  

# 3. ระบุชื่อรูปภาพที่คุณต้องการตั้ง
ชื่อรูปภาพที่ต้องการ = "63_jan_1_" 

# เรียกใช้งานฟังก์ชัน
convert_pdf_to_images(ไฟล์ต้นฉบับ, โฟลเดอร์เก็บรูป, ชื่อรูปภาพที่ต้องการ, dpi=300)