from django import template
from typing import Dict, Optional, Any

register = template.Library()

@register.simple_tag
def get_period_class(period: Dict[str, Any], classroom: Optional[Dict[str, Any]] = None) -> str:
    """
    Retourne la classe CSS pour une période en fonction de son statut.

    Args:
        period: Dictionnaire contenant les clés 'status', 'troubleshooting' (bool), 'replacement_classroom' (dict).
        classroom: Dictionnaire optionnel contenant la clé 'id'.

    Returns:
        str: Classe CSS correspondant au statut.
    """
    status = period.get('status')
    if not isinstance(status, str):
        return "bg-gray"

    # Cas simples
    if status == "absence":
        return "bg-danger-gradient"
    elif status == "present":
        return "bg-present"
    elif status == "leave":
        troubleshooting = period.get('troubleshooting', False)
        return "bg-troubleshooting-gradient" if troubleshooting else "bg-leave-gradient"

    # Cas "troubleshooting"
    elif status == "troubleshooting":
        replacement = period.get('replacement_classroom', None)
        classroom_from_per = period.get('classroom', None)

        if replacement is not None and classroom is not None and replacement.get('id') == classroom.get('id'):
            return "bg-troubleshooting"
        if classroom_from_per is not None and classroom is not None and classroom_from_per.get('id') == classroom.get('id'):
            return "bg-troubleshooting"

        return "bg-dark-gradient"

    # Cas "replacement_classroom"
    elif status == "replacement_classroom":
        replacement = period.get('replacement_classroom')
        if replacement is not None and classroom is not None and replacement.get('id') == classroom.get('id'):
            return "bg-replacement-classroom"
        return "bg-dark-gradient"

    # Cas par défaut
    elif status == "expected":
        return "bg-warning-gradient"

    return "bg-gray"  # Statut inconnu
