import json
import os
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ScheduleManager:
    """
    Gerencia o cronograma (fila de reprodução) do culto.
    Implementa o requisito FR-013.
    """
    
    def __init__(self, storage_file="schedule.json"):
        """
        Inicializa o gerenciador e carrega o cronograma salvo.
        """
        self.storage_file = storage_file
        self.items = []
        self.load_schedule()

    def add_item(self, media_item):
        """
        Adiciona um novo item (LOCAL_FILE ou YT_LINK) ao cronograma.
        Input: media_item (dict)
        """
        # Garante que o item tenha um ID único
        if 'id' not in media_item:
            import uuid
            media_item['id'] = str(uuid.uuid4())
            
        self.items.append(media_item)
        self.save_schedule()
        logging.info(f"Item adicionado ao cronograma: {media_item.get('title')}")
        return media_item

    def remove_item(self, item_id):
        """
        Remove um item pelo ID.
        """
        self.items = [item for item in self.items if item.get('id') != item_id]
        self.save_schedule()
        logging.info(f"Item {item_id} removido do cronograma.")

    def reorder_items(self, new_order_ids):
        """
        Reordena a lista baseada em uma nova sequência de IDs.
        Input: new_order_ids (list of str)
        """
        ordered_items = []
        for item_id in new_order_ids:
            item = next((i for i in self.items if i.get('id') == item_id), None)
            if item:
                ordered_items.append(item)
        
        self.items = ordered_items
        self.save_schedule()
        logging.info("Cronograma reordenado.")

    def get_schedule(self):
        """
        Retorna a lista atual de itens.
        """
        return self.items

    def save_schedule(self):
        """
        Persiste o cronograma em um arquivo JSON.
        """
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(self.items, f, indent=4, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Erro ao salvar cronograma: {e}")

    def load_schedule(self):
        """
        Carrega o cronograma do arquivo JSON.
        """
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    self.items = json.load(f)
                logging.info(f"Cronograma carregado com {len(self.items)} itens.")
            except Exception as e:
                logging.error(f"Erro ao carregar cronograma: {e}")
                self.items = []
        else:
            self.items = []

# Teste simples
if __name__ == "__main__":
    manager = ScheduleManager()
    manager.add_item({'title': 'Hino de Entrada', 'type': 'LOCAL_FILE', 'path': 'media/hino1.mp3'})
    print(manager.get_schedule())
