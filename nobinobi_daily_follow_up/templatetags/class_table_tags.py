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
    status = period.get('status')
    if not isinstance(status, str):
        return "bg-gray"

    if status == "absence":
        return "bg-danger-gradient"
    elif status == "present":
        return "bg-present"
    elif status == "leave":
        return "bg-troubleshooting-gradient" if getattr(period, 'troubleshooting', False) else "bg-leave-gradient"

    elif status == "troubleshooting":
        replacement = period.get('replacement_classroom')
        if replacement is not None:
            if replacement.id != classroom.id:
                return "bg-replacement-classroom"
            else:
                return "bg-troubleshooting"
        classroom_from_per = period.get('classroom')
        if classroom_from_per is not None and classroom_from_per.id == classroom.id:
            return "bg-troubleshooting"
        return "bg-dark-gradient"

    elif status == "replacement_classroom":
        replacement = period.get('replacement_classroom')
        if replacement is not None and replacement.id == classroom.id:
            return "bg-replacement-classroom"
        return "bg-dark-gradient"
    elif status == "expected":
        return "bg-warning-gradient"
    else:  # Cas par défaut (statut inconnu)
        return "bg-gray"
