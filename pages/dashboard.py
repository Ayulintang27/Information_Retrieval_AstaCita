import streamlit as st
from component.styles import load_css
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


df = pd.read_csv("data/data_bersih_final.csv")
load_css()

def show_dashboard():
    st.markdown(
        """
        <div class="eyebrow">Insight Berita</div>
        <div class="page-title">Analisis Dataset</div>
        <div class="page-subtitle">
        Ringkasan statistik dan distribusi data pemberitaan Asta Cita.
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # =========================
    # METRIC
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Jumlah Berita",
            len(df)
        )

    with col2:
        st.metric(
            "Jumlah Poin",
            df["poin_id"].nunique()
        )

    with col3:
        st.metric(
            "Jumlah Keyword",
            df["keyword"].nunique()
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # WORDCLOUD
    # =========================
    st.subheader("Word Cloud Berita")
    text_data = " ".join(df["stopword_removal"].dropna().astype(str))

    wordcloud = WordCloud(
        width=800,
        height=350,
        background_color="white",
        collocations=False
    ).generate(text_data)

    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    _, wordcloud_col, _ = st.columns([1, 4, 1])
    with wordcloud_col:
        st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # =========================
    # DISTRIBUSI POIN
    # =========================
    st.subheader("Distribusi Berita per Poin Asta Cita")

    poin_counts = (
        df["poin_id"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(poin_counts)

    # =========================
    # DISTRIBUSI TAHUN
    # =========================
    st.subheader("Distribusi Berita per Tahun")

    df["date"] = pd.to_datetime(
    df["date"],
    format="%m/%d/%Y, %I:%M %p, %z UTC",
    errors="coerce"
    )
    df["year"] = df["date"].dt.year

    tahun_counts = (
        df["year"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(tahun_counts)


    # =========================
    # KEYWORD TERATAS
    # =========================
    st.subheader("Keyword Terbanyak")

    keyword_counts = (
        df["keyword"]
        .value_counts()
        .head(10)
    )

    st.dataframe(keyword_counts)

