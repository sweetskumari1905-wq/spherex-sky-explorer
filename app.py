import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="SPHEREx Sky Explorer",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 SPHEREx Sky Explorer")
st.subheader("Astronomical Image Processing and Source Detection")

st.info(
    "Current demonstration dataset: WISE preliminary test image. "
    "SPHEREx integration is planned future work."
)

folder = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(folder, "WISE_processed.npy")
catalogue_path = os.path.join(
    folder, "source_catalogue_with_coordinates.csv"
)

image = np.load(image_path)
catalogue = pd.read_csv(catalogue_path)

c1, c2, c3 = st.columns(3)

c1.metric("Detected Sources", len(catalogue))
c2.metric("Image Width", image.shape[1])
c3.metric("Image Height", image.shape[0])

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Processed WISE Image")
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.imshow(image, cmap="inferno", origin="lower")
    ax.set_title("WISE Astronomical Image")
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.markdown("### Source Detection")
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.imshow(image, cmap="inferno", origin="lower")
    ax.scatter(
        catalogue["x_centroid"],
        catalogue["y_centroid"],
        s=60,
        facecolors="none",
        edgecolors="cyan"
    )
    ax.set_title("Detected Astronomical Sources")
    st.pyplot(fig)
    plt.close(fig)

st.markdown("### Source Catalogue")
st.dataframe(catalogue, use_container_width=True)

st.download_button(
    "Download Source Catalogue",
    catalogue.to_csv(index=False),
    "WISE_source_catalogue.csv",
    "text/csv"
)
