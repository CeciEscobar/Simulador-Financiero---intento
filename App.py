import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests


# Diccionario con una breve descripción de las criptomonedas
crypto_descriptions = {
    "BTC-USD": "Bitcoin es la primera criptomoneda y se utiliza principalmente como una reserva de valor y para pagos.",
    "ETH-USD": "Ethereum es una plataforma de contratos inteligentes que permite la creación de aplicaciones descentralizadas.",
    "XRP-USD": "Ripple (XRP) se utiliza principalmente en el sistema financiero para pagos transfronterizos rápidos y baratos.",
    "LTC-USD": "Litecoin es una criptomoneda diseñada para ser más rápida y más barata de usar que Bitcoin.",
    "ADA-USD": "Cardano es una plataforma de blockchain que se utiliza para desarrollar contratos inteligentes y aplicaciones descentralizadas.",
    "SOL-USD": "Solana es una plataforma blockchain que soporta aplicaciones descentralizadas y criptomonedas, enfocándose en transacciones rápidas.",
    "DOGE-USD": "Dogecoin es una criptomoneda que comenzó como una broma pero ha ganado popularidad como una moneda para microtransacciones.",
    "BNB-USD": "Binance Coin es una criptomoneda creada por el intercambio Binance y se utiliza principalmente para reducir tarifas dentro de la plataforma Binance.",
    "USDT-USD": "Tether es una stablecoin cuyo valor está respaldado 1:1 por el dólar estadounidense.",
    "MATIC-USD": "Polygon es una plataforma que conecta redes de blockchain compatibles con Ethereum, mejorando la escalabilidad de estas aplicaciones."
}

# Descargar datos globalmente antes de las funciones
cryptos = ["BTC-USD", "ETH-USD", "XRP-USD", "LTC-USD", "ADA-USD", "SOL-USD", "DOGE-USD", "BNB-USD", "USDT-USD", "MATIC-USD"]
try:
    data = yf.download(cryptos, period="1y", group_by='ticker')
except Exception as e:
    data = None
    st.error(f"Error al descargar los datos: {e}")

# Función para graficar el precio de las criptomonedas
def plot_crypto_price(crypto_data, crypto_name):
    st.subheader(f"Gráfico de precios de {crypto_name}")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(crypto_data.index, crypto_data['Close'], label=f"Precio de {crypto_name}", color='b')
    ax.set_title(f"Precio de {crypto_name} en el último año")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio (USD)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Función de bienvenida
def show_welcome():
    st.title("Bienvenido al Curso Express de Criptomonedas 💰")
    st.subheader("¡Comienza tu aprendizaje sobre criptomonedas de manera rápida y fácil! 🚀")
    st.write("Por favor, ingresa tus datos para acceder al curso.")

    with st.form(key='user_info'):
        name = st.text_input("Nombre")
        last_name = st.text_input("Apellido")
        email = st.text_input("Correo Electrónico")
        newsletter = st.checkbox("¿Quieres recibir un newsletter semanal sobre criptomonedas?")
        submit_button = st.form_submit_button(label="Registrarse")

    if submit_button:
        st.session_state.registered = True
        st.session_state.name = name
        st.session_state.newsletter = newsletter
        st.write(f"Hola {name}, bienvenido al curso de Criptomonedas. ¡Nos alegra tenerte con nosotros!")
        if newsletter:
            st.write("Te suscribiste al newsletter semanal.")


