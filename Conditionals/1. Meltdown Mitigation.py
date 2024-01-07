"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    generated_power = voltage * current
    print(generated_power)
    efficiency = (generated_power / theoretical_max_power)*100
    print(efficiency)
    if efficiency >= 80:
        return 'green'
    if 80 > efficiency >= 60:
        return 'orange'
    if 60 > efficiency >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    condition = temperature * neutrons_produced_per_second
    if condition < (threshold * 0.9):
        return 'LOW'
    if condition in range(threshold - int(threshold * 0.1), threshold + int(threshold * 0.1)):
        return 'NORMAL'
    return 'DANGER'
    # Don't need to write else in Python in general because you can just do the function return the
    # else and write what you need as an if, very cool
