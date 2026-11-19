from models import Alert


NEXT_STEPS = {
    "critical": "Investigate immediately and take corrective action.",
    "warning": "Review the affected system and monitor the metric closely.",
    "info": "Review the metric and confirm whether any action is needed.",
}


def generate_explanation(alert: Alert) -> str:
    """Generate a human-readable explanation for an alert.

    Args:
        alert: The alert whose fields are used to build the explanation.

    Returns:
        A string describing the alert, its metric comparison, and the next step.

    Raises:
        KeyError: If the alert severity is not a key in ``NEXT_STEPS``.
    """
    if alert.metric_value > alert.threshold:
        comparison = "exceeded"
    elif alert.metric_value < alert.threshold:
        comparison = "fell below"
    else:
        comparison = "reached"

    next_step = NEXT_STEPS[alert.severity]
    explanation = (
        f'This {alert.severity} alert from {alert.source} is titled "{alert.title}". '
        f"The {alert.metric_name} metric {comparison} its threshold: the current value is "
        f"{alert.metric_value}, compared with a threshold of {alert.threshold}. "
        f"Recommended next step: {next_step}"
    )

    resolved_by = getattr(alert, "resolved_by", None)
    acknowledged_by = (
        resolved_by.upper() if resolved_by is not None else "Not yet acknowledged"
    )
    return f"{explanation} Acknowledged by: {acknowledged_by}."