# Información sobre qué son las criptomonedas
def show_crypto_info():
    st.title("¿Qué son las Criptomonedas?")
    st.write("""
        Las criptomonedas son monedas digitales que utilizan criptografía para garantizar transacciones seguras. A diferencia de las monedas tradicionales, las criptomonedas no están controladas por un gobierno o una entidad central, lo que las hace descentralizadas. Se basan en una tecnología llamada blockchain o cadena de bloques, que es un registro público y descentralizado donde se almacenan todas las transacciones realizadas con cada criptomoneda.

        **Características clave de las criptomonedas:**
        - **Descentralización:** No dependen de una autoridad central como un banco o gobierno.
        - **Seguridad:** Utilizan criptografía avanzada para garantizar la seguridad de las transacciones.
        - **Anonimato:** Las transacciones pueden realizarse de forma anónima, aunque no necesariamente.
        - **Transparencia:** Todas las transacciones están registradas en la blockchain, que es pública.
        - **Transferencia rápida y global:** Las criptomonedas pueden enviarse a cualquier parte del mundo rápidamente y con bajas comisiones.
        
        **Relevancia de las Criptomonedas:**
        Las criptomonedas han ganado relevancia en la última década debido a su potencial para revolucionar los sistemas financieros tradicionales. Son vistas como una forma de inversión y como un medio de pago en línea. A pesar de su alta volatilidad, muchas instituciones financieras y empresas están comenzando a adoptarlas. Además, la tecnología blockchain tiene aplicaciones más allá de las criptomonedas, como contratos inteligentes y finanzas descentralizadas (DeFi).

        **¿Por qué son importantes las criptomonedas?**
        - **Inversiones:** Muchos las consideran una forma alternativa de inversión.
        - **Tecnología:** La blockchain puede cambiar la forma en que realizamos transacciones y almacenamos datos.
        - **Inclusión financiera:** Las criptomonedas pueden ayudar a las personas que no tienen acceso a servicios bancarios a participar en la economía global.
    """)

# Historia de las criptomonedas
def show_crypto_history():
    st.title("Historia de las Criptomonedas")
    st.write("""
        Las criptomonedas nacieron en 2009 con el Bitcoin, el primer activo digital descentralizado, creado por una persona o grupo bajo el seudónimo de Satoshi Nakamoto. Desde entonces, las criptomonedas han recorrido un largo camino, pasando por momentos de auge y crisis. Aquí te presentamos una línea del tiempo de los principales eventos de las criptomonedas:

        **Línea del Tiempo:**
        - **2008:** Satoshi Nakamoto publica el libro blanco de Bitcoin, donde describe cómo funcionaría el primer sistema de pago digital descentralizado.
        - **2009:** Bitcoin es lanzado y se realiza la primera transacción con BTC.
        - **2011:** Aparecen nuevas criptomonedas como Litecoin y Namecoin.
        - **2013:** El precio del Bitcoin alcanza los $100 por primera vez.
        - **2017:** Ethereum se convierte en la segunda criptomoneda más popular, y el mercado de criptomonedas alcanza su mayor auge hasta ese momento.
        - **2018-2019:** El mercado de criptomonedas experimenta una gran caída, conocida como "criptoinvierno".
        - **2021:** Las criptomonedas alcanzan nuevos máximos históricos, con Bitcoin superando los $60,000 y empresas grandes como Tesla invirtiendo en criptomonedas.
        - **2022-2024:** Las criptomonedas siguen siendo relevantes a pesar de las fluctuaciones del mercado, con cada vez más adopción institucional y el crecimiento de las finanzas descentralizadas (DeFi).
    """)

# Mostrar información de criptomonedas
def show_relevant_cryptos():
    if data is not None:
        st.title("Criptomonedas Más Relevantes")
    st.write("""
        **Marcadores más Relevantes:**
        - **Apertura:** Precio de la criptomoneda al inicio del día.
        - **Máximo del Día:** Precio más alto alcanzado durante el día.
        - **Mínimo del Día:** Precio más bajo alcanzado durante el día.
        - **Cierre:** Precio de la criptomoneda al final del día.
        - **Volumen:** Cantidad de la criptomoneda transaccionada durante el día.
        - **Capitalización de Mercado:** Valor total de todas las unidades de la criptomoneda en circulación.
        
        Selecciona la criptomoneda de tu interes para conocer mas sobre ella:

    """)
    selected_crypto = st.selectbox("Selecciona una criptomoneda para ver más detalles:", cryptos)

    if selected_crypto:
            description = crypto_descriptions.get(selected_crypto, "No hay descripción disponible.")
            crypto_data = data[selected_crypto]
            latest_data = crypto_data.iloc[-1]
            price = latest_data['Close']
            change = latest_data['Close'] - crypto_data['Close'].iloc[0]
            change_percent = (change / crypto_data['Close'].iloc[0]) * 100
            volume = latest_data['Volume']

            st.write(f"**Descripción:** {description}")
            st.write(f"**Precio Actual:** ${price:,.2f}")
            st.write(f"**Cambio en %:** {change_percent:,.2f}%")
            st.write(f"**Volumen:** {volume:,.0f}")
            plot_crypto_price(crypto_data, selected_crypto)

