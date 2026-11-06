import random
import sys

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.idade = 0
        self.felicidade = random.randint(50, 95)
        self.saude = random.randint(60, 100)
        self.inteligencia = random.randint(40, 100)
        self.cunha = random.randint(10, 60)
        self.aspeto = random.randint(30, 100)
        self.dinheiro = 1000
        self.vivo = True
        
        self.genero = random.choice(["Masculino", "Feminino", "Não-Binário"])
        self.orientacao = random.choice(["Hetero", "Gay", "Bi"])
        self.emprego = "Bebé"
        self.cadastro_limpo = True
        self.anos_prisao = 0
        
        self.pais = {"Pai": random.randint(60, 100), "Mãe": random.randint(60, 100)}
        self.parceiro = None
        self.filhos = []
    def gerar_cara(self):
        if not self.vivo:
            return "   💀   \n [ X_X ]"
        
        if self.idade < 3:
            topo = "   👶   "
        elif self.idade > 65:
            topo = "  [👵👴] "
        else:
            topo = "  \\\\///  " if self.genero == "Feminino" else "  |||||  "
            
        if self.saude < 30:
            olhos = " [ 👁_👁 ] \n  ( 🩺 ) "
        elif self.felicidade > 70:
            olhos = " [ ^_^ ] \n  (  ══ ) "
        else:
            olhos = " [ 😐 ] \n  (  __ ) "
            
        return f"{topo}\n{olhos}"

    def mostrar_status(self):
        print("\n" + "═"*50)
        print(self.gerar_cara())
        print(f" 👤 {self.nome} ({self.genero} | {self.orientacao}) | ⏳ {self.idade} anos")
        print(f" 💼 Carreira: {self.emprego} | 💰 Fortuna: {self.dinheiro}€")
        print(f" ❤️ Saúde: {self.saude}% | 😄 Felicidade: {self.felicidade}%")
        print(f" 🧠 Intel: {self.inteligencia}% | ✨ Aspeto: {self.aspeto}% | 🤝 Cunha: {self.cunha}%")
        print("-" * 50)
        print(f" 👨‍👩‍👦 Família -> Pai (Afeição: {self.pais['Pai']}%) | Mãe (Afeição: {self.pais['Mãe']}%)")
        if self.parceiro:
            print(f" 💍 Cônjuge: {self.parceiro} ")
        if self.filhos:
            print(f" 👶 Filhos: {', '.join(self.filhos)}")
        if self.anos_prisao > 0:
            print(f" 🚨 EM CANA: Faltam {self.anos_prisao} anos de pena!")
        print("═"*50)
    def envelhecer(self):
        self.idade += 1
        
        if self.anos_prisao > 0:
            self.anos_prisao -= 1
            self.felicidade = max(10, self.felicidade - 15)
            self.saude = max(10, self.saude - 5)
            print(f"\n⛓️ Passaste mais um ano na prisão. Faltam {self.anos_prisao} anos.")
            if self.anos_prisao == 0:
                self.emprego = "Ex-Presidiário Desempregado"
            return

        tabela_salarios = {
            "Bebé": 0, "Estudante": 50, "Desempregado": 0, "Ex-Presidiário Desempregado": 0,
            "Influencer de TikTok": 1200, "Ator de Novelas": 3500, "Jogador do Benfica": 15000,
            "Técnico de IT": 1800, "Médico de Santa Maria": 4500,
            "Deputado da Nação": 3800, "Administrador Público (Cunha Máxima)": 9000,
            "Líder de Cartel": 25000
        }
        
        salario = tabela_salarios.get(self.emprego, 1000)
        if salario > 0:
            imposto = int(salario * 0.35)
            liquido = salario - imposto
            self.dinheiro += liquido
            print(f"\n💰 Salário de {self.emprego}: +{liquido}€ (IRS: -{imposto}€)")

        if self.idade > 75 and random.random() < 0.2:
            self.saude -= random.randint(10, 30)
        
        if self.saude <= 0:
            self.vivo = False
            print(f"\n💀 GAME OVER: {self.nome} faleceu aos {self.idade} anos com {self.dinheiro}€.")
            return

        self.gerar_evento_aleatorio()

    def gerar_evento_aleatorio(self):
        if self.idade == 6:
            self.emprego = "Estudante"
        elif self.idade == 18 and self.emprego == "Estudante":
            self.emprego = "Desempregado"
            print("\n🎓 Terminaste os estudos secundários! Hora de decidir a tua vida.")

        if random.random() < 0.4:
            eventos = [
                "A tua conta de Instagram tornou-se viral! (+20% Aspeto)",
                "O teu pai pediu-te dinheiro emprestado para jogar no Placard.",
                "Foste apanhado numa rusga na discoteca. (-10% Felicidade)",
                "Herdaste uma herança de um tio afastado da Suíça! (+8000€)",
                "O teu parceiro quer discutir a relação. (-15% Felicidade)"
            ]
            ev = random.choice(eventos)
            print(f"\n✨ EVENTO: {ev}")
            if "Instagram" in ev: self.aspeto = min(100, self.aspeto + 20)
            if "Suíça" in ev: self.dinheiro += 8000
    def gerir_carreiras(self):
        print("\n--- 💼 MERCADO DE TRABALHO & CARREIRAS ---")
        print("1. Rota Fama: Influencer (Requer: Aspeto > 70)")
        print("2. Rota Fama: Ator de Novelas (Requer: Aspeto > 85, Inteligência > 50)")
        print("3. Rota Desporto: Jogador do Benfica (Requer: Saúde > 90)")
        print("4. Rota Intelectual: Técnico de IT (Requer: Inteligência > 70)")
        print("5. Rota Intelectual: Médico (Requer: Inteligência > 90, Saúde > 70)")
        print("6. Rota Cunha: Deputado da Nação (Requer: Cunha > 50)")
        print("7. Rota Cunha: Administrador Estatal (Requer: Cunha > 85)")
        
        op = input("Submeter candidatura para a rota: ")
        if op == "1" and self.aspeto > 70: self.emprego = "Influencer de TikTok"
        elif op == "2" and self.aspeto > 85 and self.inteligencia > 50: self.emprego = "Ator de Novelas"
        elif op == "3" and self.saude > 90: self.emprego = "Jogador do Benfica"
        elif op == "4" and self.inteligencia > 70: self.emprego = "Técnico de IT"
        elif op == "5" and self.inteligencia > 90 and self.saude > 70: self.emprego = "Médico de Santa Maria"
        elif op == "6" and self.cunha > 50: self.emprego = "Deputado da Nação"
        elif op == "7" and self.cunha > 85: self.emprego = "Administrador Público (Cunha Máxima)"
        else:
            print("\n❌ Rejeitado! Não tens os requisitos ou os connects (Cunha) necessários.")
            return
        print(f"\n🎉 Parabéns! Agora és oficialmente: {self.emprego}")
    def gerir_relacionamentos(self):
        print("\n--- 💍 RELACIONAMENTOS & FAMÍLIA ---")
        print("1. Passar tempo com os Pais (+Afeição)")
        print("2. Ir ao Tinder procurar parceiro")
        print("3. Ter um filho (Requer parceiro, Custo: 500€)")
        
        op = input("O que queres fazer? ")
        if op == "1":
            self.pais["Pai"] = min(100, self.pais["Pai"] + 15)
            self.pais["Mãe"] = min(100, self.pais["Mãe"] + 15)
            self.felicidade = min(100, self.felicidade + 10)
            print("\n❤️ Almoçaste com os teus pais. Eles adoraram ver-te.")
        elif op == "2":
            if self.parceiro:
                print("\n❌ Já tens um parceiro!")
                return
            nomes = ["Cláudio", "Mariana", "Tiago", "Filipa", "Inês", "Gonçalo"]
            self.parceiro = random.choice(nomes)
            print(f"\n💘 Match! Começaste a namorar com: {self.parceiro}")
            self.felicidade = min(100, self.felicidade + 20)
        elif op == "3":
            if not self.parceiro:
                print("\n❌ Precisas de um parceiro primeiro.")
                return
            if self.dinheiro < 500:
                print("\n❌ Não tens dinheiro para as despesas do bebé.")
                return
            self.dinheiro -= 500
            nome_filho = random.choice(["Martim", "Leonor", "Santiago", "Matilde"])
            self.filhos.append(nome_filho)
            print(f"\n👶 Nasceu! Deste o nome de {nome_filho} ao teu filho.")
            self.felicidade = min(100, self.felicidade + 30)
    def menu_crime(self):
        print("\n--- 🕶️ SUBMUNDO DO CRIME ---")
        print("1. Roubar carteiras no Elétrico 28")
        print("2. Tráfico de Influência na Câmara Municipal")
        print("3. Fundar um Cartel de Droga Internacional")
        
        op = input("Qual o teu golpe? ")
        sucesso = random.random() < ((self.cunha + self.inteligencia) / 200.0)
        
        if op == "1":
            if random.random() < 0.7:
                self.dinheiro += 250
                print("\n💰 Limpaste duas carteiras a turistas! (+250€)")
            else:
                print("\n🚨 A PSP apanhou-te em flagrante!")
                self.ir_para_prisao(2)
        elif op == "2":
            if sucesso:
                self.dinheiro += 4000
                self.cunha = min(100, self.cunha + 20)
                print("\n💰 Cunhas cruzadas com sucesso! Recebeste subornos. (+4000€)")
            else:
                print("\n🚨 Investigação da PJ! Foste apanhado nas escutas.")
                self.ir_para_prisao(5)
        elif op == "3":
            if sucesso and self.inteligencia > 80:
                self.emprego = "Líder de Cartel"
                self.dinheiro += 30000
                print("\n👑 Controlas as rotas marítimas! És o novo Barão de Portugal.")
            else:
                print("\n🚨 Operação da Europol! O teu império ruiu.")
                self.ir_para_prisao(12)

    def ir_para_prisao(self, anos):
        print(f"\n👨‍⚖️ Sentenciado! Foste condenado a {anos} anos de prisão efetiva.")
        self.anos_prisao = anos
        self.emprego = "Prisioneiro"
        self.cadastro_limpo = False
