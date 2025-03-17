**README.md**  
# 📷 SVD Image Compression  
This Streamlit app compresses images using **Singular Value Decomposition (SVD)**. It allows users to upload an image, adjust the number of singular values used for compression, and download the compressed result.  

---

## 🚀 Features  
✅ Upload an image in **JPG, JPEG, or PNG** format  
✅ Compress the image using **SVD**  
✅ Adjust the number of singular values (k) for compression  
✅ Compare the original and compressed images side by side  
✅ Download the compressed image  

---

## 🛠️ Requirements  
Make sure you have the following Python packages installed:  
```bash
pip install streamlit opencv-python-headless numpy
```

---

## 💻 How to Run  
1. Clone the repository:  
```bash
git clone https://github.com/guptaatharva/Python-Cia-3.git
```

2. Run the Streamlit app:  
```bash
streamlit run example.py
```

---

## 📂 File Structure  
```
svd-image-compression/
├── example.py
├── README.md
```

---

## 🏗️ Code Overview  
### `compress_image(image, k)`
- Converts the input image to grayscale  
- Applies Singular Value Decomposition (SVD)  
- Reconstructs the image using only the top `k` singular values  

### `get_image_download_link(img_array, filename)`
- Encodes the compressed image to base64  
- Generates a download link for the compressed image  

---

## 🌟 How to Use  
1. Open the app in your browser.  
2. Upload an image (JPG, JPEG, or PNG).  
3. Adjust the slider to select the number of singular values (k).  
4. View the original and compressed images side by side.  
5. Click **"Save and Download"** to download the compressed image.  

---

## 🖼️ Example  
- Original Image Size: `1920 x 1080`  
- Compressed Image Size: `1920 x 1080` (k = 50)  

---


## 👨‍💻 Author  
**[Atharva Gupta]**  
GitHub: [@guptaatharva](https://github.com/guptaatharva)  

---
