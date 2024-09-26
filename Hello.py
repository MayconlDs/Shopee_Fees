import streamlit as st

# Exibindo o header "Precificador Shopee" estilizado com as cores Shopee
st.markdown("""
    <div style='background-color: #e81d17; color: white; border-radius: 8px; padding: 2px; text-align: center; font-size: 32px; font-weight: bold;'>
        Calculadora Shopee
    </div>
""", unsafe_allow_html=True)

# Exibindo o divisor da mesma cor abaixo
st.markdown("""
    <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
""", unsafe_allow_html=True)

# Dividindo em 4 colunas
col1, col2, col3, col4 = st.columns(4)

# Input do valor de custo do produto
valor_custo_produto = col1.number_input(label='Valor Custo do Produto', step=0.05, value=0.000, min_value=0.0)

# Input do valor de venda do produto
valor_de_venda = col2.number_input(label='Valor de Venda', step=0.05, value=0.000, min_value=0.0)

# Input do valor da embalagem
valor_embalagem = col3.number_input(label='Valor Embalagem', step=0.05, value=1.000, min_value=0.0)

# Calcula o custo total do produto
valor_total_custo = valor_custo_produto + valor_embalagem

# Exibir o valor total de custo com formatação alinhada
col4.markdown(f"""
    <div style="text-align: center;">
        <label style='font-size: 12px; color: black;'>(=) Custo Produto + Embalagem</label><br>
        <h4 style='color: white; background-color: #b40001; border-radius: 10px; padding: 5px; font-size: 26px; width: 100%;'>R$ {valor_total_custo:.2f}</h4>
    </div>
    """, unsafe_allow_html=True)


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
    <div style='background-color: #e81d17; color: white; border-radius: 8px; padding: 2px; text-align: center; font-size: 32px; font-weight: bold;'>
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
                 <label style='font-size: 20px; display: block; text-align: center;'>(-) Comissão Shopee</label>
                <h4 style='color: white; background-color: #b40001; border-radius: 5px; padding:10px; font-size: 26px;text-align: center;'>R$ {valor_comissao:.2f}</h4>
                """, unsafe_allow_html=True)

    sh2.markdown(f"""
                <label style='font-size: 20px; display: block; text-align: center;'>(=) Custo Produto + Comissão Shopee</label>                
                <h4 style='color: white; background-color:#b40001; border-radius: 5px; padding:10px; font-size: 26px;text-align: center;'>R$ {total_shopee:.2f}</h4><br>           
                """, unsafe_allow_html=True)
 
    
    final_pagamento = valor_de_venda - valor_comissao
    lucro_apos_comissao = round(valor_de_venda - (valor_total_custo + valor_comissao), 2)
    porcentagem_lucro = (lucro_apos_comissao / valor_de_venda) * 100 # Calcula o lucro em relação ao custo total

    fn1, fn2 = st.columns(2)
  
    if lucro_apos_comissao > 0:
        fn1.markdown(f"""
                    <label style='font-size: 20px; display: block; text-align: center;'>(+) Lucro Operação</label>                
                    <h4 style='color: white ; background-color: #000034; border-radius: 5px; padding:16px; font-size: 30px; ;text-align: center;'>R$  {lucro_apos_comissao:.2f}</h4><br>           
                    """, unsafe_allow_html=True)
        fn2.markdown(f"""   
                    <label style='font-size: 20px; display: block; text-align: center;'>(%) Porcentagem de Ganho</label>               
                    <h4 style='color: white; background-color:#000034; border-radius: 5px; padding:16px; font-size: 30px; text-align: center;'>{porcentagem_lucro:.2f} %</h4><br>           
                    """, unsafe_allow_html=True)
            # Exibindo o divisor da mesma cor abaixo
        st.markdown("""
            <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
        """, unsafe_allow_html=True)

           
    else:
               
        st.markdown(f""" 
            <style>
                @keyframes pulse {{
                    0% {{
                        transform: scale(1);
                        background-color: red;
                    }}
                    50% {{
                        transform: scale(1.05);
                        background-color: #ff6347;
                    }}
                    100% {{
                        transform: scale(1);
                        background-color: red;
                    }}
                }}

                .animated-label {{
                    font-size: 26px;
                    display: block;
                    text-align: center;
                    background-color: red;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    animation: pulse 1.7s infinite;
                }}
            </style>

            <label class='animated-label'>Operação em Prejuizo</label>
                                  
            """, unsafe_allow_html=True)
        
        prejuizo, prejuizo2 = st.columns(2)
        
        prejuizo.markdown(f"""
                          <label style='font-size: 20px; display: block; text-align: center; color:black;'>(-) Lucro Operação</label>
                          <h4 style='color: white; background-color: #b40001; border-radius: 5px; padding:10px; font-size: 26px; text-align: center;'>R$ {lucro_apos_comissao:.2f}</h4><br>""", unsafe_allow_html=True)
        
        prejuizo2.markdown(f"""
                          <label style='font-size: 20px; display: block; text-align: center; color:black;'>(%) Porcentagem de Ganho</label>
                          <h4 style='color: white; background-color: #b40001; border-radius: 5px; padding:10px; font-size: 26px; text-align: center;'>{porcentagem_lucro:.2f} %</h4><br>""", unsafe_allow_html=True)
        
            # Exibindo o divisor da mesma cor abaixo
        st.markdown("""
                    
        <hr style='border: 1px solid #ffb16f; border-radius: 5px;'>
        """, unsafe_allow_html=True)




