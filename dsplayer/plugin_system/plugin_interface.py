from abc import ABC, abstractmethod
from typing import List, Dict, Any

class PluginInterface(ABC):
    @abstractmethod
    def on_plugin_load(self) -> None:
        """Вызывается при загрузке плагина"""
        pass

    @abstractmethod
    def on_plugin_unload(self) -> None:
        """Вызывается при выгрузке плагина"""
        pass

    @abstractmethod
    def get_plugin_name(self) -> str:
        """Возвращает имя плагина"""
        pass

    @abstractmethod
    def search(self, data: str) -> list[Dict[str, Any]]:
        """Ищет трек по запросу или url и возвращает информацию о треке"""
        pass

    @abstractmethod
    def get_url_patterns(self) -> list:
        """Возвращает список паттернов для url"""
        pass

    def get_settings(self) -> Dict[str, Any]:
        """Возвращает текущие настройки плагина"""
        return {}

    def update_settings(self, settings: Dict[str, Any]) -> None:
        """Обновляет настройки плагина"""
        pass