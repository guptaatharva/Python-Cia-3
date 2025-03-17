import streamlit as st
import numpy as np
import cv2
from io import BytesIO
import base64

def compress_image(image, k):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # SVD
    U, S, Vt = np.linalg.svd(image_gray, full_matrices=False)
    
    # Reconstruct the image using only the top k singular values
    U_k = U[:, :k]
    S_k = np.diag(S[:k])
    Vt_k = Vt[:k, :]
    
    compressed_image = U_k @ S_k @ Vt_k
    
    return compressed_image.astype(np.uint8)

def get_image_download_link(img_array, filename="compressed_image.jpg"):
    _, buffer = cv2.imencode(".jpg", img_array)
    b64 = base64.b64encode(buffer).decode()
    href = f'<a href="data:file/jpg;base64,{b64}" download="{filename}">Download Compressed Image</a>'
    return href
st.set_page_config(page_title="SVD Image Compression", page_icon="📷")
st.title("Image Compression using Singular Value Decomposition (SVD)")
st.write("Upload an image and compress it using SVD by selecting the number of singular values (k).")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    st.subheader("Original vs Compressed Image")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, channels="BGR", caption=f"Original Image ({image.shape[1]}x{image.shape[0]})", use_column_width=True)
    
    k = st.slider("Select the number of singular values (k) for compression", min_value=1, max_value=min(image.shape[0], image.shape[1]), value=50)
    
    compressed_image = compress_image(image, k)
    
    with col2:
        st.image(compressed_image, caption=f"Compressed Image ({compressed_image.shape[1]}x{compressed_image.shape[0]}) (k={k})", use_column_width=True, clamp=True)
    
    st.write("### Image Sizes:")
    st.write(f"Original Image: {image.shape[1]} x {image.shape[0]}")
    st.write(f"Compressed Image: {compressed_image.shape[1]} x {compressed_image.shape[0]}")
    
    if st.button("Save and Download Compressed Image"):
        st.markdown(get_image_download_link(compressed_image), unsafe_allow_html=True)
        st.success("Click the link above to download the compressed image.")