# Simulación financiera Criptos
def show_financial_simulator():
    st.title("Simulador Financiero")

    # Selección de la criptomoneda
    selected_crypto = st.selectbox("Selecciona una criptomoneda para simular:", cryptos)

    # Entrada del usuario: monto a invertir y tiempo de simulación
    investment = st.number_input("Monto a invertir ($USD):", min_value=0.0, value=1000.0)
    simulation_period = st.selectbox("Período de simulación:", ["1 mes", "3 meses", "6 meses", "1 año"])

    # Mapear los períodos seleccionados a valores numéricos
    periods_map = {"1 mes": 30, "3 meses": 90, "6 meses": 180, "1 año": 365}
    simulation_days = periods_map[simulation_period]

    if selected_crypto and investment > 0:
        # Extraer datos de la criptomoneda seleccionada
        crypto_data = data[selected_crypto]
        returns = crypto_data['Close'].pct_change().dropna()

        # Calcular métricas de riesgo, rendimiento y Sharpe
        mean_return = returns.mean() * simulation_days
        risk = returns.std() * (simulation_days ** 0.5)
        sharpe_ratio = mean_return / risk if risk != 0 else 0

        # Simulación de valor futuro
        future_value = investment * (1 + mean_return)

        # Mostrar resultados
        st.subheader(f"Resultados para {selected_crypto}:")
        st.write(f"**Rendimiento promedio estimado ({simulation_period}):** {mean_return:.2%}")
        st.write(f"**Riesgo (desviación estándar):** {risk:.2%}")
        st.write(f"**Ratio de Sharpe:** {sharpe_ratio:.2f}")
        st.write(f"**Valor futuro estimado:** ${future_value:,.2f}")

        # Graficar riesgo vs rendimiento
        st.subheader("Comparativa de Riesgo vs Rendimiento")
        fig, ax = plt.subplots()
        for crypto in cryptos:
            crypto_returns = data[crypto]['Close'].pct_change().dropna()
            mean_ret = crypto_returns.mean() * simulation_days
            std_dev = crypto_returns.std() * (simulation_days ** 0.5)
            ax.scatter(std_dev, mean_ret, label=crypto)

        ax.scatter(risk, mean_return, color='red', label=f"{selected_crypto} (Seleccionado)", s=100)
        ax.set_title("Riesgo vs Rendimiento")
        ax.set_xlabel("Riesgo (Desviación estándar)")
        ax.set_ylabel("Rendimiento promedio")
        ax.legend()
        st.pyplot(fig)

    else:
        st.write("Por favor, selecciona una criptomoneda y define un monto a invertir.")

    # Agregar una línea divisora en Markdown
    st.markdown('---')

    st.title("Portafolio de Criptomonedas")
    st.write("""
        En este simulador, puedes crear un portafolio de criptomonedas eligiendo hasta 4 de las siguientes criptomonedas y asignando porcentajes a cada una.
            Los porcentajes deben sumar 100%.
        """)

        # Seleccionar hasta 4 criptomonedas
    selected_cryptos = st.multiselect(
            "Selecciona hasta 4 criptomonedas para tu portafolio:",
            cryptos,
            max_selections=4
        )

        # Asignar porcentajes a cada criptomoneda
    if len(selected_cryptos) > 0:
            st.write("Por favor, asigna un porcentaje a cada criptomoneda, asegurándote de que la suma total sea 100%.")
            percentages = []
            total_percentage = 0

                    # Input para porcentajes de cada criptomoneda seleccionada
            for crypto in selected_cryptos:
                percentage = st.slider(f"Porcentaje para {crypto}", min_value=0, max_value=100, value=25)
                percentages.append(percentage)
                total_percentage += percentage

            # Verificar que la suma de los porcentajes sea 100%
            if total_percentage != 100:
                st.warning("La suma total de los porcentajes debe ser igual a 100%.")
            else:
                # Calcular el rendimiento y riesgo del portafolio
                st.write("Cálculos de rendimiento y riesgo del portafolio:")

                # Descargar datos históricos
                crypto_data = {crypto: data[crypto]['Close'] for crypto in selected_cryptos}
                returns = pd.DataFrame(crypto_data).pct_change().dropna()

                # Calcular el rendimiento esperado (media diaria)
                expected_returns = returns.mean()

                # Calcular la matriz de covarianza (riesgo)
                cov_matrix = returns.cov()

                # Calcular el rendimiento y el riesgo ponderado del portafolio
                weighted_returns = np.dot(expected_returns, np.array(percentages) / 100)
                weighted_risk = np.sqrt(np.dot(np.array(percentages) / 100, np.dot(cov_matrix, np.array(percentages) / 100)))

                # Mostrar los resultados
                st.write(f"**Rendimiento esperado del portafolio (anualizado):** {weighted_returns * 252:.2f}%")
                st.write(f"**Riesgo del portafolio (desviación estándar anualizada):** {weighted_risk * np.sqrt(252):.2f}%")

                # Graficar riesgo vs. rendimiento
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(weighted_risk * np.sqrt(252), weighted_returns * 252, color='r')
                ax.set_title("Rendimiento vs Riesgo del Portafolio")
                ax.set_xlabel("Riesgo (Desviación Estándar)")
                ax.set_ylabel("Rendimiento (%)")
                ax.grid(True)
                st.pyplot(fig)

                st.write("Este gráfico muestra el rendimiento frente al riesgo del portafolio seleccionado.")

