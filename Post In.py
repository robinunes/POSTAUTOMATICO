#!/usr/bin/env python
# coding: utf-8

# # Post automático no LinkedIn

# In[1]:


import pyautogui
import pyperclip


# In[9]:


pyautogui.PAUSE = 7

pyautogui.hotkey("ctrl", "t")
pyperclip.copy ("linkedin.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")

pyautogui.click (x=873, y=226)

mensagem = """Essa mensagem foi postada automaticamente com Python!

E não foi a única coisa que automatizei com Python hoje. Há algum tempo, montei um projeto para gerar automaticamente pdf's com orçamento de serviços de social media, em um template adequado para enviar ao cliente.

Hoje incrementei ao meu código, a tarefa de automatizar o envio do email ao cliente, contendo na mensagem os dados do orçamento além de anexar o template bonitinho e mais detalhado a respeito do serviço a ser prestado.

O funcionamento do código está detalhado no vídeo da minha tela, que anexei aqui também de forma automatica.

Na primeira etapa alimento o código com as informações do orçamento e ele gera o PDF automaticamente.
Na segunda etapa, meu robozinho começa a atuar e tudo o que vocês vêem desde a abertura de nova aba até o envio do email, foi meu programa quem fez automaticamente. Eu sei que ficou meio lento, mas tive que respeitar o tempo da minha conexão de internet. Na primeira tentativa, o tempo de resposta do programa era 2 segundos, porém a página do email não carregou a tempo, gerando assim um defeito na minha automatização. A solução foi aumentar o tempo de resposta para 5 segundos.

E é isso galera, pense em quantas atividades repetitivas no trabalho a gente não consegue vencer através de automatização.
Trabalhar de forma inteligente é a melhor forma de focar nosso tempo e dedicação naquilo que é mais importante.

A quem interessar, meu github é: /robinunes
O código do vídeo e inclusive o código que fiz para automatizar esta postagem, estão lá.


Sigamos!

"""
pyperclip.copy (mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click (x=715, y=732)

pyperclip.copy("post_automatico.mp4")
pyautogui.hotkey("ctrl", "v")

pyautogui.click (x=1708, y=977)
pyautogui.click (x=1208, y=808)
pyautogui.click (x=1218, y=739)



# In[6]:


import time
time.sleep (10)
pyautogui.position()


# In[ ]:




