from django import template
from typing import Optional

register = template.Library()

@register.simple_tag
def get_period_class(period, classroom = None):
    """
    Retourne la classe CSS pour une période en fonction de son statut.

    Args:
        period: Instance de Period avec les attributs status, troubleshooting, replacement_classroom.
        classroom: Instance de Classroom (optionnelle).

    Returns:
        str: Classe CSS correspondant au statut.
    """
    if not hasattr(period, 'status'):
        return "bg-gray"

    match period.status:
        case "absence":
            return "bg-danger-gradient"
        case "present":
            return "bg-present"
        case "leave":
            return "bg-troubleshooting-gradient" if getattr(period, 'troubleshooting', False) else "bg-leave-gradient"
        case "troubleshooting":
            return "bg-troubleshooting"
        case "replacement_classroom":
            replacement = getattr(period, 'replacement_classroom', None)
            if replacement is not None and hasattr(classroom, 'id') and replacement.id == classroom.id:
                return "bg-replacement-classroom"
            return "bg-dark-gradient"
        case "expected":
            return "bg-warning-gradient"
        case _:  # Cas par défaut (statut inconnu)
            return "bg-gray"
