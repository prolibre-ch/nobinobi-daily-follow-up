from django import template
from typing import Optional

register = template.Library()

@register.simple_tag
def get_period_class(period, classroom: Optional['Classroom'] = None):
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

    status = period.status

    if status == "absence":
        return "bg-danger-gradient"
    elif status == "present":
        return "bg-present"
    elif status == "leave":
        return "bg-troubleshooting-gradient" if getattr(period, 'troubleshooting', False) else "bg-leave-gradient"
    elif status == "troubleshooting":
        return "bg-troubleshooting"
    elif status == "replacement_classroom":
        replacement = getattr(period, 'replacement_classroom', None)
        if replacement is not None and hasattr(classroom, 'id') and replacement.id == classroom.id:
            return "bg-replacement-classroom"
        return "bg-dark-gradient"
    elif status == "expected":
        return "bg-warning-gradient"
    else:  # Cas par défaut (statut inconnu)
        return "bg-gray"
