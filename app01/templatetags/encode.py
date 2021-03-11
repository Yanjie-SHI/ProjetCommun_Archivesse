from django import template

register = template.Library()


@register.filter
def encode(value):
    value = value.replace(" ", "%20")
    value = value.replace("\"", "%22")
    value = value.replace("#", "%23")
    value = value.replace("%", "%25")
    value = value.replace("&", "%26")
    value = value.replace("(", "%28")
    value = value.replace(")", "%29")
    value = value.replace("+", "%2B")
    value = value.replace(",", "%2C")
    value = value.replace("/", "%2F")
    value = value.replace(":", "%3A")
    value = value.replace(";", "%3B")
    value = value.replace("<", "%3C")
    value = value.replace("=", "%3D")
    value = value.replace(">", "%3E")
    value = value.replace("?", "%3F")
    value = value.replace("@", "%40")
    value = value.replace("\\", "%5C")
    value = value.replace("|", "%7C")
    return value
