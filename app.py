import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import pandas as pd
from AlohaProtocol import pureAloha
from AlohaProtocol import slottedAloha
from CSMAProtocol import nonPersistent
from CSMAProtocol import onePersistent
from CSMAProtocol import pPersistent

from plotMax import annot_max


def main():
    st.title('Carrier Sense Multiple-Access Modes')
    st.sidebar.title('Throughput-Delay Characteristics')
    st.markdown('👻 compare slotted ALOHA, pure ALOHA, non-persistent CSMA, 1-persistent CSMA, and p-persistent CSMA')
    st.sidebar.subheader("Choose the model and Plot out the Throughput")

    st.sidebar.markdown('Choose the Model and Set Parameters 👀')
    models = st.sidebar.selectbox(
        "Models",
        (
            "default",
            "Pure Aloha",
            "Slotted Aloha",
            "Non-persistent CSMA",
            "1-persistent CSMA",
            "P-persistent CSMA")
    )
    compare_model = st.sidebar.selectbox(
        "Compare",
        (
            "default",
            "1-persistent VS. P-persistent",
            "Compare all 5"
        )
    )
    G = np.arange(start=0, stop=100, step=0.01)
    if models == 'default':
        pass
    if models == 'Pure Aloha':
        st.subheader('⭐ Pure Aloha ')
        S_pA = pureAloha.pure_aloha(G)
        max_S_pA = np.amax(S_pA)
        index_G = np.where(S_pA == max_S_pA)
        G_max_index = int(index_G[0])
        st.write("Max Throughput: ", round(max_S_pA, 4))
        st.write("Reaches Max Throughput when G equals: ", G[G_max_index])

        if st.sidebar.button('Plot', key='Plot'):
            p = figure(
                title='Throughput for Pure Aloha',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )
            p.line(G, S_pA, legend='pure_aloha', line_width=2)
            st.bokeh_chart(p, use_container_width=True)

    if models == 'Slotted Aloha':
        st.subheader('⭐ Slotted Aloha')
        S_sA = slottedAloha.slotted_aloha(G)
        max_S_sA = np.amax(S_sA)
        index_G = np.where(S_sA == max_S_sA)
        G_max_index = int(index_G[0])
        st.write("Max Throughput: ", round(max_S_sA, 4))
        st.write("Reaches Max Throughput when G equals: ", G[G_max_index])
        if st.sidebar.button('Plot', key='Plot'):
            p = figure(
                title='Throughput for Slotted Aloha',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )
            p.line(G, S_sA, legend='slotted_aloha', line_width=2)
            st.bokeh_chart(p, use_container_width=True)

    if models == 'Non-persistent CSMA':
        st.subheader('⭐ Non-persistent CSMA')
        S_np = nonPersistent.nonP_CSMA(G)
        max_S_np = np.amax(S_np)
        index_G = np.where(S_np == max_S_np)
        G_max_index = int(index_G[0])
        st.write("Max Throughput: ", round(max_S_np, 4))
        st.write("Reaches Max Throughput when G equals: ", G[G_max_index])
        if st.sidebar.button('Plot', key='Plot'):
            p = figure(
                title='Throughput for Non-persistent CSMA',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )
            p.line(G, S_np, legend='Non-persistent CSMA', line_width=2)
            st.bokeh_chart(p, use_container_width=True)

    if models == '1-persistent CSMA':
        st.subheader('⭐ One-persistent CSMA')
        S_op = onePersistent.oneP_CSMA(G)
        max_S_op = np.amax(S_op)
        index_G = np.where(S_op == max_S_op)
        G_max_index = int(index_G[0])
        st.write("Max Throughput: ", round(max_S_op, 4))
        st.write("Reaches Max Throughput when G equals: ", round(G[G_max_index], 4))
        if st.sidebar.button('Plot', key='Plot'):
            p = figure(
                title='Throughput for 1-persistent CSMA',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )
            p.line(G, S_op, legend='1-persistent CSMA', line_width=2)
            st.bokeh_chart(p, use_container_width=True)

    if models == 'P-persistent CSMA':
        st.subheader('⭐ P-persistent CSMA')
        st.sidebar.subheader("Model Hyperparameters")
        a_csma = st.sidebar.number_input("a: the ratio of propagation delay "
                                         "to packet transmission time",
                                         0.01, 1.00, step=0.01, key='a_csma')
        p_csma = st.sidebar.slider("p: probablity", 0.01, 1.00, key='p_csma')
        S_pP = pPersistent.oneP_CSMA(G, p_csma, a_csma)
        max_S_pP = np.amax(S_pP)
        index_G = np.where(S_pP == max_S_pP)
        G_max_index = int(index_G[0])
        st.write("Max Throughput: ", round(max_S_pP, 4))
        st.write("Reaches Max Throughput when G equals: ", round(G[G_max_index], 4))
        if st.sidebar.button('Plot', key='Plot'):
            p = figure(
                title='Throughput for P-persistent CSMA',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )
            p.line(G, S_pP, legend='P-persistent CSMA', line_width=2)
            st.bokeh_chart(p, use_container_width=True)

    if compare_model == 'default':
        pass

    if compare_model == '1-persistent VS. P-persistent':
        st.subheader('⭐ Compare 1-persistent VS. P-persistent CSMA')
        st.sidebar.subheader("Model Hyperparameters")
        a_csma = st.sidebar.number_input("a: the ratio of propagation delay "
                                         "to packet transmission time",
                                         0.01, 1.00, step=0.01, key='a_csma')
        p_csma = st.sidebar.slider("p: probablity", 0.01, 1.00, key='p_csma')

        S_op = onePersistent.oneP_CSMA(G)
        max_S_op = np.amax(S_op)
        index_G = np.where(S_op == max_S_op)
        G_max_index = int(index_G[0])
        st.write("1-persistent CSMA: ")
        st.write("Max Throughput: ", round(max_S_op, 4))
        st.write("Reaches Max Throughput when G equals: ", round(G[G_max_index], 4))

        S_pP = pPersistent.oneP_CSMA(G, p_csma, a_csma)
        max_S_pP = np.amax(S_pP)
        index_G = np.where(S_pP == max_S_pP)
        G_max_index = int(index_G[0])
        st.write("P-persistent CSMA: ")
        st.write("Max Throughput: ", round(max_S_pP, 4))
        st.write("Reaches Max Throughput when G equals: ", round(G[G_max_index], 4))

        if st.sidebar.button('Plot', key='Plot_CompareModel'):
            p = figure(
                title='Throughput for P-persistent CSMA',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )
            p.line(G, S_pP, legend='P-persistent CSMA', line_width=2, color="olive")
            p.line(G, S_op, legend='1-persistent CSMA', line_width=2, color="navy")
            st.bokeh_chart(p, use_container_width=True)

    if compare_model == 'Compare all 5':
        st.subheader('⭐ Compare all 5 Models')
        st.sidebar.subheader("Model Hyperparameters")
        a_csma = st.sidebar.number_input("a: the ratio of propagation delay "
                                         "to packet transmission time",
                                         0.01, 1.00, step=0.01, key='a_csma')
        p_csma = st.sidebar.slider("p: probablity", 0.01, 1.00, key='p_csma')

        S_pA = pureAloha.pure_aloha(G)
        max_S_pA = np.amax(S_pA)
        index_G_pa = np.where(S_pA == max_S_pA)
        G_max_index_pa = int(index_G_pa[0])

        S_sA = slottedAloha.slotted_aloha(G)
        max_S_sA = np.amax(S_sA)
        index_G_sa = np.where(S_sA == max_S_sA)
        G_max_index_sa = int(index_G_sa[0])

        S_np = nonPersistent.nonP_CSMA(G)
        max_S_np = np.amax(S_np)
        index_G_np = np.where(S_np == max_S_np)
        G_max_index_np = int(index_G_np[0])


        S_op = onePersistent.oneP_CSMA(G)
        max_S_op = np.amax(S_op)
        index_G_op = np.where(S_op == max_S_op)
        G_max_index_op = int(index_G_op[0])

        S_pP = pPersistent.oneP_CSMA(G, p_csma, a_csma)
        max_S_pP = np.amax(S_pP)
        index_G_pp = np.where(S_pP == max_S_pP)
        G_max_index_pp = int(index_G_pp[0])

        index = ['Pure Aloha',
                 'Slotted Aloha',
                 'Non-persistent CSMA',
                 '1-persistent CSMA',
                 'P-persistent CSMA']
        df = pd.DataFrame(
            data=[[max_S_pA, G[G_max_index_pa]],
                  [max_S_sA, G[G_max_index_sa]],
                  [max_S_np, G[G_max_index_np]],
                  [max_S_op, G[G_max_index_op]],
                  [max_S_pP, G[G_max_index_pp]]],
            columns=('Max Throughput', 'Corresponding G'),
            index=index
        )
        st.dataframe(df)

        if st.sidebar.button('Plot', key='Plot_CompareModel'):
            p = figure(
                title='Throughput for P-persistent CSMA',
                x_axis_label='G (Offered Channel Traffic)',
                y_axis_label='S (Throughput)'
            )

            p.line(G, S_pA, legend='Pure Aloha', line_width=2, color="#B3DE69")
            p.line(G, S_sA, legend='Slotted Aloha', line_width=2, color="grey")
            p.line(G, S_np, legend='Non-persistent CSMA', line_width=2, color="firebrick")
            p.line(G, S_pP, legend='P-persistent CSMA', line_width=2, color="olive")
            p.line(G, S_op, legend='1-persistent CSMA', line_width=2, color="navy")
            st.bokeh_chart(p, use_container_width=True)


if __name__ == '__main__':
    main()
