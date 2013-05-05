#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import mechanize
import cookielib
import os


class Iconecta(object):

    def __init__(self):
        self.login, self.senha = self.autentica()

    def configura(self):
        #cria um navegador, um browser de codigo...
        br = mechanize.Browser()
        url = 'http://franquia.ostras.net/'

        # Prepara para tratar cookies...
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Ajusta algumas opções do navegador...
        br.set_handle_equiv(True)
        br.set_handle_gzip(False)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Configura o user-agent.
        # Do ponto de vista do servidor, o navegador agora o Firefox.
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11;\
         U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615\
        Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        # Pronto! Agora é navegar, acessando a URL usando o método HTTP GET
        br.open(url)

        # Se existirem formulários, você pode selecionar o primeiro (#0), por exemplo..
        br.select_form(nr=0)

        # Para mostrar os formularios e ver os campos a serem preenchidos,
        # use um for sobre o br.forms()
        #for f in br.forms():
        #    print f

        # Preencher o formulário com os dados de login...
        br.form['l'] = self.login
        br.form['p'] = self.senha

        # Enviar o formulário usando o método HTTP POST
        br.submit()

        # E finalmente, busque o HTML retornado:
        html = br.response().read()

        #Salva o codigo HTML em um arquivo
        arq = open('t.txt', 'w')
        arq.write(html)
        arq.close()

    def franquia(self):
        #Filtra o consumo
        for line in open('t.txt'):
            if 'Consumo Total em MBs:' in line:
                consumo = line

        os.remove('t.txt')

        #Retorna só até o '<div'
        return consumo[0:-72]

    def autentica(self):
        arq = open('autenticacao.txt')
        arquivo = arq.readlines()
        arq.close()
        DADOS = ()

        login = arquivo[0].rstrip("\n")
        senha = arquivo[1].rstrip("\n")
        DADOS = (login, senha)

        return DADOS