# Noticias de yahoo finance sobre criptomonedas
def get_crypto_news():
        api_key = 'e1d5333461b440e1afc9302a262a65e8'  # Tu API Key de NewsAPI
        url = f'https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={api_key}'
        
        # Realizar la solicitud HTTP a NewsAPI
        response = requests.get(url)
        
        if response.status_code == 200:
            news_data = response.json()
            
            if news_data['status'] == 'ok':
                # Obtener las noticias
                articles = news_data['articles']
                news_list = []
                
                for article in articles[:5]:  # Obtener las primeras 5 noticias
                    title = article['title']
                    description = article['description']
                    url = article['url']
                    source = article['source']['name']
                    
                    news_list.append({
                        'title': title,
                        'description': description,
                        'url': url,
                        'source': source
                    })
                
                return news_list
            else:
                st.error("Error en la respuesta de la API.")
                return []
        else:
            st.error(f"Error al obtener noticias: {response.status_code}")
            return []

    # Función para mostrar las noticias en Streamlit
def show_crypto_news():
        st.title("Noticias sobre Criptomonedas")

        # Obtener las noticias
        articles = get_crypto_news()

        if articles:
            for article in articles:
                st.subheader(article['title'])
                st.write(article['description'])
                st.write(f"[Leer más]({article['url']}) - Fuente: {article['source']}")
                st.write("---")
        else:
            st.write("No se encontraron noticias sobre criptomonedas.")

    # Llamar a la función para mostrar las noticias
        show_crypto_news()

