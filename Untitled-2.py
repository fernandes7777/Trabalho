class Configuracao:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._configuracoes = cls._carregar_configuracoes()
        return cls._instancia
    
    @staticmethod
    def _carregar_configuracoes():
        print("Carregando configurações do arquivo...")
        return {
            "temperatura": 22,
            "luminosidade": 70,
            "modo_segurança": "ativo"
        }

    def obter_configuracao(self, chave):
        return self._configuracoes.get(chave)


config1 = Configuracao()
config2 = Configuracao()

print(config1 is config2) 


temperatura = config1.obter_configuracao("temperatura")
print(f"Temperatura desejada: {temperatura}°C")  








class Pedido:
    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.status = "Criado"
        self.clientes = []  
    
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)
    
    def notificar_clientes(self):
        for cliente in self.clientes:
            cliente.atualizar(self)
    
    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"Status do Pedido {self.id_pedido} mudou para: {self.status}")
        self.notificar_clientes()

class Cliente:
    def __init__(self, nome):
        self.nome = nome
    
    def atualizar(self, pedido):
        print(f"{self.nome}, o status do seu pedido {pedido.id_pedido} agora é: {pedido.status}")


pedido1 = Pedido(1001)
cliente1 = Cliente("João")
cliente2 = Cliente("Maria")


pedido1.adicionar_cliente(cliente1)
pedido1.adicionar_cliente(cliente2)


pedido1.atualizar_status("Em Processamento")
pedido1.atualizar_status("Enviado")
pedido1.atualizar_status("Entregue")