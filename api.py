import streamlit as st
import requests

st.set_page_config(
    page_title="Fake Store",
    page_icon="🛒",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.product-card {
    background-color: #1e1e1e;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
    height: 450px;
}

.product-card img {
    border-radius: 10px;
}

.price {
    color: #00ff88;
    font-size: 22px;
    font-weight: bold;
}

.category {
    color: #ffaa00;
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 YSL Store")
# st.write("Products fetched from FakeStore API")

# Fetch data
url = "https://fakestoreapi.com/products"

try:
    products = requests.get(url).json()

    # Search Box
    search = st.text_input("🔍 Search Product")

    if search:
        products = [
            p for p in products
            if search.lower() in p["title"].lower()
        ]

    cols = st.columns(3)

    for index, product in enumerate(products):

        with cols[index % 3]:
            st.image(product["image"], width=180)

            st.markdown(
                f"""
                <div class="product-card">
                    <h4>{product['title'][:50]}</h4>
                    <p class="category">{product['category']}</p>
                    <p>{product['description'][:100]}...</p>
                    <p class="price">${product['price']}</p>
                    ⭐ {product['rating']['rate']} ({product['rating']['count']} reviews)
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"View Details",
                key=product["id"]
            ):
                st.subheader(product["title"])
                st.image(product["image"], width=250)
                st.write(product["description"])
                st.success(f"Price: ${product['price']}")

except Exception as e:
    st.error(f"Error: {e}")