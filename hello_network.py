def get_device_status(device_name):
    return f"Device {device_name} is up and reachable via API."

def get_device_health_score(device_name):
    # fake health score for practice
    return 95

if __name__ == "__main__":
    device = "core-switch-01"
    print("Hello DevNet, testing branches with Git!")
    print(get_device_status(device))
    print(f"Health score for {device}: {get_device_health_score(device)}%")
