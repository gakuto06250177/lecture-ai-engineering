import streamlit as st

st.set_page_config(
    page_title="Tesla, Inc. 企業概要",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Tesla, Inc. (テスラ)")
st.subheader("電気自動車(EV)とクリーンエネルギーのリーディングカンパニー")
st.markdown("""
Teslaは、アメリカ合衆国テキサス州オースティンに本社を置き、
電気自動車、バッテリーエネルギー貯蔵、太陽光パネル、関連製品およびサービスを設計・製造・販売する企業です。
**「持続可能なエネルギーへ、世界の移行を加速する」** ことをミッションに掲げています。
""")
st.divider()

tab_overview, tab_ev, tab_energy = st.tabs([
    "企業概要",
    "電気自動車 (EV) 事業",
    "エネルギー事業"
])

with tab_overview:
    st.header("企業概要")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("基本情報")
        st.markdown("""
        * **本社所在地:** アメリカ合衆国 テキサス州 オースティン
        * **CEO:** イーロン・マスク (Elon Musk)
        * **設立:** 2003年
        * **日本法人:** Tesla Japan合同会社
            * *(旧社名: Tesla Motors Japan合同会社、2024年5月に現社名へ変更)*
        """)
    with col2:
        st.subheader("ミッション")
        st.info("**「持続可能なエネルギーへ、世界の移行を加速する」**")
        st.write("単なる自動車製造に留まらず、エネルギー生成・貯蔵を含むエコシステム全体での変革を目指しています。")
    st.image("/content/lecture-ai-engineering/day1/01_streamlit_UI/assets/181010_tesla.png", use_container_width=True)

with tab_ev:
    st.header("電気自動車 (EV) 事業")
    st.write("Teslaの中核事業であり、革新的なEVを設計・製造・販売しています。")

    st.subheader("主な車種ラインナップ")
    col_s3, col_xy, col_cyber = st.columns(3)
    with col_s3:
        st.markdown("Model S")
        st.markdown("**Model 3**")
    with col_xy:
        st.markdown("**Model X**")
        st.markdown("**Model Y**")
    with col_cyber:
        st.markdown("**Cybertruck**")

    st.subheader("EV事業の特徴")
    st.markdown("""
    * **高性能・長航続距離:** パフォーマンスと実用性を両立。
    * **先進的なデザイン:** シンプルかつ未来的な内外装。
    * **独自の急速充電網:** 「スーパーチャージャー」ネットワークを世界展開。
    * **ソフトウェア中心設計:** OTA (Over-the-Air)アップデートによる機能向上。
    * **自動運転支援技術:**
        * **Autopilot (オートパイロット):** 標準的な運転支援機能。
        * **FSD (Full Self-Driving):** より高度な自動運転を目指すオプション機能 (開発中・地域により機能制限あり)。
    * **オンライン直販モデル:** ディーラーを介さない販売方式。
    """)

with tab_energy:
    st.header("エネルギー事業")
    st.write("EV事業と並行し、クリーンエネルギーの生成・貯蔵・利用を促進する製品を展開しています。")

    col_power, col_mega, col_solar = st.columns(3)
    with col_power:
        st.subheader("Powerwall (パワーウォール)")
        st.write("太陽光発電で生成した電力や、安価な深夜電力を貯蔵し、家庭でのエネルギー自給自足やピークカットに貢献します。")
    with col_mega:
        st.subheader("Megapack (メガパック)")
        st.write("電力会社や大規模施設向け。電力網の安定化や再生可能エネルギーの導入拡大を支援します。")
    with col_solar:
        st.subheader("太陽光発電")
        st.write("屋根材一体型の「Solar Roof」や、従来の太陽光パネルを提供し、エネルギー生成を担います。")

    st.info("これらの製品群により、Teslaはエネルギーの生成から貯蔵、消費（EV充電など）までを一貫してサポートするエコシステムを目指しています。")
