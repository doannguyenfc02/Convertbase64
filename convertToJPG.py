from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Nhận dữ liệu JSON từ yêu cầu
        data = request.json

        # Kiểm tra xem trường 'file' có tồn tại không
        if 'file' not in data:
            return jsonify({'error': 'Missing "file" field'}), 400

        # Giải mã mã base64
        base64_encoded = data['file']
        file_content = base64.b64decode(base64_encoded)

        # Chuyển đổi nội dung thành hình ảnh
        image = Image.open(BytesIO(file_content))

        # Lưu hình ảnh thành tệp
        image.save('uploaded_image.jpg')

        return jsonify({'message': 'Image uploaded successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
