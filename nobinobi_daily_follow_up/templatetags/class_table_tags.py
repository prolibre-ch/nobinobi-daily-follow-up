from django import template
register = template.Library()

@register.simple_tag
def get_period_class(period, classroom):
    match period.status:
        case "absence": return "bg-danger-gradient"
        case "present": return "bg-present"
        case "leave":
            if period.troubleshooting: return "bg-troubleshooting-gradient"
            return "bg-leave-gradient"
        case "troubleshooting": return "bg-troubleshooting"
        case "replacement_classroom":
            if period.replacement_classroom and period.replacement_classroom.id == classroom.id: return "bg-replacement-classroom"
            return "bg-dark-gradient"
        case "expected": return "bg-warning-gradient"
        case _: return "bg-gray"
