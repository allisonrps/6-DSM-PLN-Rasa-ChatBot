from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


# =========================
# 1) Validar SABOR
# =========================
class ActionValidarSabor(Action):
    def name(self) -> Text:
        return "action_validar_sabor"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:

        sabor = tracker.get_slot("sabor")
        sabores_validos = ["calabresa", "mussarela", "frango", "portuguesa"]

        if sabor and sabor.lower() in sabores_validos:
            dispatcher.utter_message(text=f"Boa escolha! Temos {sabor}.")
        else:
            dispatcher.utter_message(
                text="Desculpe, não temos esse sabor. Os disponíveis são: calabresa, mussarela, frango e portuguesa."
            )

        return []


# =========================
# 2) Validar TAMANHO
# =========================
class ActionValidarTamanho(Action):
    def name(self) -> Text:
        return "action_validar_tamanho"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:

        tamanho = tracker.get_slot("tamanho")
        tamanhos_validos = ["pequena", "média", "media", "grande"]

        if tamanho and tamanho.lower() in tamanhos_validos:
            dispatcher.utter_message(text=f"Beleza, uma pizza {tamanho}.")
        else:
            dispatcher.utter_message(
                text="Não entendi o tamanho 😅. Temos pequena, média e grande."
            )

        return []


# =========================
# 3) Mostrar CARDÁPIO + PREÇOS
# =========================
class ActionMostrarCardapioPreco(Action):
    def name(self) -> Text:
        return "action_mostrar_cardapio_preco"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:

        cardapio = """
🍕 Nosso cardápio de pizzas:

➡️ Sabores:
- Calabresa → R$ 35,00
- Mussarela → R$ 32,00
- Frango → R$ 38,00
- Portuguesa → R$ 40,00

➡️ Tamanhos:
- Pequena → - R$ 5,00
- Média → preço padrão
- Grande → + R$ 10,00

➡️ Bordas:
- Recheada → +R$ 5,00
- Vulcão → +R$ 7,00
- Fina → sem acréscimo
- Sem borda → sem acréscimo
        """

        dispatcher.utter_message(text=cardapio)
        return []


# =========================
# 4) Informar ENTREGA
# =========================
class ActionInformarEntrega(Action):
    def name(self) -> Text:
        return "action_informar_entrega"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:

        entrega_info = """
🚚 Fazemos entregas em toda a cidade!  
- Taxa: R$ 5,00  
- Tempo médio: até 40 minutos  
- Promoção: pedidos acima de R$ 80 têm entrega grátis 🎉
        """
        dispatcher.utter_message(text=entrega_info)
        return []