def jogar():
    print("═" * 50)
    print("       👑 CUNHA LIFE v2.0 COMPLETE EDITION 👑       ")
    print("═" * 50)
    nome = input("Digita o nome do teu avatar: ")
    p = Personagem(nome)
    
    while p.vivo:
        p.mostrar_status()
        print("\nAÇÕES DO TURNO:")
        print("1 ⏳ Avançar 1 Ano (Envelhecer)")
        print("2 💼 Menu de Carreiras (Fama/Média/Cunha)")
        print("3 💍 Menu de Família & Relacionamentos")
        print("4 🕶️ Atividades Criminosas")
        print("5 💪 Ir à Clínica Privada (+Saúde | Custa 200€)")
        print("6 ❌ Desistir da Vida (Sair)")
        
        escolha = input("\nEscolha a sua ação: ")
        
        if escolha == "1": p.envelhecer()
        elif escolha == "2": p.gerir_carreiras()
        elif escolha == "3": p.gerir_relacionamentos()
        elif escolha == "4": p.menu_crime()
        elif escolha == "5":
            if p.dinheiro >= 200:
                p.dinheiro -= 200
                p.saude = min(100, p.saude + 25)
                print("\n🔬 Consulta feita! Recuperaste 25% de Saúde.")
            else:
                print("\n❌ Sem saldo para o privado. O SNS está com lista de espera.")
        elif escolha == "6":
            print("\nA fechar o jogo..."); break
        else:
            print("\n⚠️ Comando inválido.")

if __name__ == "__main__":
    jogar()
