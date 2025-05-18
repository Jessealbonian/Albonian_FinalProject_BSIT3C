from django import template

register = template.Library()

@register.filter
def format_count(value):
    """Formats count with commas (e.g., 1000 -> 1,000)."""
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value  # Return original value if conversion fails
