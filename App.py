import customtkinter as ctk


class APP(ctk.CTk):

    def __init__(self):
        super().__init__() 
        
        
        self.layout()
        self.aplicacao()
        

    

    def formatar_numero(self, numero):
        numero_str = str(numero)
        
        # Separa a parte inteira e a parte decimal (se houver)
        partes = numero_str.split('.')
        
        # Formata a parte inteira com pontos como separadores de milhares
        parte_inteira = '{:,.0f}'.format(float(partes[0]))
        
        # Se houver parte decimal, pegue os dois primeiros dígitos
        if len(partes) > 1:
            parte_decimal = partes[1][:2]
        else:
            parte_decimal = '00'  # Se não houver parte decimal, adicione dois zeros
        
        # Separe a parte inteira em grupos de três dígitos com ponto como separador
        parte_inteira_formatada = '.'.join(parte_inteira.split(','))
        
        # Combine a parte inteira formatada, a vírgula e os dois dígitos decimais
        valor_formatado = f'{parte_inteira_formatada},{parte_decimal}'
        
        return valor_formatado
    

    def calcular(self):
        if self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric() and  self.entrymensal.get()=='' and self.periodo.get() == 'Anos' and self.juros.get() == 'Anual':
            principal = float(self.entryinicial.get())
            juros = float(self.entryjuros.get())/100
            periodo = float(self.entryperiodo.get())
            A = principal * (1 + juros) ** periodo
            intperiodo = int(periodo)
            taxajuros = round(juros,0)
            print(taxajuros)
            stringtaxajuros = f'{juros*100}% (anual)'
            valorprincipal = round(principal,2) #17.98
            print(valorprincipal)
            formatado1 = self.formatar_numero(valorprincipal) # '17.98'
            print(formatado1)
            valor_total = round(A,2) # 29.99
            print(valor_total)
            formatado2 = self.formatar_numero(valor_total) # '29,99'
            print(formatado2)
            valor_juros = round(valor_total-valorprincipal,2)
            print(valor_juros)
            formatado3=self.formatar_numero(valor_juros)
            print(formatado3)


            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=380,y=83)
            self.resultadoinicial.configure(text=f'R$ {formatado1}')
      
            self.resultadojuros.place(x=350,y=123)
            self.resultadojuros.configure(text=stringtaxajuros)
        
            self.resultadomensal.place(x=640,y=83)
            self.resultadomensal.configure(text='-')
          
            self.resultadoperiodo.place(x=640,y=123)
            self.resultadoperiodo.configure(text=f'{intperiodo} anos')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R$ {formatado3}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R$ {formatado1}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R$ {formatado2}')
           
            self.resetbutton.place(x=60,y=425)
                


            #Funcionando // Periodo --> Ano, Juros --> Ano, sem aportes mensais. // 



        
        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric() and self.entrymensal.get().isnumeric and self.periodo.get() == 'Anos' and self.juros.get() == 'Anual':
            principal = round(float(self.entryinicial.get()), 2)
            juros = float(self.entryjuros.get()) / 100
            periodo = round(float(self.entryperiodo.get()), 2)
            mensal = round(float(self.entrymensal.get()), 2)

                # Converta a taxa de juros anual em uma taxa de juros mensal
            juros_mensal = (1 + juros) ** (1/12) - 1

            # Cálculo do valor futuro (B)
            B = principal * (1 + juros_mensal) ** (12 * periodo) + mensal * (((1 + juros_mensal) ** (12 * periodo)) - 1) / juros_mensal

            # Cálculo do valor investido
            valor_investid = principal + (mensal * 12 * periodo)

            # Cálculo dos juros ganhos
            juros_ganhos = B - valor_investid

            

            valor = round(valor_investid,2)
            valor1 = self.formatar_numero(valor)

            juros_g= round(juros_ganhos,2)
            juros_gg=self.formatar_numero(juros_g)

            valor_finall = round(B,2)
            valor_finalll = self.formatar_numero(valor_finall)

            princial1= round(principal,2)
            principal2 = self.formatar_numero(princial1)

            juros1= juros*100
            jurostx = round(juros1,2)

            op = round(mensal,2)
            opi = self.formatar_numero(op)

            periodo_int = int(periodo)
        
            

            
            m1= self.formatar_numero(mensal)

            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=350,y=83)
            self.resultadoinicial.configure(text=f'R${principal2}')
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f' {jurostx}% (anual)')
        
            self.resultadomensal.place(x=600,y=83)
            self.resultadomensal.configure(text=f'R${opi}')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{periodo_int} anos')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R${juros_gg}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R${valor1}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R${valor_finalll}')

            self.resetbutton.place(x=60,y=425)



            # Funcionando // Periodo --> Ano , Juros --> Ano, com aportes mensais.
        
        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric()  and self.entrymensal.get()=='' and self.periodo.get() == 'Anos' and self.juros.get() == 'Mensal':
            principal = int(self.entryinicial.get())  # Valor inicial
            juros_mensal = int(self.entryjuros.get()) / 100  # Taxa de juros mensal (em decimal)
            periodo_anos = int(self.entryperiodo.get())  # Período em anos

            # Converta a taxa de juros mensal em uma taxa de juros anual
            juros_anual = (1 + juros_mensal) ** 12 - 1

            # Fórmula dos juros compostos sem aportes mensais
            C = principal * (1 + juros_anual) ** periodo_anos
            print('C')
            print(C)
            inicial3 = self.formatar_numero(principal)
            juros3 = self.formatar_numero(juros_mensal*100)

            valortotal = self.formatar_numero(round(C,2))
            print(valortotal)

            totaljuros = round(C,2) - principal
            print(totaljuros)



            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=380,y=83)
            self.resultadoinicial.configure(text=inicial3)
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f'{juros3}% (mensal)')
        
            self.resultadomensal.place(x=640,y=83)
            self.resultadomensal.configure(text='-')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{periodo_anos} anos')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R$ {totaljuros}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R$ {inicial3}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R$ {valortotal}')
           
            self.resetbutton.place(x=60,y=425)





            


            # Funcionando // Periodo --> Ano , Juros --> Mensal, sem aportes mensais.
        
        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric() and self.entrymensal.get().isnumeric and self.periodo.get() == 'Anos' and self.juros.get() == 'Mensal':
            principal = round(float(self.entryinicial.get()), 2)  # Valor inicial
            juros_mensal = float(self.entryjuros.get()) / 100  # Taxa de juros mensal (em decimal)
            periodo_anos = round(float(self.entryperiodo.get()), 2)  # Período em anos
            mensal = round(float(self.entrymensal.get()), 2)  # Valor mensal

            # Converta a taxa de juros mensal em uma taxa de juros anual
            juros_anual = (1 + juros_mensal) ** 12 - 1

            # Fórmula dos juros compostos com aportes mensais
            D = principal * (1 + juros_anual) ** periodo_anos + mensal * (((1 + juros_mensal) ** 12) ** periodo_anos - 1) / juros_mensal
            print('D')
            print(D)
            dd = self.formatar_numero(round(D,2))
            print(dd)
            principal1= self.formatar_numero(round(principal,2))
            print(principal1)
            valor_investido = principal + (mensal * 12 * periodo_anos)  # O montante total investido ao longo do período
            valorr_investido = self.formatar_numero(valor_investido)
            print(valorr_investido)
            mensal1= self.formatar_numero(mensal)
            vtj = D - valor_investido
            juros = self.formatar_numero(vtj)
            print(juros)
            

            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=340,y=83)
            self.resultadoinicial.configure(text=f'R$ {principal}')
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f'{juros_mensal*100}% (mensal)')
        
            self.resultadomensal.place(x=600,y=83)
            self.resultadomensal.configure(text=f'R$ {mensal1}')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{int(periodo_anos)} anos')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R$ {juros}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R$ {valorr_investido}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R$ {dd}')
           
            self.resetbutton.place(x=60,y=425)

            # Funcionando // Periodo --> Anos, Juros --> Mensal, com aportes mensais.

        
        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric() and self.entrymensal.get()=='' and self.periodo.get() == 'Meses' and self.juros.get() == 'Anual':
            principal = float(self.entryinicial.get())  # Valor inicial
            juros_anual = float(self.entryjuros.get())/100 # Taxa de juros anual (em decimal)
            periodo_meses = float(self.entryperiodo.get())  # Período em meses

            # Converta a taxa de juros anual em uma taxa de juros mensal
            juros_mensal = (1 + juros_anual) ** (1/12) - 1

            # Fórmula dos juros compostos sem aportes mensais
            E = principal * (1 + juros_mensal) ** periodo_meses
            print('E')
            print(E)
            juros_certo = juros_anual*100
            juros_certoo = int(round(juros_certo,2))
            
            
            periodo_meses_int = int(periodo_meses)
            valortotal0 =round((E),2)
            valototal1=self.formatar_numero(valortotal0)
            principal1 = int(principal)
            principal2 = self.formatar_numero(principal1)
            vj= valortotal0 - principal
            print(vj)
            
            
            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=340,y=83)
            self.resultadoinicial.configure(text=f'R$ {principal2}')
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f'{juros_certoo}% (anual)')
        
            self.resultadomensal.place(x=600,y=83)
            self.resultadomensal.configure(text=f'-')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{periodo_meses_int} meses')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R$ {vj}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R$ {principal2}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R$ {valototal1}')

            self.resetbutton.place(x=60,y=425)


            # Funcionando // Periodo --> Meses, Juros --> Anual, sem aportes mensais.

        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric() and self.entrymensal.get().isnumeric and self.periodo.get() == 'Meses' and self.juros.get() == 'Anual':
            principal = float(self.entryinicial.get())  # Valor inicial
            juros_anual = float(self.entryjuros.get())/100   # Taxa de juros anual (em decimal)
            periodo_meses = float(self.entryperiodo.get())  # Período em meses
            mensal = float(self.entrymensal.get())  # Valor mensal

            # Converta a taxa de juros anual em uma taxa de juros mensal
            juros_mensal = (1 + juros_anual) ** (1/12) - 1

            # Fórmula precisa dos juros compostos com aportes mensais e juros anuais em meses
            F = principal * ((1 + juros_mensal) ** periodo_meses) + mensal * ((((1 + juros_mensal) ** periodo_meses) - 1) / juros_mensal)

            print('F')
            print(F)


            valor_total = round(F,2)
            mensal1= round(mensal,2)
            mensal2= self.formatar_numero(mensal1)
            valortotal1 = self.formatar_numero(valor_total)
            inicial = self.formatar_numero(principal)
            juros_mensal1 = round(juros_mensal,2)
            periodo_meses_int = int(periodo_meses)

            valor_investido = principal + (mensal * periodo_meses)
            valor_investidoo = self.formatar_numero(valor_investido)
            totaljuros = valor_total - valor_investido
            totaljuross = round(totaljuros,2)


            juros_certo = juros_anual*100
            juros_certoo = int(round(juros_certo,2))
            



            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=340,y=83)
            self.resultadoinicial.configure(text=f'R$ {inicial}')
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f'{juros_certoo}% (anual)')
        
            self.resultadomensal.place(x=600,y=83)
            self.resultadomensal.configure(text=f'R$ {mensal2}')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{periodo_meses_int} meses')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R$ {totaljuross}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R$ {valor_investidoo}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R$ {valortotal1}')

            self.resetbutton.place(x=60,y=425)

            # Funcionando // Periodo --> Meses, Juros --> Anual, com aportes mensais.

        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric()and self.entrymensal.get()=='' and self.periodo.get() == 'Meses' and self.juros.get() == 'Mensal':
            principal = float(self.entryinicial.get())  # Valor inicial
            juros_mensal = float(self.entryjuros.get()) / 100  # Taxa de juros mensal (em decimal)
            periodo_meses = float(self.entryperiodo.get())  # Período em meses

            # Fórmula dos juros compostos sem aportes mensais
            G = principal * (1 + juros_mensal) ** periodo_meses
            print('G')
            print(G)
            principal0= round(principal,2)
            principal1=self.formatar_numero(principal0)
            periodo_meses_int = int(periodo_meses)
            juros_correto = juros_mensal*100
            juros_correto2 = round(juros_correto,2)

            valor_total = round(G,2)
            valoor = self.formatar_numero(valor_total)

            juross = valor_total - principal
            jurosss = round(juross,2)
            jurosS = self.formatar_numero(jurosss)
            

            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=340,y=83)
            self.resultadoinicial.configure(text=f'R$ {principal1}')
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f'{juros_correto2}% (mensal)')
        
            self.resultadomensal.place(x=600,y=83)
            self.resultadomensal.configure(text=f'-')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{periodo_meses_int} meses')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R${jurosS}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R${principal1}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R${valoor}')

            self.resetbutton.place(x=60,y=425)

            # Funcionando // Periodo --> Meses, Juros --> Meses, sem aportes mensais.

        elif self.entryinicial.get().isnumeric() and self.entryjuros.get().isnumeric() and self.entryperiodo.get().isnumeric() and self.entrymensal.get().isnumeric and self.periodo.get() == 'Meses' and self.juros.get() == 'Mensal':
            principal = round(float(self.entryinicial.get()), 2)  # Valor inicial
            juros_mensal = float(self.entryjuros.get()) / 100  # Taxa de juros mensal (em decimal)
            periodo_meses = round(float(self.entryperiodo.get()), 2)  # Período em meses
            mensal = round(float(self.entrymensal.get()), 2)  # Valor mensal

            # Fórmula correta dos juros compostos com aportes mensais
            H = principal * ((1 + juros_mensal) ** periodo_meses) + mensal * (((1 + juros_mensal) ** periodo_meses) - 1) / juros_mensal

            print('H')
            print(H)
            principal0 = round(principal,2)
            principal1 = self.formatar_numero(principal0)
            periodo_meses_int=int(periodo_meses)
            mensal0=round(mensal,2)
            mensal1=self.formatar_numero(mensal0)
            valor_total = round(H,2)
            valor_totall = self.formatar_numero(valor_total)
            valor_investido = principal + (mensal * periodo_meses)
            valor_investido1 = round(valor_investido,2)
            valor_investido2 = self.formatar_numero(valor_investido1)
            print(valor_investido2)
            txjuros = round(juros_mensal,2)*100
            print(txjuros)
            totalemjuros = valor_total - valor_investido1
            print(totalemjuros)

            self.resultado.place(x=0, y=0)

            self.meucalculo.place(x=20,y=20)
            
            self.frameinicial.place(x=220,y=80)
            
            self.framemensal.place(x=480,y=80)
             
            self.framemeperiodo.place(x=480,y=120)

            self.framejuros.place(x=220,y=120)
         
            self.labeljuros.place(x=230,y=122)
           
            self.labelinicial.place(x=230,y=83)
            
          
            self.labelmensal.place(x=490,y=83)
         
            self.labelperiodo.place(x=490,y=122)

            self.resultadoinicial.place(x=340,y=83)
            self.resultadoinicial.configure(text=f'R${principal1}')
      
            self.resultadojuros.place(x=330,y=123)
            self.resultadojuros.configure(text=f'{txjuros}% (mensal)')
        
            self.resultadomensal.place(x=600,y=83)
            self.resultadomensal.configure(text=f'R${mensal1}')
          
            self.resultadoperiodo.place(x=600,y=123)
            self.resultadoperiodo.configure(text=f'{periodo_meses_int} meses')
            
            self.labelresultado.place(x=20,y=180)
          
            self.framevalortotalfinal.place(x=200,y=260)
            
            self.framevalortotalinvestido.place(x=450,y=260)
           
            self.frametotalemjuros.place(x=700,y=260)
                                         
            self.titulovalorfinaltotal.place(x=260,y=260)
            
            self.titulovalortotalinvestido.place(x=500,y=260)
                                  
            self.titulototalemjuros.place(x=750,y=260)

            self.VALORtotaljuros.place(x=750,y=300)
            self.VALORtotaljuros.configure(text=f'R${totalemjuros}')

            self.VALORtotalinvestido.place(x=500,y=300)
            self.VALORtotalinvestido.configure(text=f'R${valor_investido2}')

            self.VALORtotalfinal.place(x=250,y=300)
            self.VALORtotalfinal.configure(text=f'R${valor_totall}')

            self.resetbutton.place(x=60,y=425)

            # Funcionando // Periodo --> Meses, Juros --> Meses , com aportes mensais.

    def layout(self):
        self.title('Calculadora de Juros Compostos')
        self.geometry('1000x500')
        
        


    

    def ler_entry_inicial(self,event):
       
        
        valor = self.entryinicial.get()
        if not valor.isnumeric() and valor  != '':
            self.LabelErrorInicial.place(x=240,y=240)
        else:
            if self.LabelErrorInicial is not None:
                self.LabelErrorInicial.place_forget()
            else:
                return
            
    def ler_entry_juros(self,event):
       
        
        valor = self.entryjuros.get()
        if not valor.isnumeric() and valor  != '':
            self.LabelErrorJuros.place(x=240,y=350)
        else:
            if self.LabelErrorJuros is not None:
                self.LabelErrorJuros.place_forget()
            else:
                return
            
    def ler_entry_mensal(self,event):
       
        
        valor = self.entrymensal.get()
        if not valor.isnumeric() and valor  != '':
            self.LabelErrorMensal.place(x=500,y=240)
        else:
            if self.LabelErrorMensal is not None:
                self.LabelErrorMensal.place_forget()
            else:
                return
    
    def ler_entry_periodo(self,event):
       
        
        valor = self.entryperiodo.get()
        if not valor.isnumeric() and valor  != '':
            self.LabelErrorPeriodo.place(x=500,y=350)
        else:
            if self.LabelErrorPeriodo is not None:
                self.LabelErrorPeriodo.place_forget()
            else:
                return
            
            
    def clear(self):
        self.entryinicial.delete(0, 'end')
        self.LabelErrorInicial.place_forget()
        self.entrymensal.delete(0, 'end')
        self.LabelErrorMensal.place_forget()
        self.entryjuros.delete(0, 'end')
        self.LabelErrorJuros.place_forget()
        self.entryperiodo.delete(0, 'end')
        self.LabelErrorPeriodo.place_forget()

    def recarregar(self):
                self.entryinicial.delete(0, 'end')
                self.LabelErrorInicial.place_forget()
                self.entrymensal.delete(0, 'end')
                self.LabelErrorMensal.place_forget()
                self.entryjuros.delete(0, 'end')
                self.LabelErrorJuros.place_forget()
                self.entryperiodo.delete(0, 'end')
                self.LabelErrorPeriodo.place_forget()
                self.VALORtotalfinal.place_forget()
                self.VALORtotalinvestido.place_forget()
                self.VALORtotaljuros.place_forget()
                self.titulototalemjuros.place_forget()
                self.titulovalortotalinvestido.place_forget()
                self.titulovalorfinaltotal.place_forget()
                self.frametotalemjuros.place_forget()
                self.framevalortotalinvestido.place_forget()
                self.framevalortotalfinal.place_forget()
                self.labelresultado.place_forget()
                self.resultadoperiodo.place_forget()
                self.resultadomensal.place_forget()
                self.resultadojuros.place_forget()
                self.resultadoinicial.place_forget()
                self.labelperiodo.place_forget()
                self.labelmensal.place_forget()
                self.labelinicial.place_forget()
                self.labeljuros.place_forget()
                self.framejuros.place_forget()
                self.framemeperiodo.place_forget()
                self.framemensal.place_forget()
                self.frameinicial.place_forget()
                self.meucalculo.place_forget()
                self.resultado.place_forget()
                self.resetbutton.place_forget()

                

                
               
 
    



    
            
    def aplicacao(self):
        
    
        self.labelfundo=ctk.CTkLabel(self,text='',bg_color='#22142b',height=1000,width=1000)
        self.labelfundo.place(x=0,y=0)



        self.Labeltitulo=ctk.CTkLabel(self,text='Calculadora de Juros Compostos',
                            bg_color='#22142b',font=('Tahoma',25),text_color='#f8f3fe',
                            height=20,width=40)
        self.Labeltitulo.place(x=330,y=50)


        
        self.Label3=ctk.CTkLabel(self,text='Valor inicial',
                            bg_color='#22142b',font=('Tahoma',15),text_color='#f8f3fe',
                            height=20,width=40)
        self.Label3.place(x=230,y=180)


        
        self.Label4=ctk.CTkLabel(self,text='Valor mensal',
                            bg_color='#22142b',font=('Tahoma',15),text_color='#f8f3fe',
                            height=20,width=40)
        self.Label4.place(x=500,y=180)


        
        self.Label5=ctk.CTkLabel(self,text='Taxa de juros',
                            bg_color='#22142b',font=('Tahoma',15),text_color='#f8f3fe',
                            height=20,width=40)
        self.Label5.place(x=230,y=290)


        
        self.Label6=ctk.CTkLabel(self,text='Período em',
                            bg_color='#22142b',font=('Tahoma',15),text_color='#f8f3fe',
                            height=20,width=40)
        self.Label6.place(x=500,y=290)


        
        self.entryinicial = ctk.CTkEntry(self,width=200,height=30,font=('Tahoma',20),
                              placeholder_text='0,00',
                              corner_radius=20,bg_color='#22142b')
        self.entryinicial.place(x=230,y=200)
        self.entryinicial.bind('<FocusOut>', self.ler_entry_inicial)
        self.LabelErrorInicial= ctk.CTkLabel(self,text='Valor inválido',
                                                 text_color='red',height=15,bg_color='#22142b',
                                                 width=40,
                                                 font=('Tahoma',20))
        self.LabelErrorInicial.place(x=230, y=220)
        self.LabelErrorInicial.place_forget()



        self.entryjuros = ctk.CTkEntry(self,width=120,height=30,font=('Tahoma',20),
                              placeholder_text='%',
                              bg_color='#22142b')
        self.entryjuros.place(x=230,y=310)
        self.entryjuros.bind('<FocusOut>', self.ler_entry_juros)
        self.LabelErrorJuros= ctk.CTkLabel(self,text='Valor inválido',
                                                 text_color='red',height=15,bg_color='#22142b',
                                                 width=40,
                                                 font=('Tahoma',20))
        self.LabelErrorJuros.place(x=300, y=220)
        self.LabelErrorJuros.place_forget()
        



        self.entrymensal = ctk.CTkEntry(self,width=200,height=30,font=('Tahoma',20),
                              placeholder_text='0,00',corner_radius=20,
                              bg_color='#22142b')
        self.entrymensal.place(x=500,y=200)
        self.entrymensal.bind('<FocusOut>', self.ler_entry_mensal)
        self.LabelErrorMensal= ctk.CTkLabel(self,text='Valor inválido',
                                                 text_color='red',height=15,bg_color='#22142b',
                                                 width=40,
                                                 font=('Tahoma',20))
        self.LabelErrorMensal.place(x=250, y=400)
        self.LabelErrorMensal.place_forget()

        


        self.entryperiodo = ctk.CTkEntry(self,width=120,height=30,font=('Tahoma',20),
                              placeholder_text='0',
                              bg_color='#22142b',)
        self.entryperiodo.place(x=500,y=310)
        self.entryperiodo.bind('<FocusOut>', self.ler_entry_periodo)
        self.LabelErrorPeriodo= ctk.CTkLabel(self,text='Valor inválido',
                                                 text_color='red',height=15,bg_color='#22142b',
                                                 width=40,
                                                 font=('Tahoma',20))
        self.LabelErrorPeriodo.place(x=250, y=400)
        self.LabelErrorPeriodo.place_forget()

        


        self.button1 = ctk.CTkButton(self,text='CALCULAR',
                                bg_color='#22142b',
                                text_color='#fff',fg_color='blue',
                                corner_radius=20,
                                font=('Tahoma',20),
                                command=self.calcular
                                )
        self.button1.place(x=700,y=425)


        
        self.button2 = ctk.CTkButton(self,text='LIMPAR',
                                bg_color='#22142b',
                                text_color='#fff',fg_color='blue',
                                corner_radius=20,command=self.clear,
                                font=('Tahoma',20),
                                )
        self.button2.place(x=850,y=425)

        self.juros= ctk.StringVar(value='Mensal')
        self.menuma = ctk.CTkOptionMenu(self,values=['Mensal','Anual'],
                                        width=20,height=30,
                                        bg_color='#22142b',
                                        font=('Tahome',15),
                                        button_color='#212325',
                                        button_hover_color='#535452',
                                        text_color='#fff',
                                        dropdown_text_color='#fff',
                                        fg_color='#343638',
                                        variable=self.juros
                                    
                                        )
        self.menuma.place(x=350,y=310)


        
        self.periodo = ctk.StringVar(value='Anos')

        self.menuperiodo = ctk.CTkOptionMenu(self,values=['Meses','Anos'],
                                        width=20,height=30,
                                        bg_color='#22142b',
                                        font=('Tahome',15),
                                        button_color='#212325',
                                        button_hover_color='#535452',
                                        text_color='#fff',
                                        dropdown_text_color='#fff',
                                        fg_color='#343638',
                                        variable=self.periodo,
                                    
                                        )
        self.menuperiodo.place(x=620,y=310)
        #-------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------
        self.resultado = ctk.CTkLabel(self,text='',bg_color='#22142b',height=1000,width=1000)
        self.resultado.place(x=0, y=0)
        self.resultado.place_forget()
        
        
        
        self.meucalculo= ctk.CTkLabel(self,text='Meu cálculo',bg_color='black',
                                      width=20,height=20,
                                      font=('Tahome',30),fg_color='#22142b')
        self.meucalculo.place(x=20,y=20)
        self.meucalculo.place_forget()

        self.frameinicial = ctk.CTkFrame(self,bg_color='#22142b',width=250,height=30,fg_color='#3c4043',
                                         corner_radius=20,)
        self.frameinicial.place(x=220,y=80)
        self.frameinicial.place_forget()

        self.framemensal = ctk.CTkFrame(self,bg_color='#22142b',width=250,height=30,fg_color='#3c4043',
                                         corner_radius=20,)
        self.framemensal.place(x=480,y=80)
        self.framemensal.place_forget()

        self.framemeperiodo = ctk.CTkFrame(self,bg_color='#22142b',width=250,height=30,fg_color='#3c4043',
                                         corner_radius=20,)
        self.framemeperiodo.place(x=480,y=120)
        self.framemeperiodo.place_forget()

        self.framejuros = ctk.CTkFrame(self,bg_color='#22142b',width=250,height=30,fg_color='#3c4043',
                                         corner_radius=20,)
        self.framejuros.place(x=220,y=120)
        self.framejuros.place_forget()


        self.labeljuros=ctk.CTkLabel(self,text='Taxa de juros',font=('Helvetica',14),width=25,height=25,
                                       bg_color='#3c4043',fg_color='#3c4043',text_color='#0d1117')
        self.labeljuros.place(x=230,y=122)
        self.labeljuros.place_forget()


        self.labelinicial=ctk.CTkLabel(self,text='Valor inicial',font=('Helvetica',14),width=25,height=25,
                                       bg_color='#3c4043',fg_color='#3c4043',text_color='#0d1117')
        self.labelinicial.place(x=230,y=83)
        self.labelinicial.place_forget()

        self.labelmensal=ctk.CTkLabel(self,text='Valor mensal',font=('Helvetica',14),width=25,height=25,
                                       bg_color='#3c4043',fg_color='#3c4043',text_color='#0d1117')
        self.labelmensal.place(x=490,y=83)
        self.labelmensal.place_forget()


        self.labelperiodo=ctk.CTkLabel(self,text='Período em',font=('Helvetica',14),width=25,height=25,
                                       bg_color='#3c4043',fg_color='#3c4043',text_color='#0d1117')
        self.labelperiodo.place(x=490,y=122)
        self.labelperiodo.place_forget()


        self.resultadoinicial = ctk.CTkLabel(self,text='inicial',font=('Helvetica',14),width=25,height=25,
                                             bg_color='#3c4043',fg_color='#3c4043',text_color='#e8f0fe')
        self.resultadoinicial.place(x=370,y=83)
        self.resultadoinicial.place_forget()


        self.resultadojuros = ctk.CTkLabel(self,text='Taxa',font=('Helvetica',14),width=25,height=25,
                                             bg_color='#3c4043',fg_color='#3c4043',text_color='#e8f0fe')
        self.resultadojuros.place(x=340,y=123)
        self.resultadojuros.place_forget()

        self.resultadomensal = ctk.CTkLabel(self,text='Mensal',font=('Helvetica',14),width=25,height=25,
                                             bg_color='#3c4043',fg_color='#3c4043',text_color='#e8f0fe')
        self.resultadomensal.place(x=550,y=83)
        self.resultadomensal.place_forget()


        self.resultadoperiodo = ctk.CTkLabel(self,text='Periodo',font=('Helvetica',14),width=25,height=25,
                                             bg_color='#3c4043',fg_color='#3c4043',text_color='#e8f0fe')
        self.resultadoperiodo.place(x=550,y=123)
        self.resultadoperiodo.place_forget()




        self.labelresultado= ctk.CTkLabel(self,text='Resultado',bg_color='black',
                                      width=20,height=20,
                                      font=('Tahome',30),fg_color='#22142b')
        self.labelresultado.place(x=20,y=180)
        self.labelresultado.place_forget()


        self.framevalortotalfinal = ctk.CTkFrame(self,bg_color='#22142b',width=230,height=100
                                                 ,fg_color='#3c4043',corner_radius=10,border_color='#22142b')
        self.framevalortotalfinal.place(x=200,y=260)
        self.framevalortotalfinal.place_forget()


        self.framevalortotalinvestido = ctk.CTkFrame(self,bg_color='#22142b',width=230,height=100
                                                 ,fg_color='#3c4043',corner_radius=10,border_color='#22142b')
        self.framevalortotalinvestido.place(x=450,y=260)
        self.framevalortotalinvestido.place_forget()

        self.frametotalemjuros = ctk.CTkFrame(self,bg_color='#22142b',width=230,height=100
                                                 ,fg_color='#3c4043',corner_radius=10,border_color='#22142b')
        self.frametotalemjuros.place(x=700,y=260)
        self.frametotalemjuros.place_forget()



        self.titulovalorfinaltotal = ctk.CTkLabel(self,text='Valor final total',width=20,height=20,
                                                  bg_color='#3c4043',fg_color='#3c4043',text_color='black',
                                                  font=('arial',15)
                                                  )
        self.titulovalorfinaltotal.place(x=260,y=260)
        self.titulovalorfinaltotal.place_forget()



        self.titulovalortotalinvestido = ctk.CTkLabel(self,text='Valor total investido',width=20,height=20,
                                                  bg_color='#3c4043',fg_color='#3c4043',text_color='black',
                                                  font=('arial',15)
                                                  )
        self.titulovalortotalinvestido.place(x=500,y=260)
        self.titulovalortotalinvestido.place_forget()




        self.titulototalemjuros = ctk.CTkLabel(self,text='Total em juros',width=20,height=20,
                                                  bg_color='#3c4043',fg_color='#3c4043',text_color='black',
                                                  font=('arial',15)
                                                  )
        self.titulototalemjuros.place(x=750,y=260)
        self.titulototalemjuros.place_forget()


        self.VALORtotaljuros= ctk.CTkLabel(self,font=('arial',17),bg_color='#3c4043',text_color='black',text='')
        self.VALORtotaljuros.place(x=750,y=300)
        self.VALORtotaljuros.place_forget()

        self.VALORtotalinvestido= ctk.CTkLabel(self,font=('arial',17),bg_color='#3c4043',text_color='black',text='')
        self.VALORtotalinvestido.place(x=500,y=300)
        self.VALORtotalinvestido.place_forget()

        self.VALORtotalfinal= ctk.CTkLabel(self,font=('arial',17),bg_color='#3c4043',text_color='black',text='')
        self.VALORtotalfinal.place(x=250,y=300)
        self.VALORtotalfinal.place_forget()

       

        self.resetbutton = ctk.CTkButton(self,text='RESET',
                                bg_color='#22142b',
                                text_color='#fff',fg_color='red',
                                corner_radius=5,
                                hover_color='#fe4648',command=self.recarregar,
                                font=('Tahoma',20),
                                )
        self.resetbutton.place(x=60,y=425)

        self.resetbutton.place_forget()
        
        
        
    



    






if __name__ == '__main__':
    app = APP()

    app.mainloop()