# Preguntas Frecuentes
def show_faq():
    st.title("Preguntas Frecuentes")
    # Lista de preguntas frecuentes
    questions = [
        "¿Qué es el valor Sharpe y cómo se calcula?",
        "¿Si soy adverso al riesgo, puedo invertir en criptomonedas?",
        "¿Qué son las criptomonedas?",
        "¿Qué es el Bitcoin?",
        "¿Es seguro invertir en criptomonedas?",
        "¿Cómo puedo comprar criptomonedas?",
        "¿Qué es un monedero o wallet de criptomonedas?",
        "¿Cómo se protegen mis criptomonedas?",
        "¿Qué es una blockchain?",
        "¿Cuáles son las criptomonedas más populares?",
        "¿Qué es la minería de criptomonedas?",
        "¿Cuál es el futuro de las criptomonedas?",
        "¿Qué riesgos tiene invertir en criptomonedas?",
        "¿Cómo saber si una criptomoneda es una estafa?",
        "¿Qué significa ser un inversor a largo plazo en criptomonedas?"
    ]
            

    # Seleccionar una pregunta con un identificador único
    selected_question = st.selectbox(
        "Selecciona una pregunta", questions, key="faq_selectbox"
    )

            # Responder a las preguntas
    if selected_question == "¿Qué es el valor Sharpe y cómo se calcula?":
                st.write("""
                    El **valor Sharpe** es una medida de rentabilidad ajustada por riesgo. Se calcula usando la fórmula:
                    \[
                    \text{Sharpe} = \frac{R_p - R_f}{\sigma_p}
                    \]
                    Donde:
                    - \( R_p \) es el rendimiento esperado de la inversión.
                    - \( R_f \) es el rendimiento libre de riesgo.
                    - \( \sigma_p \) es la volatilidad de la inversión.

                    Un valor Sharpe alto indica que la inversión ofrece buenos rendimientos en relación con el riesgo asumido.
                """)
            
    elif selected_question == "¿Si soy adverso al riesgo, puedo invertir en criptomonedas?":
                st.write("""
                    Las criptomonedas son **muy volátiles**, lo que significa que tienen un alto nivel de riesgo. 
                    Si eres adverso al riesgo, invertir en criptomonedas puede no ser adecuado para ti debido a la 
                    posibilidad de grandes pérdidas. Sin embargo, si decides invertir, es importante hacerlo de forma 
                    cautelosa y solo invertir una parte pequeña de tu portafolio que puedas permitirte perder.
                """)
            
    elif selected_question == "¿Qué son las criptomonedas?":
                st.write("""
                    Las **criptomonedas** son monedas digitales que utilizan tecnología de criptografía para asegurar las transacciones y controlar la creación de nuevas unidades. 
                    Son descentralizadas y no están controladas por ninguna entidad central como los bancos. El Bitcoin es el ejemplo más conocido.
                """)
            
    elif selected_question == "¿Qué es el Bitcoin?":
                st.write("""
                    El **Bitcoin (BTC)** es la primera criptomoneda creada en 2009 por un individuo o grupo bajo el pseudónimo de **Satoshi Nakamoto**. 
                    Es una moneda digital que se utiliza para transacciones en línea y se basa en una tecnología llamada **blockchain**.
                """)
            
    elif selected_question == "¿Es seguro invertir en criptomonedas?":
                st.write("""
                    Invertir en criptomonedas implica un alto nivel de **riesgo**. Aunque la tecnología blockchain es segura, 
                    las criptomonedas son susceptibles a **fluctuaciones de precio** muy grandes, y hay riesgos de **fraude**, **hackeos** 
                    y **regulaciones cambiantes**. Es fundamental investigar y entender bien los riesgos antes de invertir.
                """)
            
    elif selected_question == "¿Cómo puedo comprar criptomonedas?":
                st.write("""
                    Puedes comprar criptomonedas a través de **exchanges** (plataformas de intercambio) como **Coinbase**, **Binance** o **Kraken**.
                    Normalmente necesitarás crear una cuenta en el exchange, depositar dinero (por ejemplo, en pesos o dólares) y luego realizar la compra de criptomonedas.
                """)
            
    elif selected_question == "¿Qué es un monedero o wallet de criptomonedas?":
                st.write("""
                    Un **monedero de criptomonedas** (o **wallet**) es una herramienta que te permite almacenar y gestionar tus criptomonedas.
                    Pueden ser **software** (en tu computadora o teléfono) o **hardware** (dispositivos físicos). 
                    Los monederos almacenan las claves privadas que te permiten acceder a tus criptomonedas.
                """)
            
    elif selected_question == "¿Cómo se protegen mis criptomonedas?":
                st.write("""
                    Las criptomonedas se protegen mediante **criptografía**. Además, es recomendable almacenar tus criptomonedas en monederos **seguros** 
                    y utilizar **autenticación de dos factores**. No compartas nunca tus claves privadas con nadie y haz copias de seguridad de tus claves.
                """)
            
    elif selected_question == "¿Qué es una blockchain?":
                st.write("""
                    La **blockchain** es una tecnología de registro descentralizado y transparente que permite realizar transacciones de manera segura.
                    Es la base de las criptomonedas y garantiza que las transacciones no puedan ser alteradas una vez confirmadas.
                """)
            
    elif selected_question == "¿Cuáles son las criptomonedas más populares?":
                st.write("""
                    Las criptomonedas más populares incluyen **Bitcoin (BTC)**, **Ethereum (ETH)**, **Binance Coin (BNB)**, **Cardano (ADA)**, 
                    **Solana (SOL)**, y **Ripple (XRP)**, entre otras.
                """)
            
    elif selected_question == "¿Qué es la minería de criptomonedas?":
                st.write("""
                    La **minería de criptomonedas** es el proceso por el cual se validan las transacciones y se agregan a la blockchain. 
                    Los mineros usan potentes computadoras para resolver complejos problemas matemáticos y obtener recompensas en forma de criptomonedas.
                """)
            
    elif selected_question == "¿Cuál es el futuro de las criptomonedas?":
                st.write("""
                    El futuro de las criptomonedas es incierto, pero se espera que su adopción crezca a medida que más personas y empresas 
                    comprendan sus beneficios. Sin embargo, la **regulación** y la **volatilidad** podrían afectar su evolución.
                """)
            
    elif selected_question == "¿Qué riesgos tiene invertir en criptomonedas?":
                st.write("""
                    Los riesgos incluyen **alta volatilidad**, **fraude**, **falta de regulación**, y **pérdida de fondos** debido a ataques cibernéticos o errores humanos.
                    Es importante investigar y estar preparado para la posible pérdida total de la inversión.
                """)
            
    elif selected_question == "¿Cómo saber si una criptomoneda es una estafa?":
                st.write("""
                    Para evitar las estafas, investiga sobre la criptomoneda antes de invertir. Busca información sobre su **equipo de desarrollo**, 
                    **comunidad**, y **caso de uso**. Desconfía de promesas de retornos altos sin riesgo y proyectos sin transparencia.
                """)
            
    elif selected_question == "¿Qué significa ser un inversor a largo plazo en criptomonedas?":
                st.write("""
                    Ser un **inversor a largo plazo** en criptomonedas significa comprar y mantener criptomonedas con la esperanza de que 
                    su valor aumente a largo plazo. Este enfoque minimiza la exposición a la volatilidad diaria, pero todavía conlleva riesgos.
                """)



# Función principal
def main():
    # Si ya está registrado, no mostrar la bienvenida
    if not st.session_state.get('registered', False):
        show_welcome()
    else:
        # Menú desplegable en el lado izquierdo
        st.sidebar.markdown('<h2 style="text-align: center;">Descubre lo que tenemos para ofrecerte</h2>', unsafe_allow_html=True)
        option = st.sidebar.selectbox(
            "Selecciona una sección:",
            (
                "¿Qué son las Criptomonedas?",
                "Historia de las Criptomonedas",
                "Criptomonedas Más Relevantes",
                "Simulador Financiero",
                "Noticias Relevantes sobre Criptomonedas",
                "Preguntas Frecuentes"
            )
        )

        # Navegación entre las secciones
        if option == "¿Qué son las Criptomonedas?":
            show_crypto_info()
        elif option == "Historia de las Criptomonedas":
            show_crypto_history()
        elif option == "Criptomonedas Más Relevantes":
            show_relevant_cryptos()
        elif option == "Simulador Financiero":
            show_financial_simulator()
        elif option == "Noticias Relevantes sobre Criptomonedas":
            show_crypto_news()
        elif option == "Preguntas Frecuentes":
            show_faq()

if __name__ == "__main__":
    main()
    


