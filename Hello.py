import streamlit as st

# Exibindo o header "Precificador Shopee" estilizado com as cores Shopee
st.markdown("""
    <div style='background-color: #e81d17; color: white; border-radius: 8px; padding: 20px; text-align: center; font-size: 32px; font-weight: bold;'>
        Precificador Shopee
    </div>
""", unsafe_allow_html=True)

# Exibindo o divisor da mesma cor abaixo
st.markdown("""
    <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Input do valor de custo do produto
valor_custo_produto = col1.number_input(label='Digite o valor de Custo do Produto R$', step=0.05, value=0.001, min_value=0.0)

# Input do valor da embalagem
valor_embalagem = col2.radio(
    label='Escolha o valor da embalagem R$',
    options=[0.00, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50],
    index=0,
    horizontal=True
)

col3, col4 = st.columns(2)


valor_de_venda = col3.number_input(label='Valor de Venda', step=0.05, value=0.000, min_value=0.0)

# Calcula o custo total do produto
valor_total_custo = valor_custo_produto + valor_embalagem

col4.markdown(f"<h4 style='color: white; background-color: #f7452e; border-radius: 10px; padding: 25px; font-size: 26px;text-align: center;'   >Valor de Custo R$ {valor_total_custo:.2f}</h4>", unsafe_allow_html=True)

# Exibindo o divisor da mesma cor abaixo
st.markdown("""
    <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
""", unsafe_allow_html=True)


# Verifica se o valor de venda é menor que o custo total
if valor_de_venda < valor_total_custo:
    st.error("Valor de Venda não pode ser menor que o Custo do Produto!", icon='🚨')
    
else:
   # Exibindo o header "Precificador Shopee" estilizado com as cores Shopee
    st.markdown("""
    <div style='background-color: #e81d17; color: white; border-radius: 8px; padding: 20px; text-align: center; font-size: 32px; font-weight: bold;'>
       Analítico Shopee
    </div>
        """, unsafe_allow_html=True)
    
    # Exibindo o divisor da mesma cor abaixo
    st.markdown("""
    <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
    """, unsafe_allow_html=True)

    
    sh1, sh2 = st.columns(2)
    
    # Variaveis comissão fixa shopee
    valor_fixo = 4.00
    comissao = 22.00

    valor_comissao = ((valor_de_venda * comissao) / 100) + valor_fixo
    total_shopee = valor_total_custo + valor_comissao
    
    sh1.markdown(f"""
                <h4 style='color: white; background-color: #b40001; border-radius: 5px; padding:20px; font-size: 26px;text-align: center;'>Comissão Shopee R$ {valor_comissao:.2f}</h4>
                """, unsafe_allow_html=True)

    sh2.markdown(f"""                
                <h4 style='color: white; background-color:#b40001; border-radius: 5px; padding:20px; font-size: 26px;text-align: center;'>Custo P. + Shopee R$ {total_shopee:.2f}</h4><br>           
                """, unsafe_allow_html=True)
 
    
    final_pagamento = valor_de_venda - valor_comissao
    lucro_apos_comissao = round(valor_de_venda - (valor_total_custo + valor_comissao), 2)
    porcentagem_lucro = (lucro_apos_comissao / valor_de_venda) * 100 # Calcula o lucro em relação ao custo total

    fn1, fn2 = st.columns(2)
  
    if lucro_apos_comissao > 0:
        fn1.markdown(f"""                
                    <h4 style='color: white ; background-color: #000034; border-radius: 5px; padding:20px; font-size: 26px; ;text-align: center;'>Lucro : R$  {lucro_apos_comissao:.2f}</h4><br>           
                    """, unsafe_allow_html=True)
        fn2.markdown(f"""                
                    <h4 style='color: white; background-color:#000034; border-radius: 5px; padding:20px; font-size: 26px; text-align: center;'>Lucro % : {porcentagem_lucro:.2f}</h4><br>           
                    """, unsafe_allow_html=True)
            # Exibindo o divisor da mesma cor abaixo
        st.markdown("""
            <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
        """, unsafe_allow_html=True)

           
    else:
        st.markdown(f"""                
                    <h4 style='color: white; background-color: red; border-radius: 5px; padding:20px; font-size: 26px; text-align: center;'>Lucro da Operação: R$ {lucro_apos_comissao:.2f}</h4><br>           
                    """, unsafe_allow_html=True)
            # Exibindo o divisor da mesma cor abaixo
        st.markdown("""
        <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
        """, unsafe_allow_html=True)



