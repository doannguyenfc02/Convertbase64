import base64

def image_to_base64(image_path, output_file):
    try:
        with open(image_path, "rb") as image_file:
            # Đọc nội dung của ảnh
            image_content = image_file.read()

            # Mã hóa nội dung thành base64
            base64_encoded = base64.b64encode(image_content)

            # Chuyển đổi từ bytes sang chuỗi (str)
            base64_string = base64_encoded.decode('utf-8')

            # Lưu vào tệp văn bản
            with open(output_file, "w") as output:
                output.write(base64_string)
            
            print(f"Chuyển đổi thành công và lưu vào {output_file}")
    except Exception as e:
        print(f"Lỗi: {e}")

# Gọi hàm với tên file ảnh và tên file output
image_to_base64("input_img/test.jpg", "base64/test2.txt")
