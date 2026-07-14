from django import template
register = template.Library()

@register.simple_tag
def get_period_class(period, classroom):
    if period.absence: return "bg-danger-gradient"
    if period.status == "present": return "bg-present"
    if period.status == "leave" and period.troubleshooting: return "bg-troubleshooting-gradient"
    if period.status == "leave": return "bg-leave-gradient"
    if period.replacement_classroom == classroom: return "bg-replacement-classroom"
    if period.status == "troubleshooting": return "bg-troubleshooting"
    if period.status == "replacement_classroom": return "bg-dark-gradient"
    if period.status == "expected": return "bg-warning-gradient"
    return "bg-gray"
